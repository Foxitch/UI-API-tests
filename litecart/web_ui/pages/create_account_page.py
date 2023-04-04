import allure
from litecart.web_ui.generator.generator import generated_user_data
from litecart.web_ui.locators.create_account_page_locators import CreateAccountPageLocators
from selenium.webdriver.remote.webelement import WebElement


class CreateAccountPage:
    """ If methods name contains 'get and 'btn' it should return action CLICK """

    def __init__(self, app):
        self.app = app

    def get_first_name_input_field(self) -> WebElement:
        return self.app.common.is_present(CreateAccountPageLocators.FIRST_NAME_INPUT_FIELD)

    def get_last_name_input_field(self) -> WebElement:
        return self.app.common.is_present(CreateAccountPageLocators.LAST_NAME_INPUT_FIELD)

    def get_address_1_input_field(self) -> WebElement:
        return self.app.common.is_present(CreateAccountPageLocators.ADDRESS_1_INPUT_FIELD)

    def get_postcode_input_field(self) -> WebElement:
        return self.app.common.is_present(CreateAccountPageLocators.POSTCODE_INPUT_FIELD)

    def get_city_input_field(self) -> WebElement:
        return self.app.common.is_present(CreateAccountPageLocators.CITY_INPUT_FIELD)

    def get_select_country_drop_down(self) -> WebElement:
        return self.app.common.is_present(CreateAccountPageLocators.SELECT_COUNTRY_DROP_DOWN)

    def get_email_input_field(self) -> WebElement:
        return self.app.common.is_present(CreateAccountPageLocators.EMAIL_INPUT_FIELD)

    def get_phone_input_field(self) -> WebElement:
        return self.app.common.is_present(CreateAccountPageLocators.PHONE_INPUT_FIELD)

    def get_desired_password_input_field(self) -> WebElement:
        return self.app.common.is_present(CreateAccountPageLocators.DESIRED_PASSWORD_INPUT_FIELD)

    def get_confirm_password_input_field(self) -> WebElement:
        return self.app.common.is_present(CreateAccountPageLocators.CONFIRM_PASSWORD_INPUT_FIELD)

    def get_create_account_btn(self) -> None:
        return self.app.common.is_present(CreateAccountPageLocators.CREATE_ACCOUNT_BUTTON).click()

    def get_error_pop_up_text(self) -> str:
        return self.app.common.is_present(CreateAccountPageLocators.ERROR_POP_UP).text

    @staticmethod
    def __clear_input_field(input_field: WebElement) -> None:
        return input_field.clear()

    @allure.step('Open the Create Account page')
    def open_create_account_page(self) -> None:
        self.app.homepage.logout_process()
        self.app.homepage.get_create_account_footer_btn()

        assert 'create_account' in self.app.wd.current_url, 'Create Account page is not opened'

    @allure.step('Fill all required fields and press "Create account" button')
    def fill_all_required_fields_and_click_create_account_btn(self) -> None:
        user_info = next(generated_user_data())
        password = user_info.password

        self.get_first_name_input_field().send_keys(user_info.first_name)
        self.get_last_name_input_field().send_keys(user_info.last_name)
        self.get_address_1_input_field().send_keys(user_info.address_1)

        self.__clear_input_field(self.get_postcode_input_field())
        self.get_postcode_input_field().send_keys(user_info.postcode)

        self.get_city_input_field().send_keys(user_info.city)
        self.get_email_input_field().send_keys(user_info.email)
        self.get_phone_input_field().send_keys(user_info.phone)
        self.get_desired_password_input_field().send_keys(password)
        self.get_confirm_password_input_field().send_keys(password)

        self.get_create_account_btn()
        assert self.get_error_pop_up_text() == 'Invalid CAPTCHA given', \
            f'Expected text is "Invalid CAPTCHA given", actual is {self.get_error_pop_up_text()}'
