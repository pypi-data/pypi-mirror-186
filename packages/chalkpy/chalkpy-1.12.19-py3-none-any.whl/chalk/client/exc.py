from typing import List

from chalk.client.models import ChalkError


class ChalkBaseException(Exception):
    ...


class ChalkOfflineQueryException(ChalkBaseException):
    message: str
    errors: List[ChalkError]

    def __init__(self, message: str, errors: List[ChalkError]):
        self.message = message
        self.errors = errors
        super().__init__(message + "\n" + "\n".join(["\t" + e.message for e in errors[0:3]]))


class ChalkResolverRunException(ChalkBaseException):
    message: str

    def __init__(self, message: str):
        self.message = message
        super().__init__(message)


class ChalkDatasetDownloadException(ChalkBaseException):
    message: str

    def __init__(self, message: str):
        self.message = message
        super().__init__(message)


__all__ = [
    "ChalkBaseException",
    "ChalkOfflineQueryException",
    "ChalkResolverRunException",
    "ChalkDatasetDownloadException",
]
