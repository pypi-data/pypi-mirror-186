import os

import pytest
from dotenv import load_dotenv

from tests.settings import Settings


@pytest.fixture(scope='session', autouse=True)
def load_env():
    old_environ = dict(os.environ)

    load_dotenv()

    yield

    os.environ.clear()
    os.environ.update(old_environ)


@pytest.fixture(scope='session')
def settings():
    return Settings()


@pytest.fixture(scope='session')
def anyio_backend():
    return 'asyncio', {'use_uvloop': True}
