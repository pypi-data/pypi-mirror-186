from datetime import datetime
from typing import Optional

import pytest

from chalk.features import feature, feature_time, features, has_one
from chalk.importer import import_sql_file_resolvers

fraud_mysql = None
risk_sf = None
marketing_sf = None

try:
    import pymysql
    import snowflake

    from chalk.sql import MySQLSource, SnowflakeSource
    from chalk.sql._internal.sql_file_resolver import *

    fraud_mysql = MySQLSource(name="FRAUD_MYSQL")
    risk_sf = SnowflakeSource(name="RISK_SF")
    marketing_sf = SnowflakeSource(name="MARKETING_SF")
except ImportError:
    snowflake = None
    pymysql = None


@features
class Burrito:
    id: str
    name: str
    size: str


@features
class Meat:
    id: int
    name: str
    calories: float

    burrito_id: str
    burrito: Burrito = has_one(lambda: Burrito.id == Meat.burrito_id)


@pytest.mark.skipif(snowflake is None, reason="Snowflake is not installed")
def test_simple_sql_file_resolver():
    sources = [risk_sf]
    sql_string = """-- source: RISK_SF
        -- cron: 1h
        -- resolves: burrito
        select name, size from burritos_table where id = ${burrito.id}"""
    sql_string_result = SQLStringResult(path="sample_path", sql_string=sql_string, error=None)
    resolver_result = get_sql_file_resolver(sources, sql_string_result)
    assert not resolver_result.errors
    res = resolver_result.resolver
    assert res.function_definition == "select name, size from burritos_table where id = ${burrito.id}"
    assert res.inputs == [Burrito.id]
    assert res.output.__columns__ == (Burrito.name, Burrito.size)
    assert resolver_result.fields == {"name": "burrito.name", "size": "burrito.size"}
    assert resolver_result.args == {"__chalk_burrito_id__": "burrito.id"}
    assert (
        str(res.fn()._query)
        == """-- source: RISK_SF
        -- cron: 1h
        -- resolves: burrito
        select name, size from burritos_table where id = :__chalk_burrito_id__"""
    )


@pytest.mark.skipif(snowflake is None, reason="Snowflake is not installed")
def test_multiple_input_sql_file_resolver():
    sources = [risk_sf]
    sql_string = """-- source: RISK_SF
        -- cron: 1h
        -- resolves: burrito
        select name, size from burritos_table where id = ${burrito.id} and name=${burrito.name}"""
    sql_string_result = SQLStringResult(path="sample_path", sql_string=sql_string, error=None)
    resolver_result = get_sql_file_resolver(sources, sql_string_result)
    assert not resolver_result.errors
    res = resolver_result.resolver
    assert Burrito.id._chalk_feature in res.inputs and Burrito.name._chalk_feature in res.inputs
    assert res.output.__columns__ == (Burrito.name, Burrito.size)
    assert resolver_result.fields == {"name": "burrito.name", "size": "burrito.size"}
    assert resolver_result.args == {"__chalk_burrito_id__": "burrito.id", "__chalk_burrito_name__": "burrito.name"}
    assert res.default_args == [ResolverArgErrorHandler(None)] * 2


@pytest.mark.skipif(snowflake is None, reason="Snowflake is not installed")
def test_incremental_sql_file_resolver():
    sources = [risk_sf]
    sql_string = """-- source: RISK_SF
        -- cron: 1h
        -- resolves: burrito
        -- type: offline
        -- incremental:
        --    mode: parameter
        --    lookback_period: 60m
        select name, size from burritos_table where id = ${burrito.id}"""
    sql_string_result = SQLStringResult(path="sample_path", sql_string=sql_string, error=None)
    resolver_result = get_sql_file_resolver(sources, sql_string_result)
    assert not resolver_result.errors
    res = resolver_result.resolver
    assert res.inputs == [Burrito.id]
    assert res.output.__columns__ == (Burrito.name, Burrito.size)
    assert isinstance(res, OfflineResolver)
    assert res.fn().incremental_settings.mode == "parameter"
    assert str(res.fn().incremental_settings.lookback_period) == "1:00:00"
    assert resolver_result.fields == {"name": "burrito.name", "size": "burrito.size"}
    assert resolver_result.args == {"__chalk_burrito_id__": "burrito.id"}


@pytest.mark.skipif(snowflake is None, reason="Snowflake is not installed")
def test_no_sql_source():
    sources = [marketing_sf]
    sql_string = """-- source: RISK_SF
        -- cron: 1h
        -- resolves: burrito
        select name, size from burritos_table where id = ${burrito.id}"""
    sql_string_result = SQLStringResult(path="sample_path", sql_string=sql_string, error=None)
    resolver_result = get_sql_file_resolver(sources, sql_string_result)
    assert resolver_result.errors[0].display == "Source RISK_SF not found"


@pytest.mark.skipif(snowflake is None, reason="Snowflake is not installed")
def test_two_sql_sources():
    sources = [marketing_sf, risk_sf]
    sql_string = """-- source: snowflake
        -- cron: 1h
        -- resolves: burrito
        select name, size from burritos_table where id = ${burrito.id}"""
    sql_string_result = SQLStringResult(path="sample_path", sql_string=sql_string, error=None)
    resolver_result = get_sql_file_resolver(sources, sql_string_result)
    assert resolver_result.errors[0].display.startswith("More than one snowflake source exists")


@pytest.mark.skipif(snowflake is None, reason="Snowflake is not installed")
def test_comments_parsed():
    sources = [marketing_sf]
    sql_string = """-- Here is a normal comment
        -- source: snowflake
        -- cron: 1h
        -- resolves: burrito
        -- incremental:
        --    mode: parameter
        --    lookback_period: 60m
        -- tags:
        --    - one:1
        --    - two:2
        -- Here is another comment with a colon : in : it
        select name, size from burritos_table where id = ${burrito.id}"""
    sql_string_result = SQLStringResult(path="sample_path", sql_string=sql_string, error=None)
    resolver_result = get_sql_file_resolver(sources, sql_string_result)
    assert len(resolver_result.errors) == 0
    assert resolver_result.resolver.doc == "Here is a normal comment\nHere is another comment with a colon : in : it"
    assert resolver_result.resolver.tags == ["one:1", "two:2"]


@pytest.mark.skipif(snowflake is None, reason="Snowflake is not installed")
def test_single_tag_parse():
    sources = [marketing_sf]
    sql_string = """-- Here is a normal comment
        -- source: snowflake
        -- cron: 1h
        -- resolves: burrito
        -- incremental:
        --    mode: parameter
        --    lookback_period: 60m
        -- tags: singletag
        -- Here is another comment with a colon : in : it
        select name, size from burritos_table where id = ${burrito.id}"""
    sql_string_result = SQLStringResult(path="sample_path", sql_string=sql_string, error=None)
    resolver_result = get_sql_file_resolver(sources, sql_string_result)
    assert len(resolver_result.errors) == 0
    assert resolver_result.resolver.tags == ["singletag"]


@pytest.mark.skipif(snowflake is None, reason="Snowflake is not installed")
def test_single_tag_malformed_parse():
    sources = [marketing_sf]
    sql_string = """-- Here is a normal comment
        -- source: snowflake
        -- cron: 1h
        -- resolves: burrito
        -- incremental:
        --    mode: parameter
        --    lookback_period: 60m
        -- tags:
        --    one: 1
        --    two: 2
        -- Here is another comment with a colon : in : it
        select name, size from burritos_table where id = ${burrito.id}"""
    sql_string_result = SQLStringResult(path="sample_path", sql_string=sql_string, error=None)
    resolver_result = get_sql_file_resolver(sources, sql_string_result)
    assert len(resolver_result.errors) == 1
    assert resolver_result.errors[0].display == "Parameter 'tags' value {'one': 1, 'two': 2} should be a list"


@pytest.mark.skipif(snowflake is None, reason="Snowflake is not installed")
def test_malformed_sql_query():
    sources = [marketing_sf, risk_sf]
    sql_string = """-- source: bigquery
        -- cron: 1h
        -- resolves: burrito
        -- bad comment
        -- another bad comment
        select name, size from burritos_table whereASDFW id = ${burrito.id}"""
    sql_string_result = SQLStringResult(path="sample_path", sql_string=sql_string, error=None)
    resolver_result = get_sql_file_resolver(sources, sql_string_result)
    assert len(resolver_result.errors) == 1
    assert resolver_result.errors[0].display.startswith("Cannot SQL parse")


@pytest.mark.skipif(snowflake is None, reason="Snowflake is not installed")
def test_missing_required_source():
    sources = [marketing_sf, risk_sf]
    sql_string = """-- missing: required_comment
        -- cron: 1h
        -- resolves: burrito
        select name, size from burritos_table where id = ${burrito.id}"""
    sql_string_result = SQLStringResult(path="sample_path", sql_string=sql_string, error=None)
    resolver_result = get_sql_file_resolver(sources, sql_string_result)
    assert (
        resolver_result.errors[0].display == "Missing value for 'source'. Please specify via "
        "source type in ['snowflake', 'postgres', 'postgresql', 'mysql', "
        "'bigquery', 'cloudsql', 'redshift', 'sqlite'], or via source name in "
        "['MARKETING_SF', 'RISK_SF']"
    )


@pytest.mark.skipif(snowflake is None, reason="Snowflake is not installed")
def test_missing_required_resolves():
    sources = [marketing_sf]
    sql_string = """-- missing: required_comment
        -- source: MARKETING_SF
        -- cron: 1h
        select name, size from burritos_table where id = ${burrito.id}"""
    sql_string_result = SQLStringResult(path="sample_path", sql_string=sql_string, error=None)
    resolver_result = get_sql_file_resolver(sources, sql_string_result)
    assert resolver_result.errors[0].display.startswith("Key 'resolves' must be described in comments.")


@pytest.mark.skipif(snowflake is None, reason="Snowflake is not installed")
def test_default_variable_sql_resolver():
    sources = [risk_sf]
    sql_string1 = """-- source: RISK_SF
        -- cron: 1h
        -- resolves: burrito
        select b_name as name, b_size as size
        from burritos_table where id = ${burrito.id | "b_1"}"""
    sql_string2 = """-- source: RISK_SF
        -- cron: 1h
        -- resolves: burrito
        select b_name as name, b_size as size
        from burritos_table where id = ${burrito.id or "b_1"}"""
    sql_string_result1 = SQLStringResult(path="sample_path", sql_string=sql_string1, error=None)
    sql_string_result2 = SQLStringResult(path="sample_path", sql_string=sql_string2, error=None)
    resolver_result = get_sql_file_resolver(sources, sql_string_result1)
    resolver_result2 = get_sql_file_resolver(sources, sql_string_result2)
    assert resolver_result == resolver_result2
    assert not resolver_result.errors
    res = resolver_result.resolver
    assert res.inputs == [Burrito.id]
    assert res.output.__columns__ == (Burrito.name, Burrito.size)
    assert res.default_args == [ResolverArgErrorHandler("b_1")]
    assert resolver_result.fields == {"name": "burrito.name", "size": "burrito.size"}
    assert resolver_result.args == {"__chalk_burrito_id__": "burrito.id"}
    assert (
        str(res.fn()._query)
        == """-- source: RISK_SF
        -- cron: 1h
        -- resolves: burrito
        select b_name as name, b_size as size
        from burritos_table where id = :__chalk_burrito_id__"""
    )


@pytest.mark.skipif(snowflake is None, reason="Snowflake is not installed")
def test_default_variable_sql_resolver_int():
    sources = [risk_sf]
    sql_string = """-- source: RISK_SF
        -- cron: 1h
        -- resolves: meat
        select id, name
        from meat_table where id = ${meat.id | 2}"""

    sql_string_result = SQLStringResult(path="sample_path", sql_string=sql_string, error=None)
    resolver_result = get_sql_file_resolver(sources, sql_string_result)
    assert not resolver_result.errors
    res = resolver_result.resolver
    assert res.inputs == [Meat.id]
    assert res.output.__columns__ == (Meat.id, Meat.name)
    assert res.default_args == [ResolverArgErrorHandler(2)]
    assert (
        str(res.fn()._query)
        == """-- source: RISK_SF
        -- cron: 1h
        -- resolves: meat
        select id, name
        from meat_table where id = :__chalk_meat_id__"""
    )


@pytest.mark.skipif(snowflake is None, reason="Snowflake is not installed")
def test_default_variable_sql_resolver_float():
    sources = [risk_sf]
    sql_string = """-- source: RISK_SF
        -- cron: 1h
        -- resolves: meat
        select id, name
        from meat_table where calories = ${meat.calories | 2.2}"""

    sql_string_result = SQLStringResult(path="sample_path", sql_string=sql_string, error=None)
    resolver_result = get_sql_file_resolver(sources, sql_string_result)
    assert not resolver_result.errors
    res = resolver_result.resolver
    assert res.inputs == [Meat.calories]
    assert res.output.__columns__ == (Meat.id, Meat.name)
    assert res.default_args == [ResolverArgErrorHandler(2.2)]


@pytest.mark.skipif(snowflake is None, reason="Snowflake is not installed")
def test_malformed_default_variable_sql_resolver():
    sources = [risk_sf]
    sql_string1 = """-- source: RISK_SF
        -- cron: 1h
        -- resolves: burrito
        select b_name as name, b_size as size
        from burritos_table where id = ${burrito.id | burrito.size | burrito.value}"""
    sql_string_result1 = SQLStringResult(path="sample_path", sql_string=sql_string1, error=None)
    resolver_result = get_sql_file_resolver(sources, sql_string_result1)
    assert resolver_result.errors[0].display.startswith("If character '|' is used, both variable name")


@pytest.mark.skipif(snowflake is None, reason="Snowflake is not installed")
def test_as_sql_resolver():
    sources = [risk_sf]
    sql_string = """-- source: RISK_SF
        -- cron: 1h
        -- resolves: burrito
        select b_name as name, b_size as size
        from burritos_table where id = ${burrito.id}"""
    sql_string_result = SQLStringResult(path="sample_path", sql_string=sql_string, error=None)
    resolver_result = get_sql_file_resolver(sources, sql_string_result)
    assert not resolver_result.errors
    res = resolver_result.resolver
    assert res.inputs == [Burrito.id]
    assert res.output.__columns__ == (Burrito.name, Burrito.size)
    assert resolver_result.fields == {"name": "burrito.name", "size": "burrito.size"}
    assert resolver_result.args == {"__chalk_burrito_id__": "burrito.id"}


@pytest.mark.skipif(snowflake is None, reason="Snowflake is not installed")
def test_sql_resolver_with_table_names():
    sources = [risk_sf]
    sql_string = """-- source: RISK_SF
        -- cron: 1h
        -- resolves: burrito
        select burritos_table.name, burritos_table.size
        from burritos_table where id = ${burrito.id}"""
    sql_string_result = SQLStringResult(path="sample_path", sql_string=sql_string, error=None)
    resolver_result = get_sql_file_resolver(sources, sql_string_result)
    assert not resolver_result.errors
    res = resolver_result.resolver
    assert res.inputs == [Burrito.id]
    assert res.output.__columns__ == (Burrito.name, Burrito.size)
    assert resolver_result.fields == {"name": "burrito.name", "size": "burrito.size"}
    assert resolver_result.args == {"__chalk_burrito_id__": "burrito.id"}


@pytest.mark.skipif(snowflake is None, reason="Snowflake is not installed")
def test_as_sql_resolver_with_table_names():
    sources = [risk_sf]
    sql_string = """-- source: RISK_SF
        -- cron: 1h
        -- resolves: burrito
        select burritos_table.name as name, burritos_table.size as size
        from burritos_table where id = ${burrito.id}"""
    sql_string_result = SQLStringResult(path="sample_path", sql_string=sql_string, error=None)
    resolver_result = get_sql_file_resolver(sources, sql_string_result)
    assert not resolver_result.errors
    res = resolver_result.resolver
    assert res.inputs == [Burrito.id]
    assert res.output.__columns__ == (Burrito.name, Burrito.size)
    assert resolver_result.fields == {"name": "burrito.name", "size": "burrito.size"}
    assert resolver_result.args == {"__chalk_burrito_id__": "burrito.id"}


@pytest.mark.skipif(snowflake is None, reason="Snowflake is not installed")
def test_one_sql_file_resolver():
    sources = [risk_sf]
    sql_string = """-- source: RISK_SF
        -- cron: 1h
        -- count: one
        -- resolves: burrito
        select name, size from burritos_table where id = ${burrito.id}"""
    sql_string_result = SQLStringResult(path="sample_path", sql_string=sql_string, error=None)
    resolver_result = get_sql_file_resolver(sources, sql_string_result)
    assert not resolver_result.errors
    res = resolver_result.resolver
    assert res.function_definition == "select name, size from burritos_table where id = ${burrito.id}"
    assert res.inputs == [Burrito.id]
    assert res.output.features == (Burrito.name, Burrito.size)
    assert resolver_result.fields == {"name": "burrito.name", "size": "burrito.size"}
    assert resolver_result.args == {"__chalk_burrito_id__": "burrito.id"}
    assert res.fn().finalizer == "OneOrNone"


@pytest.mark.skipif(snowflake is None, reason="Snowflake is not installed")
def test_sql_join_hop():
    sources = [risk_sf]
    sql_string = """-- source: RISK_SF
        -- cron: 1h
        -- resolves: burrito
        SELECT burritos_table.id AS id,
        burritos_table.name AS name,
        burritos_table.size AS size,
        FROM burritos_table JOIN meat_table ON burritos_table.id = meat_table.burrito_id
        WHERE meat_table.id = ${meat.id}"""
    # in this case, 'id = ${}' wouldn't work! Be careful!
    sql_string_result = SQLStringResult(path="sample_path", sql_string=sql_string, error=None)
    resolver_result = get_sql_file_resolver(sources, sql_string_result)
    assert not resolver_result.errors
    res = resolver_result.resolver
    assert res.inputs == [Meat.id]
    assert res.output.__columns__ == (Burrito.id, Burrito.name, Burrito.size)
    assert resolver_result.fields == {"id": "burrito.id", "name": "burrito.name", "size": "burrito.size"}
    assert resolver_result.args == {"__chalk_meat_id__": "meat.id"}


@pytest.mark.skipif(snowflake is None, reason="Snowflake is not installed")
def test_sql_join_stay():
    sources = [risk_sf]
    sql_string = """-- source: RISK_SF
        -- cron: 1h
        -- resolves: meat
        SELECT meat_table.name AS name, meat_table.id as id
        FROM burritos_table JOIN meat_table ON burritos_table.id = meat_table.burrito_id
        WHERE meat_table.id = ${meat.id}"""
    # in this case, 'id = ${}' wouldn't work! Be careful!
    sql_string_result = SQLStringResult(path="sample_path", sql_string=sql_string, error=None)
    resolver_result = get_sql_file_resolver(sources, sql_string_result)
    assert not resolver_result.errors
    res = resolver_result.resolver
    assert res.inputs == [Meat.id]
    assert res.output.__columns__ == (Meat.name, Meat.id)
    assert resolver_result.fields == {"name": "meat.name", "id": "meat.id"}
    assert resolver_result.args == {"__chalk_meat_id__": "meat.id"}
