import json

import pytest

from chalk.client.models import ChalkError, ErrorCode, ErrorCodeCategory, OnlineQueryResponse


@pytest.mark.parametrize("code", list(ErrorCode))
def test_create_chalk_error(code: ErrorCode):
    assert isinstance(ErrorCode.category(code), ErrorCodeCategory)
    error = ChalkError(code=code, message="")
    assert error.category == ErrorCode.category(error.code)
    assert error.dict()["category"] == ErrorCode.category(error.code)


def test_chalk_error_serialization():
    x = ChalkError(code=ErrorCode.RESOLVER_FAILED, message="Test error")
    x_jsoned = x.json()
    x_dict = json.loads(x_jsoned)
    del x_dict["category"]
    x_parsed = ChalkError(**x_dict)
    assert x == x_parsed
