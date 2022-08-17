import allure
import pytest
from litecart.web_ui.pages.application import Application


@allure.suite('Create Account Page')
class TestCreateAccountPage:

    @pytest.mark('ui')
    @allure.title('Validate possibility to open Create Account page')
    def test_open_create_account_page(self, app: Application):
        app.create_account.open_create_account_page()

    @pytest.mark('ui')
    @allure.title('Validate impossibility to create User without entered captcha')
    def test_check_the_impossibility_to_create_user_without_captcha(self, app: Application):
        app.create_account.open_create_account_page()
        app.create_account.fill_all_required_fields_and_click_create_account_btn()
