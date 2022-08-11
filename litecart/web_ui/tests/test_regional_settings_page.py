import time
import allure
from litecart.web_ui.pages.application import Application


@allure.suite('Regional Settings Page')
class TestRegionalSettingsPage:

    @allure.title('Validate possibility to open Regional Settings page')
    def test_open_regional_settings_page(self, app: Application):
        app.regional_settings_page.open_regional_settings_page()

    @allure.title('Validate possibility to change currency')
    def test_change_currency(self, app: Application):
        app.regional_settings_page.change_currency()

