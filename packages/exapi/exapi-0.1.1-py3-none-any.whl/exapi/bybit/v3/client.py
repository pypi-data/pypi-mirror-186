from json import JSONDecodeError

from httpx import HTTPStatusError, RequestError, URL
from pydantic import ValidationError

from exapi import Client
from exapi.bybit.exceptions import BybitException
from exapi.bybit.v3.auth import ByBitAuth
from exapi.bybit.v3.constants import BASE_API_URL
from exapi.bybit.v3.models import ResponseData
from exapi.types import Data


class BaseClient(Client):

    def __init__(
            self,
            base_url: URL | str = BASE_API_URL,
            api_key: str = None,
            api_secret: str = None,
            recv_window: int = 5000,
            **kwargs,
    ):
        super().__init__(base_url=base_url, **kwargs)
        self.__api_key = api_key
        self.__api_secret = api_secret
        self.__recv_window = recv_window

    @property
    def _recv_window(self) -> int:
        return self.__recv_window

    @property
    def _auth(self) -> ByBitAuth:
        if not hasattr(self, '__auth'):
            if self.__api_key is None:
                raise BybitException('API key not present')
            if self.__api_secret is None:
                raise BybitException('API secret not present')

            self.__auth = ByBitAuth(
                api_key=self.__api_key,
                api_secret=self.__api_secret,
                recv_window=self.__recv_window,
            )

        return self.__auth

    async def request(self, *args, **kwargs) -> Data:
        try:
            response = await super().request(*args, **kwargs)
        except RequestError as exc:
            raise BybitException(str(exc), request=exc.request)
        except HTTPStatusError as exc:
            raise BybitException(str(exc), request=exc.request, response=exc.response)

        try:
            json_data = response.json()
        except JSONDecodeError as exc:
            self._logger.exception(f'Invalid JSON: {response.text}')
            raise BybitException(str(exc), response=response)

        try:
            data = ResponseData(**json_data)
        except (ValidationError, ValueError, TypeError, AssertionError) as exc:
            self._logger.exception(f'Could not validate response data: {response.text}')
            raise BybitException(str(exc), response=response)

        if data.ret_code:
            self._logger.error(f'code: {data.ret_code}, msg: {data.ret_msg}')
            raise BybitException(message=data.ret_msg, code=data.ret_code, response=response)

        return getattr(data, 'result', None)
