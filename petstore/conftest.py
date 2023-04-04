import os

import pytest
from dotenv import load_dotenv


load_dotenv()


@pytest.fixture(scope='session')
def options() -> dict:
    return {'url': os.getenv('PET_URL')}
