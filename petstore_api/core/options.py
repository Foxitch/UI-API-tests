def pytest_addoption(parser) -> None:
    parser.addoption("--proto", action="store", default='https')
    parser.addoption("--url", action="store", default='petstore.swagger.io')

