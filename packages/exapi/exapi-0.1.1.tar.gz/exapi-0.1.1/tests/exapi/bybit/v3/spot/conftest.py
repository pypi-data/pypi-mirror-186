from typing import Callable, Dict

import pytest

from tests.settings import Settings


@pytest.fixture(scope='module')
async def client(settings: Settings):
    async with SpotHTTP(
            endpoint=settings.BYBIT_ENDPOINT,
            api_key=settings.BYBIT_API_KEY,
            api_secret=settings.BYBIT_API_SECRET,
    ) as client:
        yield client


@pytest.fixture
def set_client_request_result(monkeypatch) -> Callable[[Dict], None]:
    def set_request_result(result: Dict):
        async def mock_request(*args, **kwargs) -> Dict:
            return result

        monkeypatch.setattr(BaseHTTP, 'request', mock_request)

    return set_request_result
