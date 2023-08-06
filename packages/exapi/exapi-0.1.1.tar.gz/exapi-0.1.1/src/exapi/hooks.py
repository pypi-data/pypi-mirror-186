import logging

from httpx import Request, Response

logger = logging.getLogger(__name__)


async def raise_on_4xx_5xx(response: Response):
    response.raise_for_status()


async def log_request(request: Request):
    method = request.method
    content = await request.aread() if method == 'POST' else ''
    logger.debug(f'Request -> {method=} {request.url} {content=}')


async def log_response(response: Response):
    request = response.request
    method = request.method
    status_code = response.status_code
    content = await response.aread()
    logger.debug(f'Response -> {status_code=} {method=} {request.url} {content=}')
