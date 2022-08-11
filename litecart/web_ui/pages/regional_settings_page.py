import random
import allure
from litecart.web_ui.locators.regional_settings_page_locators import RegionalSettingsPageLocators
from selenium.webdriver.remote.webelement import WebElement


class RegionalSettingsPage:
    """ If methods name contains 'get and 'btn' it should return action CLICK """

    def __init__(self, app):
        self.app = app

    def get_select_language_drop_down(self) -> WebElement:
        return self.app.common.is_present(RegionalSettingsPageLocators.SELECT_LANGUAGE_DROP_DOWN)

    def get_select_currency_drop_down(self) -> WebElement:
        return self.app.common.is_present(RegionalSettingsPageLocators.SELECT_CURRENCY_DROP_DOWN)

    def get_select_country_drop_down(self) -> WebElement:
        return self.app.common.is_present(RegionalSettingsPageLocators.SELECT_COUNTRY_DROP_DOWN)

    def get_list_with_countries(self) -> list[WebElement]:
        return self.app.common.are_present(RegionalSettingsPageLocators.LIST_WITH_COUNTRIES)

    def get_save_btn(self) -> None:
        return self.app.common.is_present(RegionalSettingsPageLocators.SAVE_BUTTON).click()

    @allure.step('Open the Regional Settings page from the footer')
    def open_regional_settings_page(self):
        self.app.homepage.get_regional_settings_footer_btn()
        assert 'regional_setting' in self.app.wd.current_url, 'Regional Settings page is not opened'

    @allure.step('Select a currency')
    def __select_currency(self, currency: str) -> None:
        select_currency = self.app.common.select_element(self.get_select_currency_drop_down())
        select_currency.select_by_value(currency)

    @allure.step('Select a country')
    def __select_country(self, country_position: int) -> None:
        self.get_list_with_countries()[country_position].click()

    @allure.step('Change a currency and country on the Regional Settings page')
    def change_currency(self):
        self.open_regional_settings_page()
        self.__select_currency('EUR')
        self.get_select_country_drop_down().click()
        self.__select_country(random.randint(1, len(self.get_list_with_countries())))
        self.get_save_btn()

        assert self.app.homepage.get_current_currency() == 'EUR' and \
               self.app.homepage.get_current_country() != 'Russian Federation', 'Currency or country are not changed'



