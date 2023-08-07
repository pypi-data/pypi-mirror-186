from __future__ import annotations

import uuid
from datetime import datetime
from enum import Enum
from typing import Any, Dict, List, Mapping, Optional, Union

import numpy as np
from pydantic import BaseModel, Field, root_validator


class OnlineQueryContext(BaseModel):
    # The environment under which to run the resolvers.
    # API tokens can be scoped to an # environment.
    # If no environment is specified in the query,
    # but the token supports only a single environment,
    # then that environment will be taken as the scope
    # for executing the request.
    environment: Optional[str] = None

    # The tags used to scope the resolvers.
    # More information at https://docs.chalk.ai/docs/resolver-tags
    tags: Optional[List[str]] = None


class OfflineQueryContext(BaseModel):
    # The environment under which to run the resolvers.
    # API tokens can be scoped to an # environment.
    # If no environment is specified in the query,
    # but the token supports only a single environment,
    # then that environment will be taken as the scope
    # for executing the request.
    environment: Optional[str] = None


class ErrorCode(str, Enum):
    # The query contained features that do not exist.
    PARSE_FAILED = "PARSE_FAILED"

    # A resolver was required as part of running the dependency
    # graph that could not be found.
    RESOLVER_NOT_FOUND = "RESOLVER_NOT_FOUND"

    # The query is invalid. All supplied features need to be
    # rooted in the same top-level entity.
    INVALID_QUERY = "INVALID_QUERY"

    # A feature value did not match the expected schema
    # (eg. `incompatible type "int"; expected "str"`)
    VALIDATION_FAILED = "VALIDATION_FAILED"

    # The resolver for a feature errored.
    RESOLVER_FAILED = "RESOLVER_FAILED"

    # A crash in a resolver that was to produce an input for
    # the resolver crashed, and so the resolver could not run
    # crashed, and so the resolver could not run.
    UPSTREAM_FAILED = "UPSTREAM_FAILED"

    # The request was submitted with an invalid authentication header.
    UNAUTHENTICATED = "UNAUTHENTICATED"

    # An unspecified error occurred.
    INTERNAL_SERVER_ERROR = "INTERNAL_SERVER_ERROR"

    @classmethod
    def category(cls, c: Union[ErrorCode, str]) -> ErrorCodeCategory:
        c = ErrorCode[c]
        return {
            cls.PARSE_FAILED: ErrorCodeCategory.REQUEST,
            cls.RESOLVER_NOT_FOUND: ErrorCodeCategory.REQUEST,
            cls.INVALID_QUERY: ErrorCodeCategory.REQUEST,
            cls.VALIDATION_FAILED: ErrorCodeCategory.FIELD,
            cls.RESOLVER_FAILED: ErrorCodeCategory.FIELD,
            cls.UPSTREAM_FAILED: ErrorCodeCategory.FIELD,
            cls.UNAUTHENTICATED: ErrorCodeCategory.NETWORK,
            cls.INTERNAL_SERVER_ERROR: ErrorCodeCategory.NETWORK,
        }[c]


class ErrorCodeCategory(str, Enum):

    # Request errors are raised before execution of your
    # resolver code. They may occur due to invalid feature
    # names in the input or a request that cannot be satisfied
    # by the resolvers you have defined.
    REQUEST = "REQUEST"

    # Field errors are raised while running a feature resolver
    # for a particular field. For this type of error, you’ll
    # find a feature and resolver attribute in the error type.
    # When a feature resolver crashes, you will receive null
    # value in the response. To differentiate from a resolver
    # returning a null value and a failure in the resolver,
    # you need to check the error schema.
    FIELD = "FIELD"

    # Network errors are thrown outside your resolvers.
    # For example, your request was unauthenticated,
    # connection failed, or an error occurred within Chalk.
    NETWORK = "NETWORK"


class ChalkException(BaseModel):
    # The name of the class of the exception.
    kind: str

    # The message taken from the exception.
    message: str

    # The stacktrace produced by the code.
    stacktrace: str

    class Config:
        frozen = True


class ChalkError(BaseModel):
    # The type of the error
    code: ErrorCode

    # The category of the error, given in the type field for the error codes.
    # This will be one of "REQUEST", "NETWORK", and "FIELD".
    category: ErrorCodeCategory = ErrorCodeCategory.NETWORK

    # A readable description of the error message.
    message: str

    # The exception that caused the failure, if applicable.
    exception: Optional[ChalkException] = None

    # The fully qualified name of the failing feature, eg.user.identity.has_voip_phone.
    feature: Optional[str] = None

    # The fully qualified name of the failing resolver, eg.my.project.get_fraud_score.
    resolver: Optional[str] = None

    class Config:
        frozen = True

    def copy_for_feature(self, feature: str) -> "ChalkError":
        return self.copy(update={"feature": feature})

    @root_validator
    def validate_category(cls, values: Dict[str, Any]):
        values["category"] = ErrorCode.category(values["code"])
        return values


class ResolverRunStatus(str, Enum):
    RECEIVED = "received"
    SUCCEEDED = "succeeded"
    FAILED = "failed"


class ResolverRunResponse(BaseModel):
    id: str
    status: ResolverRunStatus


class WhoAmIResponse(BaseModel):
    user: str


class FeatureResolutionMeta(BaseModel):
    chosen_resolver_fqn: str
    cache_hit: bool

    class Config:
        frozen = True


class FeatureResult(BaseModel):
    # The name of the feature requested, eg.user.identity.has_voip_phone.
    field: str

    # The value of the requested feature.
    # If an error was encountered in resolving this feature,
    # this field will be empty.
    value: Any

    pkey: Any

    # The error code encountered in resolving this feature.
    # If no error occurred, this field is empty.
    error: Optional[ChalkError] = None

    # The time at which this feature was computed.
    # This value could be significantly in the past if you're using caching.
    ts: Optional[datetime] = None

    meta: Optional[FeatureResolutionMeta] = None


class ExchangeCredentialsRequest(BaseModel):
    client_id: str
    client_secret: str
    grant_type: str


class ExchangeCredentialsResponse(BaseModel):
    access_token: str
    token_type: str
    expires_in: int
    # expires_at: datetime
    api_server: str
    primary_environment: Optional[str] = None
    engines: Optional[Mapping[str, str]] = None


class OfflineQueryInput(BaseModel):
    columns: List[str]
    values: List[List[Any]]


class OnlineQueryRequest(BaseModel):
    inputs: Mapping[str, Any]
    outputs: List[str]
    staleness: Optional[Mapping[str, str]] = None
    context: Optional[OnlineQueryContext] = None
    include_meta: bool = False
    skip_online_storage: Optional[bool] = False
    skip_offline_storage: Optional[bool] = False
    skip_metrics_storage: Optional[bool] = False
    skip_cache_lookups: Optional[bool] = False
    correlation_id: Optional[str] = None
    query_name: Optional[str] = None
    deployment_id: Optional[str] = None
    meta: Optional[Mapping[str, str]] = None


class TriggerResolverRunRequest(BaseModel):
    resolver_fqn: str


class QueryMeta(BaseModel):
    execution_duration_s: float
    deployment_id: Optional[str] = None
    query_id: Optional[str] = None


class OnlineQueryResponse(BaseModel):
    data: List[FeatureResult]
    errors: Optional[List[ChalkError]] = None
    meta: Optional[QueryMeta] = None

    def for_fqn(self, fqn: str):
        return next((x for x in self.data if x.field == fqn), None)

    class Config:
        json_encoders = {
            np.integer: int,
            np.floating: float,
        }


class CreateOfflineQueryJobRequest(BaseModel):
    output: List[str] = Field(description="A list of output feature root fqns to query")
    required_output: List[str] = Field(default_factory=list, description="A list of required output feature root fqns")
    destination_format: str = Field(description="The desired output format. Should be 'CSV' or 'PARQUET'")
    job_id: Optional[uuid.UUID] = Field(
        default=None,
        description=(
            "A unique job id. If not specified, one will be auto generated by the server. If specified by the client, "
            "then jobs with the same ID will be rejected."
        ),
    )
    input: Optional[OfflineQueryInput] = Field(default=None, description="Any givens")
    max_samples: Optional[int] = Field(
        default=None,
        description="The maximum number of samples. If None, no limit",
    )
    max_cache_age_secs: Optional[int] = Field(
        default=None,  # Defaults to ``OFFLINE_QUERY_MAX_CACHE_AGE_SECS`` in the chalkengine config
        description=(
            "The maximum staleness, in seconds, for how old the view on the offline store can be. That is, "
            "data ingested within this interval will not be reflected in this offline query. "
            "Set to ``0`` to ignore the cache. If not specified, it defaults to 30 minutes."
        ),
    )
    observed_at_lower_bound: Optional[datetime] = Field(
        default=None,
        description="The lower bound for the observed at timestamp (inclusive). If not specified, defaults to the beginning of time",
    )
    observed_at_upper_bound: Optional[datetime] = Field(
        default=None,
        description="The upper bound for the observed at timestamp (inclusive). If not specified, defaults to the end of time.",
    )
    dataset_name: Optional[str] = None
    branch: Optional[str] = None


# FIXME document
class ComputeResolverOutputRequest(BaseModel):
    input: OfflineQueryInput
    resolver_fqn: str
    branch: Optional[str] = None
    environment: Optional[str] = None


class RecomputeResolverOutputRequest(BaseModel):
    persistent_id: str
    resolver_fqn: str
    branch: Optional[str] = None
    environment: Optional[str] = None


class ComputeResolverOutputResponse(BaseModel):
    job_id: str
    persistent_id: str
    errors: Optional[List[ChalkError]] = None


class OfflineQueryRequest(BaseModel):
    """V1 OfflineQueryRequest. Not used by the current Chalk Client."""

    output: List[str]  # output features which can be null
    input: Optional[OfflineQueryInput] = None
    dataset: Optional[str] = None
    max_samples: Optional[int] = None
    max_cache_age_secs: Optional[int] = None
    required_outputs: List[str] = Field(default_factory=list)  # output features which cannot be null


class OfflineQueryResponse(BaseModel):
    """V1 OfflineQueryResponse. Not used by the current Chalk Client."""

    columns: List[str]
    output: List[List[Any]]
    errors: Optional[List[ChalkError]] = None


class CreateOfflineQueryJobResponse(BaseModel):
    """
    Attributes:
        job_id: A job ID, which can be used to retrieve the results.
    """

    job_id: uuid.UUID
    version: int = 1  # Field is deprecated
    errors: Optional[List[ChalkError]] = None


class GetOfflineQueryJobResponse(BaseModel):
    is_finished: bool = Field(description="Whether the export job is finished (it runs asynchronously)")
    version: int = Field(
        default=1,  # Backwards compatibility
        description=(
            "Version number representing the format of the data. The client uses this version number "
            "to properly decode and load the query results into DataFrames."
        ),
    )
    urls: List[str] = Field(
        description="A list of short-lived, authenticated URLs that the client can download to retrieve the exported data."
    )
    errors: Optional[List[ChalkError]] = None
