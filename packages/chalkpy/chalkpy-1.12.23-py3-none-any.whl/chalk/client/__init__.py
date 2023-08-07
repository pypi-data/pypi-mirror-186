from typing import Optional

from chalk.client.client_impl import ChalkAPIClientImpl
from chalk.client.client_protocol import ChalkAPIClientProtocol, OnlineQueryResponseProtocol
from chalk.client.exc import (
    ChalkBaseException,
    ChalkDatasetDownloadException,
    ChalkOfflineQueryException,
    ChalkResolverRunException,
)
from chalk.client.models import (
    ChalkError,
    ChalkException,
    ErrorCode,
    ErrorCodeCategory,
    FeatureResult,
    OfflineQueryContext,
    OnlineQueryContext,
    OnlineQueryResponse,
    ResolverRunResponse,
    WhoAmIResponse,
)

__all__ = [
    "ChalkError",
    "ChalkResolverRunException",
    "ChalkDatasetDownloadException",
    "ChalkOfflineQueryException",
    "FeatureResult",
    "WhoAmIResponse",
    "OnlineQueryResponse",
    "OnlineQueryResponseProtocol",
    "ChalkBaseException",
    "ChalkAPIClientProtocol",
    "OnlineQueryContext",
    "OfflineQueryContext",
    "ResolverRunResponse",
    "ErrorCode",
    "ErrorCodeCategory",
    "ChalkException",
    "ChalkClient",
]


def ChalkClient(
    *,
    client_id: Optional[str] = None,
    client_secret: Optional[str] = None,
    environment: Optional[str] = None,
    api_server: Optional[str] = None,
) -> ChalkAPIClientProtocol:
    return ChalkAPIClientImpl(
        client_id=client_id,
        client_secret=client_secret,
        environment=environment,
        api_server=api_server,
    )
