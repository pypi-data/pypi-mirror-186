from typing import Callable

import pytest
from httpx import ReadTimeout
from pytest_httpx import HTTPXMock

from exapi.bitget.exceptions import BitgetException
from exapi.bitget.v1.client import BaseClient


@pytest.mark.anyio
async def test_client_request_auth_exc(
        bitget_base_no_auth: BaseClient,
):
    with pytest.raises(BitgetException) as exc_info:
        await bitget_base_no_auth.request(
            method='GET',
            url='/test_client_request_auth_exc',
            auth=True,
        )

    assert exc_info.type is BitgetException


@pytest.mark.anyio
async def test_client_request_timeout(
        httpx_mock: HTTPXMock,
        bitget_base: BaseClient,
):
    httpx_mock.add_exception(ReadTimeout('Unable to read within timeout'))

    with pytest.raises(BitgetException) as exc_info:
        await bitget_base.request(method='GET', url='/test_client_request_error')

    assert exc_info.type is BitgetException


@pytest.mark.anyio
async def test_client_request_invalid_json(
        httpx_mock: HTTPXMock,
        bitget_base: BaseClient,
):
    httpx_mock.add_response(content=b'Invalid JSON body')

    with pytest.raises(BitgetException) as exc_info:
        await bitget_base.request(method='GET', url='/test_client_request_invalid_json')

    assert exc_info.type is BitgetException


@pytest.mark.anyio
@pytest.mark.parametrize('status_code', [101, 308, 400, 500])
async def test_client_request_status(
        httpx_mock: HTTPXMock,
        bitget_base: BaseClient,
        status_code: int,
):
    httpx_mock.add_response(status_code=status_code)

    with pytest.raises(BitgetException) as exc_info:
        await bitget_base.request(method='PUT', url='/test_client_request_status')

    assert exc_info.type is BitgetException
    assert exc_info.value.response.status_code == status_code


@pytest.mark.anyio
async def test_client_request_params_bugfix(
        add_httpx_bitget_response: Callable,
        httpx_mock: HTTPXMock,
        bitget_base: BaseClient,
):
    add_httpx_bitget_response(
        data={'request': 'ok'},
    )

    await bitget_base.request(
        method='GET',
        url='/test_client_request_params_bugfix',
        params={'test': 3.0}
    )

    request = httpx_mock.get_request()
    fixed_value = request.url.params.get('test')

    assert fixed_value == '3'


@pytest.mark.anyio
@pytest.mark.parametrize(
    'data',
    [
        [],
        '',
        'test',
        {
            'some': 'data',
        },
    ],
)
async def test_client_request_response_fail_validation(
        httpx_mock: HTTPXMock,
        bitget_base: BaseClient,
        data: dict,
):
    httpx_mock.add_response(json=data)

    with pytest.raises(BitgetException) as exc_info:
        await bitget_base.request(
            method='GET',
            url='/test_client_request_response_fail_validation',
        )

    assert exc_info.type is BitgetException


@pytest.mark.anyio
@pytest.mark.parametrize(
    'data',
    [
        {'retCode': 33004, 'retMsg': 'Your api key has expired.', 'result': {}, 'time': 123},
        {'retCode': 10003, 'retMsg': 'You are not authorized to execute this request.', 'result': {}, 'time': 123},
    ],
)
async def test_client_request_response_with_error(
        httpx_mock: HTTPXMock,
        bitget_base: BaseClient,
        data: dict,
):
    httpx_mock.add_response(json=data)

    with pytest.raises(BitgetException) as exc_info:
        await bitget_base.request(
            method='GET',
            url='/test_client_request_response_with_error',
        )

    assert exc_info.type is BitgetException


@pytest.mark.anyio
async def test_client_request_response_with_ignore_codes(
        httpx_mock: HTTPXMock,
        bitget_base: BaseClient,
        monkeypatch,
):
    monkeypatch.setattr(bitget_base, 'ignore_codes', {33000})
    httpx_mock.add_response(
        json={
            'code': 33000,
            'msg': 'Error message',
        },
    )

    await bitget_base.request(
        method='GET',
        url='/test_client_request_response_with_ignore_codes',
    )

    assert True


@pytest.mark.anyio
async def test_client_request(
        add_httpx_bitget_response,
        bitget_base: BaseClient,
):
    add_httpx_bitget_response(
        data={'request': 'ok'},
    )
    data = await bitget_base.request(method='GET', url='/test_client_request')
    assert data == {'request': 'ok'}


@pytest.mark.anyio
async def test_client_get(
        add_httpx_bitget_response,
        bitget_base: BaseClient,
):
    add_httpx_bitget_response(
        method='GET',
        data={'get': 'ok'},
    )
    data = await bitget_base.get('/test_client_get')
    assert data == {'get': 'ok'}


@pytest.mark.anyio
async def test_client_post(
        add_httpx_bitget_response,
        bitget_base: BaseClient,
):
    add_httpx_bitget_response(
        method='POST',
        data={'post': 'ok'},
    )
    data = await bitget_base.post('/test_client_post')
    assert data == {'post': 'ok'}
