from time import time
from typing import Callable, Dict

import pytest
from pytest_httpx import HTTPXMock

from tests.settings import Settings


@pytest.fixture(scope='module')
async def client(settings: Settings):
    async with BaseHTTP(
            endpoint=settings.BYBIT_ENDPOINT,
            api_key=settings.BYBIT_API_KEY,
            api_secret=settings.BYBIT_API_SECRET,
    ) as client:
        yield client


@pytest.fixture(scope='module')
async def client_no_auth(settings: Settings):
    async with BaseHTTP(endpoint=settings.BYBIT_ENDPOINT) as client:
        yield client


@pytest.fixture
def add_httpx_response(httpx_mock: HTTPXMock) -> Callable:
    def add_response(
            result: Dict,
            *args,
            ret_code: int = 0,
            ret_msg: str = '',
            **kwargs
    ):
        data = ResponseData(
            ret_code=ret_code,
            ret_msg=ret_msg,
            result=result,
            time=int(time()),
        )
        kwargs['json'] = data.dict(
            exclude_none=True,
            by_alias=True,
        )
        httpx_mock.add_response(*args, **kwargs)

    return add_response
