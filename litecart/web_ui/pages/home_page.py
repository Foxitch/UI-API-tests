import allure
from litecart.web_ui.locators.home_page_locators import HomePageLocators
from selenium.webdriver.remote.webelement import WebElement


class HomePage:
    """ If methods name contains 'get and 'btn' it should return action CLICK """

    def __init__(self, app):
        self.app = app

    def get_email_input_field(self) -> WebElement:
        return self.app.common.is_present(HomePageLocators.EMAIL_INPUT_FILED)

    def get_password_input_field(self) -> WebElement:
        return self.app.common.is_present(HomePageLocators.PASSWORD_INPUT_FIELD)

    def get_login_btn(self) -> None:
        return self.app.common.is_present(HomePageLocators.LOGIN_BUTTON).click()

    def get_logout_btn(self) -> None:
        return self.app.common.is_present(HomePageLocators.LOGOUT_BUTTON).click()

    def get_pop_up_text(self) -> str:
        return self.app.common.is_present(HomePageLocators.POP_UP_LINE).text

    def get_regional_settings_footer_btn(self) -> None:
        return self.app.common.is_present(HomePageLocators.REGIONAL_SETTINGS_BUTTON).click()

    def get_create_account_footer_btn(self) -> None:
        return self.app.common.is_present(HomePageLocators.CREATE_ACCOUNT_BUTTON).click()

    def get_current_currency(self) -> str:
        return self.app.common.is_present(HomePageLocators.CURRENT_CURRENCY).text

    def get_current_country(self) -> str:
        return self.app.common.is_present(HomePageLocators.CURRENT_COUNTRY).text

    @allure.step('Logout process')
    def logout_process(self) -> None:
        self.get_logout_btn()
        assert self.get_pop_up_text() == 'You are now logged out.', \
            'Expected successful pop-up message after the logout process'
