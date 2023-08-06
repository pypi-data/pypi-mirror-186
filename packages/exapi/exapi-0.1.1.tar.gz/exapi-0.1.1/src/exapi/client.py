import logging
from json import JSONDecodeError
from types import TracebackType
from typing import Self, Type

from httpx import AsyncClient, Auth, HTTPStatusError, RequestError, URL
from pydantic import BaseModel

from exapi import hooks
from exapi.constants import VERSION
from exapi.exceptions import ExapiException
from exapi.types import Data


class Client:

    def __init__(
            self,
            base_url: URL | str = '',
            log_level: int = logging.INFO,
            log_requests: bool = False,
            log_responses: bool = False,
            **kwargs,
    ):
        self.__logger = logging.getLogger(__name__)

        if len(logging.root.handlers) == 0:
            # no handler on root logger set
            # we add handler just for this logger to not mess with custom logic from outside
            handler = logging.StreamHandler()
            handler.setFormatter(
                logging.Formatter(
                    fmt='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S',
                ),
            )
            handler.setLevel(log_level)
            self.__logger.addHandler(handler)

        self.__client = AsyncClient(
            event_hooks={
                'request': [hooks.log_request] if log_requests else [],
                'response': [hooks.raise_on_4xx_5xx, *([hooks.log_response] if log_responses else [])]
            },
            base_url=base_url,
            headers={
                'User-Agent': 'exapi-' + VERSION,
                'Accept': 'application/json',
            },
            **kwargs,
        )

    @property
    def _client(self) -> AsyncClient:
        return self.__client

    @property
    def _logger(self) -> logging.Logger:
        return self.__logger

    @property
    def _auth(self) -> Auth:
        raise ExapiException('Auth not implemented.')

    async def request(
            self,
            method: str,
            url: str,
            *,
            json: BaseModel | dict | None = None,
            params: BaseModel | dict | None = None,
            auth: bool = False,
            **kwargs,
    ) -> Data:
        if params is None:
            params = {}

        if isinstance(params, BaseModel):
            params = params.dict(exclude_none=True, by_alias=True)
        else:
            params = {k: v for k, v in params.items() if v is not None}

        if isinstance(json, BaseModel):
            json = json.dict(exclude_none=True, by_alias=True)

        # Bug fix: change floating whole numbers to integers to prevent auth signature errors.
        for key, val in params.items():
            if isinstance(val, float) and val == int(val):
                params[key] = int(val)

        try:
            return await self._client.request(
                method=method,
                url=url,
                json=json,
                params=params,
                auth=self._auth if auth else None,
                **kwargs
            )
        except RequestError as exc:
            self._logger.exception(f'Error while requesting {exc.request.url!r}.')
            raise
        except HTTPStatusError as exc:
            self._logger.exception(f'Error response {exc.response.status_code} while requesting {exc.request.url!r}.')
            raise

    async def get(self, url: str, auth: bool = False, **kwargs) -> Data:
        return await self.request(method='GET', url=url, auth=auth, **kwargs)

    async def post(self, url: str, auth: bool = False, **kwargs) -> Data:
        return await self.request(method='POST', url=url, auth=auth, **kwargs)

    async def aclose(self) -> None:
        await self._client.aclose()

    async def __aenter__(self) -> Self:
        await self._client.__aenter__()

        return self

    async def __aexit__(
            self,
            exc_type: Type[BaseException] | None = None,
            exc_value: BaseException | None = None,
            traceback: TracebackType | None = None,
    ) -> None:
        await self._client.__aexit__(exc_type, exc_value, traceback)
