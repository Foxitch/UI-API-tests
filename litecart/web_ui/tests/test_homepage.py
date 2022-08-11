import allure
from litecart.web_ui.pages.application import Application


@allure.suite('Home Page')
class TestHomePage:

    @allure.title('Check a logout process')
    def test_logout_process(self, app: Application):
        app.homepage.logout_process()

    @allure.title('Validate impossibility to create User without entered captcha')
    def check_the_impossibility_to_create_user_without_captcha(self, app: Application):
        app.homepage.logout_process()

