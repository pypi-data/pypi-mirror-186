from time import time
from typing import Generator

from httpx import Auth, Request, Response

from exapi.bitget import utils


class BitgetAuth(Auth):
    requires_request_body = True

    def __init__(
            self,
            api_key: str,
            api_secret: str,
            api_passphrase: str,
    ):
        self.__api_key = api_key
        self.__api_secret = api_secret
        self.__api_passphrase = api_passphrase

    def auth_flow(
            self,
            request: Request,
    ) -> Generator[Request, Response, None]:
        url = request.url
        timestamp = int(time() * 1000)
        request_path = url.path + url.query.decode('ascii')
        body = request.content.decode('utf-8') if request.method == 'POST' else ''
        payload = utils.calc_hash(
            timestamp=timestamp,
            method=request.method,
            request_path=request_path,
            body=body,
        )
        sign = utils.sign(
            payload=payload,
            secret=self.__api_secret,
        )
        headers = {
            'ACCESS-KEY': self.__api_key,
            'ACCESS-SIGN': sign,
            'ACCESS-TIMESTAMP': str(timestamp),
            'ACCESS-PASSPHRASE': self.__api_passphrase,
        }
        request.headers.update(headers=headers)

        yield request
