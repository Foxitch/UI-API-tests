import pytest


def pytest_addoption(parser) -> None:
    parser.addoption("--proto", action="store", default='http')
    parser.addoption("--url", action="store", default='localhost/litecart/en')
    parser.addoption("--email", action="store", default='john@gmail.com')
    parser.addoption("--password", action="store", default='123456')


@pytest.fixture(scope="session")
def options(request) -> dict:
    dict_options = dict()
    dict_options['proto'] = request.config.getoption("proto")
    dict_options['url'] = request.config.getoption("url")
    dict_options['email'] = request.config.getoption('email')
    dict_options['password'] = request.config.getoption('password')
    return dict_options
