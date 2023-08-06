from typing import Callable

import pytest
from httpx import HTTPError, HTTPStatusError, ReadTimeout, RequestError
from pytest_httpx import HTTPXMock

from exapi.bybit.v3 import BaseHTTP


@pytest.mark.anyio
async def test_client_request_auth_runtime(
        client_no_auth: BaseHTTP,
):
    with pytest.raises(RuntimeError) as exc_info:
        await client_no_auth.request(
            method='GET',
            url='/test_client_request_auth_runtime',
            auth=True,
        )

    assert exc_info.type is RuntimeError


@pytest.mark.anyio
async def test_client_request_timeout(
        httpx_mock: HTTPXMock,
        client: BaseHTTP,
):
    httpx_mock.add_exception(ReadTimeout('Unable to read within timeout'))

    with pytest.raises(ReadTimeout) as exc_info:
        await client.request(method='GET', url='/test_client_request_error')

    assert exc_info.type is ReadTimeout
    assert isinstance(exc_info.value, RequestError)


@pytest.mark.anyio
async def test_client_request_invalid_json(
        httpx_mock: HTTPXMock,
        client: BaseHTTP,
):
    httpx_mock.add_response(content=b'Invalid JSON body')

    with pytest.raises(HTTPError) as exc_info:
        await client.request(method='GET', url='/test_client_request_invalid_json')

    assert exc_info.type is HTTPError


@pytest.mark.anyio
@pytest.mark.parametrize('status_code', [101, 308, 400, 500])
async def test_client_request_status(
        httpx_mock: HTTPXMock,
        client: BaseHTTP,
        status_code: int,
):
    httpx_mock.add_response(status_code=status_code)

    with pytest.raises(HTTPStatusError) as exc_info:
        await client.request(method='PUT', url='/test_client_request_status')

    assert exc_info.type is HTTPStatusError
    assert exc_info.value.response.status_code == status_code


@pytest.mark.anyio
async def test_client_request_params_bugfix(
        add_httpx_response: Callable,
        httpx_mock: HTTPXMock,
        client: BaseHTTP,
):
    add_httpx_response(
        result={'request': 'ok'},
    )

    await client.request(
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
        client: BaseHTTP,
        data: dict,
):
    httpx_mock.add_response(json=data)

    with pytest.raises(HTTPError) as exc_info:
        await client.request(
            method='GET',
            url='/test_client_request_response_fail_validation',
        )

    assert exc_info.type is HTTPError


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
        client: BaseHTTP,
        data: dict,
):
    httpx_mock.add_response(json=data)

    with pytest.raises(HTTPError) as exc_info:
        await client.request(
            method='GET',
            url='/test_client_request_response_with_error',
        )

    assert exc_info.type is HTTPError


@pytest.mark.anyio
async def test_client_request_response_with_ignore_codes(
        httpx_mock: HTTPXMock,
        client: BaseHTTP,
        monkeypatch,
):
    monkeypatch.setattr(client, 'ignore_codes', {33000})
    httpx_mock.add_response(
        json={
            'retCode': 33000,
            'retMsg': 'Error message',
            'result': {},
            'time': 123,
        },
    )

    await client.request(
        method='GET',
        url='/test_client_request_response_with_ignore_codes',
    )

    assert True


@pytest.mark.anyio
async def test_client_request(
        add_httpx_response,
        client: BaseHTTP,
):
    add_httpx_response(
        result={'request': 'ok'},
    )
    data = await client.request(method='GET', url='/test_client_request')
    assert data == {'request': 'ok'}


@pytest.mark.anyio
async def test_client_get(
        add_httpx_response,
        client: BaseHTTP,
):
    add_httpx_response(
        method='GET',
        result={'get': 'ok'},
    )
    data = await client.get('/test_client_get')
    assert data == {'get': 'ok'}


@pytest.mark.anyio
async def test_client_post(
        add_httpx_response,
        client: BaseHTTP,
):
    add_httpx_response(
        method='POST',
        result={'post': 'ok'},
    )
    data = await client.post('/test_client_post')
    assert data == {'post': 'ok'}
