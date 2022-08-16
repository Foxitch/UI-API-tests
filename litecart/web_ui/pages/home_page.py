import random
import time

import allure
from selenium.common import TimeoutException

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

    def __get_list_with_product_on_the_main_page(self) -> list[WebElement]:
        return self.app.common.are_present(HomePageLocators.PRODUCTS_ON_THE_MAIN_PAGE)

    def validate_products_option_is_on_the_page(self) -> bool:
        return self.app.common.validate_element_visible_on_the_page(
            locator=HomePageLocators.PRODUCTS_OPTION_SIZE_SELECT, timeout=3
        )

    def __get_quantity_input_field(self) -> WebElement:
        return self.app.common.is_present(HomePageLocators.QUANTITY_INPUT_FIELD)

    def __get_add_to_cart_btn(self) -> None:
        return self.app.common.is_present(HomePageLocators.ADD_TO_CART_BUTTON).click()

    def __get_move_to_cart_btn(self) -> None:
        return self.app.common.is_present(HomePageLocators.OPEN_THE_CART_BUTTON).click()

    def __get_cart_price(self) -> int:
        cart_price = self.app.common.is_present(HomePageLocators.CART_PRICE).text
        return int(cart_price.split('$')[-1])

    def get_remove_from_cart_btn(self) -> None:
        return self.app.common.is_present(HomePageLocators.REMOVE_FROM_CART_BUTTON).click()

    @allure.step('Logout process')
    def logout_process(self) -> None:
        self.get_logout_btn()
        assert self.get_pop_up_text() == 'You are now logged out.', \
            'Expected successful pop-up message after the logout process'

    @allure.step('Open a cart')
    def open_a_cart(self) -> None:
        self.__get_move_to_cart_btn()
        assert 'checkout' in self.app.wd.current_url, 'Cart is not opened'

    @allure.step('Change a products quantity')
    def change_a_products_quantity(self, product_count: int) -> None:
        self.app.common.execute_script(
            f"arguments[0].setAttribute('value','{product_count}')", self.__get_quantity_input_field()
        )

    @allure.step('Get price of the selected product')
    def get_price_of_the_selected_product(self) -> int:
        try:
            price = self.app.common.is_present(
                locator=HomePageLocators.SELECTED_PRODUCT_PRICE, timeout=3
            ).text
        except TimeoutException:
            price = self.app.common.is_present(
                locator=HomePageLocators.SALE_PRODUCT_PRICE, timeout=3
            ).text

        return int(price.split('$')[-1])

    @allure.step('Select a products option')
    def select_a_products_option(self) -> None:
        if self.validate_products_option_is_on_the_page() is True:
            select_option = self.app.common.select_element(
                element=self.app.common.is_present(HomePageLocators.PRODUCTS_OPTION_SIZE_SELECT)
            )
            select_option.select_by_value('Small')

    @allure.step('Select a product')
    def select_a_product_from_the_main_page(self) -> None:
        products_count: int = len(self.__get_list_with_product_on_the_main_page())
        self.__get_list_with_product_on_the_main_page()[random.randint(0, products_count - 1)].click()
        self.select_a_products_option()

    @allure.step('Validate added price to cart is correct')
    def validate_added_price_to_cart(self, products_count: int = 1) -> None:
        cart_price: int = self.__get_cart_price()
        product_price: int = self.get_price_of_the_selected_product() * products_count

        self.__get_add_to_cart_btn()
        time.sleep(3)

        assert self.__get_cart_price() == cart_price + product_price, \
            f'Expected cart price is {cart_price + product_price}, actual is {self.__get_cart_price()}'

    @allure.step('Add some products to the cart')
    def add_some_products_to_the_cart(self, products_count: int) -> None:
        self.change_a_products_quantity(products_count)
        self.validate_added_price_to_cart(products_count)


