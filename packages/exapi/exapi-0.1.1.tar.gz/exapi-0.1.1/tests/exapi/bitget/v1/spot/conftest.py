import pytest

from exapi.bitget.v1.spot import SpotClient
from tests.settings import Settings


@pytest.fixture(scope='module')
async def bitget_spot(settings: Settings):
    async with SpotClient(
            api_key=settings.BITGET_API_KEY,
            api_secret=settings.BITGET_API_SECRET,
            api_passphrase=settings.BITGET_API_PASSPHRASE,
    ) as client:
        yield client
