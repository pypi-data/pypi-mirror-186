import dataclasses
import datetime as dt
import decimal
import inspect
import json
import os
import re
from pathlib import Path
from typing import Dict, Iterable, List, Optional

import sqlglot
import yaml
from sqlglot.expressions import Expression

from chalk import OfflineResolver, OnlineResolver
from chalk.features import DataFrame, Feature, Features, FeatureSetBase
from chalk.features.resolver import ResolverArgErrorHandler
from chalk.serialization.codec import FEATURE_CODEC
from chalk.sql import TableIngestProtocol
from chalk.sql._internal.integrations.bigquery import BigQuerySourceImpl
from chalk.sql._internal.integrations.cloudsql import CloudSQLSourceImpl
from chalk.sql._internal.integrations.mysql import MySQLSourceImpl
from chalk.sql._internal.integrations.postgres import PostgreSQLSourceImpl
from chalk.sql._internal.integrations.redshift import RedshiftSourceImpl
from chalk.sql._internal.integrations.snowflake import SnowflakeSourceImpl
from chalk.sql._internal.integrations.sqlite import SQLiteFileSourceImpl
from chalk.sql._internal.sql_source import BaseSQLSource

_SOURCES = {
    "snowflake": SnowflakeSourceImpl,
    "postgres": PostgreSQLSourceImpl,
    "postgresql": PostgreSQLSourceImpl,
    "mysql": MySQLSourceImpl,
    "bigquery": BigQuerySourceImpl,
    "cloudsql": CloudSQLSourceImpl,
    "redshift": RedshiftSourceImpl,
    "sqlite": SQLiteFileSourceImpl,
}

_RESOLVER_TYPES = {
    "offline": OfflineResolver,
    "batch": OfflineResolver,
    "online": OnlineResolver,
    "realtime": OnlineResolver,
}

_LIST_PARAMETERS = ["environment", "tags"]


@dataclasses.dataclass
class ResolverError:
    """Generic class for returning errors at any point during resolution process"""

    display: str
    path: str
    parameter: Optional[str]


@dataclasses.dataclass
class ResolverResult:
    """Chief return class with resolver we actually use"""

    resolver: Optional[OnlineResolver]
    errors: List[ResolverError]
    db: Optional[TableIngestProtocol]
    fields: Optional[Dict[str, str]]
    args: Optional[Dict[str, str]]


@dataclasses.dataclass
class SQLStringResult:
    """Class for getting the sql string from the file"""

    path: str
    sql_string: Optional[str]
    error: Optional[ResolverError]

    @classmethod
    def fail(cls, display_error: str, path: str) -> "SQLStringResult":
        return cls(path=path, sql_string=None, error=ResolverError(display=display_error, path=path, parameter=None))


@dataclasses.dataclass
class GlotResult:
    """Class for editing the sql string, and using sqlglot on sql string"""

    sql_string: str
    glot: Optional[Expression]
    args: Optional[Dict[str, str]]
    default_args: List[Optional[str]]
    errors: List[ResolverError]


@dataclasses.dataclass
class ParseResult:
    """Class for important info gathered from glot"""

    sql_string: str
    comment_dict: Optional[Dict[str, str]]
    fields: Optional[Dict[str, str]]
    namespace: Optional[str]
    source: Optional[BaseSQLSource]
    docstring: Optional[str]
    errors: List[ResolverError]


def get_sql_file_resolvers(
    sql_file_resolve_location: Path, sources: Iterable[BaseSQLSource]
) -> Iterable[ResolverResult]:
    """Iterate through all `.chalk.sql` filepaths, gather the sql strings, and get a resolver hopefully for each."""
    for dp, dn, fn in os.walk(os.path.expanduser(sql_file_resolve_location)):
        for f in fn:
            filepath = os.path.join(dp, f)
            if not filepath.endswith(".chalk.sql"):
                continue
            sql_string_result = _get_sql_string(filepath)
            yield get_sql_file_resolver(sources, sql_string_result)


def get_sql_file_resolver(sources: Iterable[BaseSQLSource], sql_string_result: SQLStringResult) -> ResolverResult:
    """Parse the sql strings and get a ResolverResult from each"""
    if sql_string_result.error:
        return ResolverResult(resolver=None, errors=[sql_string_result.error], db=None, fields=None, args=None)
    path = sql_string_result.path

    errors: List[ResolverError] = []
    glot_result: GlotResult = _get_sql_glot(sql_string_result.sql_string, path)
    if glot_result.errors:
        return ResolverResult(resolver=None, errors=glot_result.errors, db=None, fields=None, args=None)

    parsed: ParseResult = _parse_glot(glot_result, path, sources)
    if parsed.errors:
        return ResolverResult(resolver=None, errors=parsed.errors, db=parsed.source, fields=None, args=None)

    incremental_dict = parsed.comment_dict.get("incremental")
    return_one = parsed.comment_dict.get("count") == "one"

    # function for online resolver to process
    def fn(
        *input_values,
        database=parsed.source,
        sql_query=parsed.sql_string,
        field_dict=parsed.fields,
        args_dict=glot_result.args,
        incremental=incremental_dict,
    ):
        arg_dict = {arg: input_value for input_value, arg in zip(input_values, args_dict.keys())}
        func = database.query_string(
            query=sql_query,
            fields=field_dict,
            args=arg_dict,
        )
        if incremental:
            func = func.incremental(**incremental)
        if return_one:
            func = func.one()
        return func

    # validate inputs and outputs as real features in graph
    inputs: List[Feature] = []
    for arg in glot_result.args.values():
        try:
            inputs.append(Feature.from_root_fqn(arg))
        except Exception as e:
            errors.append(
                ResolverError(display=f"Cannot find input feature '{arg}' in graph, {e}", path=path, parameter=arg)
            )
    outputs: List[Feature] = []
    for output in parsed.fields.values():
        try:
            outputs.append(Feature.from_root_fqn(output))
        except Exception as e:
            errors.append(
                ResolverError(
                    display=f"Cannot find output feature '{output}' in graph, {e}", path=path, parameter=output
                )
            )
    result = ResolverResult(resolver=None, errors=errors, db=parsed.source, fields=None, args=None)

    if result.errors:
        return result

    if return_one:
        output = Features[tuple(outputs)]
    else:
        output = DataFrame[tuple(outputs)]

    resolver_type = OnlineResolver
    if parsed.comment_dict.get("type"):
        resolver_type = _RESOLVER_TYPES[parsed.comment_dict["type"]]

    default_args = [ResolverArgErrorHandler(default_value) for default_value in glot_result.default_args]

    # cast singletons as lists of size one for 'environment' and 'tags' parameters
    for parameter_name in _LIST_PARAMETERS:
        parameter = parsed.comment_dict.get(parameter_name)
        if isinstance(parameter, str):
            parsed.comment_dict[parameter_name] = [parameter]
        if parsed.comment_dict.get(parameter_name) and not isinstance(parsed.comment_dict[parameter_name], list):
            result.errors.append(
                ResolverError(
                    display=f"Parameter '{parameter_name}' value {parsed.comment_dict[parameter_name]} should be a list",
                    path=path,
                    parameter=parameter_name,
                )
            )
            return result

    # attempt to instantiate the resolver
    try:
        resolver = resolver_type(
            filename=path,
            function_definition=_remove_comments(sql_string_result.sql_string),
            fqn=path.replace(".chalk.sql", ""),
            doc=parsed.docstring,
            inputs=inputs,
            output=output,
            fn=fn,
            environment=parsed.comment_dict.get("environment"),
            tags=parsed.comment_dict.get("tags"),
            max_staleness=parsed.comment_dict.get("max_staleness"),
            cron=parsed.comment_dict.get("cron"),
            machine_type=parsed.comment_dict.get("machine_type"),
            when=None,
            state=None,
            default_args=default_args,
            owner=parsed.comment_dict.get("owner"),
        )
    except Exception as e:
        result.errors.append(
            ResolverError(
                display=f"{resolver_type.capitalize()} resolver could not be instantiated, {e}",
                path=path,
                parameter=None,
            )
        )
        return result

    result.resolver = resolver
    result.fields = parsed.fields
    result.args = glot_result.args
    return result


def _get_sql_string(path: str) -> SQLStringResult:
    """Attempt to get a sql string from a filepath and gracefully exit if unable to"""
    sql_string_result = SQLStringResult(path=path, sql_string=None, error=None)
    if not path.endswith(".chalk.sql"):
        return SQLStringResult.fail(display_error=f"sql resolver file '{path}' must end in '.chalk.sql'", path=path)
    sql_string = None
    if os.path.isfile(path):
        with open(path) as f:
            sql_string = f.read()
    else:
        caller_filename = inspect.stack()[1].filename
        dir_path = os.path.dirname(os.path.realpath(caller_filename))
        if isinstance(path, bytes):
            path = path.decode("utf-8")
        relative_path = os.path.join(dir_path, path)
        if os.path.isfile(relative_path):
            with open(relative_path) as f:
                sql_string = f.read()
    if sql_string is None:
        return SQLStringResult.fail(display_error=f"Cannot find file '{path}'", path=path)
    sql_string_result.sql_string = sql_string
    return sql_string_result


def _get_sql_glot(sql_string: str, path: str) -> GlotResult:
    """Get sqlglot from sql string and gracefully exit if unable to"""
    glot_result = GlotResult(sql_string=sql_string, glot=None, args=None, default_args=[], errors=[])
    args = {}  # sql string -> input feature string
    variables = set(re.findall("\\${.*?\\}", sql_string))
    # replace ?{variable_name} with :variable_name for sqlalchemy, and keep track of input args necessary
    for variable_pattern in variables:
        has_default_arg = False
        variable = variable_pattern[2:-1]  # cut off ${ and }
        for split_var in ["|", " or "]:  # default argument
            # TODO cannot parse something like {Transaction.category or "Waffles or Pancakes"} yet
            if split_var in variable:
                split = variable.split(split_var)
                if len(split) != 2:
                    glot_result.errors.append(
                        ResolverError(
                            display=f"If character '|' is used, both variable name and default value must be "
                            f'specified in ({variable}) like \'?{{variable_name | "default_value"}}',
                            path=path,
                            parameter=None,
                        )
                    )
                else:  # has default argument
                    variable = split[0].strip()
                    default_arg = split[1].strip()
                    glot_result.default_args.append(FEATURE_CODEC.decode_fqn(variable, json.loads(default_arg)))
                    has_default_arg = True
        if not has_default_arg:
            # TODO default value of None should be refactored since None is a legitimate default value
            glot_result.default_args.append(None)
        period_replaced = variable.replace(".", "_")
        sql_safe_str = f"__chalk_{period_replaced}__"
        sql_string = sql_string.replace(variable_pattern, f":{sql_safe_str}")
        args[sql_safe_str] = variable

    glot_result.sql_string = sql_string
    glot_result.args = args
    try:
        glot_result.glot = sqlglot.parse_one(glot_result.sql_string)
    except Exception as e:
        glot_result.errors.append(
            ResolverError(display=f"Cannot SQL parse {glot_result.sql_string}, {e}", path=path, parameter=None)
        )
        return glot_result
    if not isinstance(glot_result.glot, sqlglot.expressions.Select):
        glot_result.errors.append(
            ResolverError(
                display=f"SQL query {glot_result.sql_string} should be of 'SELECT' type", path=path, parameter=None
            )
        )
    return glot_result


def _parse_glot(glot_result: GlotResult, path: str, sources: Iterable[BaseSQLSource]) -> ParseResult:
    """Parse useful info from sqlglot and gracefully exit if unable to"""
    parse_result = ParseResult(
        sql_string=glot_result.sql_string,
        comment_dict=None,
        fields=None,
        namespace=None,
        source=None,
        docstring=None,
        errors=[],
    )

    # parse comments into dictionary
    comments = ""
    docstring = ""
    for comment in glot_result.glot.comments:
        if comment.strip().startswith("-"):
            comments += f"{comment}\n"
        else:
            split = comment.split(":")
            if len(split) != 2:
                docstring += f"{comment.strip()}\n"
            else:
                comments += f"{comment}\n"
    try:
        comment_dict = yaml.safe_load(comments)
    except Exception as e:
        parse_result.errors.append(
            ResolverError(
                display=f"Comments key-values '{comments}' must be of YAML form, {e}",
                path=path,
                parameter=comments,
            )
        )

    if parse_result.errors:
        return parse_result
    parse_result.comment_dict = comment_dict
    parse_result.docstring = docstring.strip()

    # define a source SQL database. Can either specify name or kind if only one of the kind is present.
    source_name = parse_result.comment_dict.get("source")
    if not source_name:
        parse_result.errors.append(
            ResolverError(
                display=f"Missing value for 'source'. "
                f"Please specify via source type in {list(_SOURCES.keys())}, "
                f"or via source name in {[source.name for source in sources]}",
                path=path,
                parameter="source",
            )
        )
        return parse_result

    source = None
    if source_name not in _SOURCES:  # actual name of source
        for possible_source in sources:
            if possible_source.name == source_name:
                source = possible_source
    else:
        for possible_source in sources:
            if isinstance(possible_source, _SOURCES.get(source_name)):
                if source:
                    parse_result.errors.append(
                        ResolverError(
                            display=f"More than one {source_name} source exists. Instead, refer to the integration by "
                            f"name among ({[source.name for source in sources]}).",
                            path=path,
                            parameter=source_name,
                        )
                    )
                source = possible_source
    if not source:
        parse_result.errors.append(
            ResolverError(display=f"Source {source_name} not found", path=path, parameter=source_name)
        )
    parse_result.source = source

    if parse_result.errors:
        return parse_result

    # get resolver fields: which columns selected will match to which chalk feature?
    namespace = parse_result.comment_dict.get("resolves")
    # TODO: should handle parsing of 'resolves' list of features instead of namespace in the future
    if not namespace:
        parse_result.errors.append(
            ResolverError(
                display=f"Key 'resolves' must be described in comments. "
                f"Please choose one of the feature classes in {list(FeatureSetBase.registry.keys())}.",
                path=path,
                parameter=source_name,
            )
        )
        return parse_result
    parse_result.namespace = namespace
    fields = {}  # sql string -> output feature string

    for column_name in glot_result.glot.named_selects:
        fields[column_name] = f"{namespace}.{column_name}"
    parse_result.fields = fields

    return parse_result


def _remove_comments(sql_string: str) -> str:
    sql_string = re.sub(
        re.compile("/\\*.*?\\*/", re.DOTALL), "", sql_string
    )  # remove all occurrences streamed comments (/*COMMENT */) from string
    sql_string = re.sub(
        re.compile("//.*?\n"), "", sql_string
    )  # remove all occurrence single-line comments (//COMMENT\n ) from string
    sql_string = re.sub(
        re.compile("--.*?\n"), "", sql_string
    )  # remove all occurrence single-line comments (//COMMENT\n ) from string
    return sql_string.strip()
