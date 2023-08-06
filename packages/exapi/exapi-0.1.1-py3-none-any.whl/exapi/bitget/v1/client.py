from json import JSONDecodeError

from httpx import HTTPStatusError, RequestError, URL
from pydantic import ValidationError

from exapi import Client
from exapi.bitget.exceptions import BitgetException
from exapi.bitget.v1 import BitgetAuth
from exapi.bitget.v1.constants import BASE_API_URL
from exapi.bitget.v1.models import ResponseData
from exapi.types import Data


class BaseClient(Client):

    def __init__(
            self,
            base_url: URL | str = BASE_API_URL,
            api_key: str = None,
            api_secret: str = None,
            api_passphrase: str = None,
            **kwargs,
    ):
        super().__init__(base_url=base_url, **kwargs)
        self.__api_key = api_key
        self.__api_secret = api_secret
        self.__api_passphrase = api_passphrase

    @property
    def _auth(self) -> BitgetAuth:
        if not hasattr(self, '__auth'):
            if self.__api_key is None:
                raise BitgetException('API key not present')
            if self.__api_secret is None:
                raise BitgetException('API secret not present')
            if self.__api_passphrase is None:
                raise BitgetException('API passphrase not present')

            self.__auth = BitgetAuth(
                api_key=self.__api_key,
                api_secret=self.__api_secret,
                api_passphrase=self.__api_passphrase,
            )

        return self.__auth

    async def request(self, *args, **kwargs) -> Data:
        try:
            response = await super().request(*args, **kwargs)
        except RequestError as exc:
            raise BitgetException(str(exc), request=exc.request)
        except HTTPStatusError as exc:
            raise BitgetException(str(exc), request=exc.request, response=exc.response)

        try:
            json_data = response.json()
        except JSONDecodeError as exc:
            self._logger.exception(f'Invalid JSON: {response.text}')
            raise BitgetException(str(exc), response=response)

        try:
            data = ResponseData(**json_data)
        except (ValidationError, ValueError, TypeError, AssertionError) as exc:
            self._logger.exception(f'Could not validate response data: {response.text}')
            raise BitgetException(str(exc), response=response)

        if data.code:
            self._logger.error(f'code: {data.code}, msg: {data.msg}')
            raise BitgetException(message=data.msg, code=data.code, response=response)

        return getattr(data, 'data', None)
