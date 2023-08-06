from httpx import Request, Response


class ExapiException(Exception):

    def __init__(
            self,
            message: str,
            code: str | int | None = None,
            request: Request | None = None,
            response: Response | None = None,
    ):
        super().__init__(message)
        self.__code = code
        self.__request = getattr(response, 'request', None) if response and request is None else request
        self.__response = response
        self.__status_code = getattr(response, 'status_code', None) if response else None

    @property
    def code(self) -> str | int | None:
        return self.__code

    @property
    def request(self) -> Request | None:
        return self.__request

    @property
    def response(self) -> Response | None:
        return self.__response

    @property
    def status_code(self) -> int | None:
        return self.__status_code
