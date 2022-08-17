def pytest_addoption(parser) -> None:
    parser.addoption("--proto", action="store", default='http')
    parser.addoption("--url", action="store", default='localhost/litecart/en')
    parser.addoption("--email", action="store", default='john@gmail.com')
    parser.addoption("--password", action="store", default='123456')
