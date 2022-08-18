def pytest_addoption(parser) -> None:
    parser.addoption("--proto_pet", action="store", default='https')
    parser.addoption("--url_pet", action="store", default='petstore.swagger.io')

