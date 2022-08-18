import allure
import pytest
from litecart.web_ui.pages.application import Application


@allure.suite('Home Page')
class TestHomePage:

    @pytest.mark.ui
    @allure.title('Check a logout process')
    def test_logout_process(self, app: Application):
        app.homepage.logout_process()

    @pytest.mark.ui
    @allure.title('Validate possibility to open cart from the Home page')
    def test_open_a_cart(self, app: Application):
        app.homepage.open_cart()

    @pytest.mark.ui
    @allure.title('Add products to the cart')
    def test_add_product_to_the_cart(self, app: Application):
        app.homepage.select_a_product_from_the_main_page()
        app.homepage.validate_added_price_to_cart()

    @pytest.mark.ui
    @allure.title('Validate possibility to add more than one product to cart and empty it')
    def test_add_some_products_to_the_cart_and_empty_it(self, app: Application):
        app.homepage.select_a_product_from_the_main_page()
        app.homepage.add_some_products_to_the_cart(products_count=3)
        app.homepage.open_cart()
        app.homepage.empty_cart()

    @pytest.mark.ui
    @allure.title('Validate possibility to make order')
    def test_confirmation_order(self, app: Application):
        app.homepage.select_a_product_from_the_main_page()
        app.homepage.add_some_products_to_the_cart(products_count=1)
        app.homepage.make_order()
