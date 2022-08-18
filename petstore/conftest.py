import pytest
from petstore.api.core.options import *


@pytest.fixture(scope='function')
def options(request) -> dict:
    dict_options = dict()
    dict_options['proto'] = request.config.getoption('proto_pet')
    dict_options['url'] = request.config.getoption('url_pet')
    return dict_options
