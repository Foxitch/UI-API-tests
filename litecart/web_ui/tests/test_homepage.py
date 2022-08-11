import allure
from litecart.web_ui.pages.application import Application


@allure.suite('Home Page')
class TestHomePage:

    @allure.title('Check a logout process')
    def test_logout_process(self, app: Application):
        app.homepage.logout_process()

