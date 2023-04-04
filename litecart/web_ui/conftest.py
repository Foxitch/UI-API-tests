import os

from dotenv import load_dotenv

import allure
import pytest

from datetime import datetime

from litecart.web_ui.pages.application import Application


load_dotenv()


@pytest.fixture(scope='function')
def app() -> Application:
    fixture = Application()
    fixture.session.login(
        email=os.getenv('LOGIN'),
        password=os.getenv('PASSWORD'),
        url=os.getenv('URL')
    )
    yield fixture
    allure.attach(fixture.wd.get_screenshot_as_png(),
                  name=f"Screenshot {datetime.today()}",
                  attachment_type=allure.attachment_type.PNG)
    fixture.destroy()
