from time import time
from typing import Generator

from httpx import Auth, Request, Response

from exapi.bybit import utils


class ByBitAuth(Auth):
    requires_request_body = True

    def __init__(
            self,
            api_key: str,
            api_secret: str,
            recv_window: int = 5000,
    ):
        self.__api_key = api_key
        self.__api_secret = api_secret
        self.__recv_window = recv_window

    def auth_flow(
            self,
            request: Request,
    ) -> Generator[Request, Response, None]:
        timestamp = int(time() * 10 ** 3)

        if request.method == 'POST':
            data = request.content.decode('utf-8')
        else:
            data = request.url.query.decode('ascii')

        payload = utils.calc_hash(
            timestamp=timestamp,
            secret=self.__api_secret,
            recv_window=self.__recv_window,
            data=data,
        )
        sign = utils.sign(
            payload=payload,
            secret=self.__api_secret,
        )
        headers = {
            'X-BAPI-API-KEY': self.__api_key,
            'X-BAPI-SIGN': sign,
            'X-BAPI-SIGN-TYPE': '2',
            'X-BAPI-TIMESTAMP': str(timestamp),
            'X-BAPI-RECV-WINDOW': str(self.__recv_window),
        }
        request.headers.update(headers=headers)

        yield request
