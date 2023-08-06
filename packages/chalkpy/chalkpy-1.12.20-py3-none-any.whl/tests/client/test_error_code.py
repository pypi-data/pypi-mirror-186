import pytest

from chalk.client.models import ChalkError, ErrorCode, ErrorCodeCategory


@pytest.mark.parametrize("code", list(ErrorCode))
def test_create_chalk_error(code: ErrorCode):
    assert isinstance(ErrorCode.category(code), ErrorCodeCategory)
    error = ChalkError(code=code, message="")
    assert error.category == ErrorCode.category(error.code)
    assert error.dict()["category"] == ErrorCode.category(error.code)
