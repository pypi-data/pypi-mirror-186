from typing import Callable

import pytest
from pytest_httpx import HTTPXMock

from exapi.bitget.v1.client import BaseClient
from exapi.bitget.v1.models import ResponseData
from tests.settings import Settings


@pytest.fixture(scope='module')
async def bitget_base(settings: Settings):
    async with BaseClient(
            api_key=settings.BITGET_API_KEY,
            api_secret=settings.BITGET_API_SECRET,
            api_passphrase=settings.BITGET_API_PASSPHRASE,
    ) as client:
        yield client


@pytest.fixture(scope='module')
async def bitget_base_no_auth(settings: Settings):
    async with BaseClient() as client:
        yield client


@pytest.fixture
def set_bitget_request_result(monkeypatch) -> Callable[[list | dict | str | int | None], None]:
    def set_request_result(result: list | dict | str | int | None):
        async def mock_request(*args, **kwargs) -> list | dict | str | int | None:
            return result

        monkeypatch.setattr(BaseClient, 'request', mock_request)

    return set_request_result


@pytest.fixture
def add_httpx_bitget_response(httpx_mock: HTTPXMock) -> Callable:
    def add_response(
            data: list | dict | str | int | None,
            *args,
            code: int = 0,
            msg: str = '',
            **kwargs
    ):
        result = ResponseData(
            code=code,
            msg=msg,
            data=data,
        )
        kwargs['json'] = result.dict(
            exclude_none=True,
            by_alias=True,
        )
        httpx_mock.add_response(*args, **kwargs)

    return add_response
