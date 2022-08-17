import pytest


def pytest_addoption(parser) -> None:
    parser.addoption("--proto", action="store", default='https')
    parser.addoption("--url", action="store", default='petstore.swagger.io')


@pytest.fixture(scope='function')
def options(request) -> dict:
    dict_options = dict()
    dict_options['proto'] = request.config.getoption('proto')
    dict_options['url'] = request.config.getoption('url')
    return dict_options
