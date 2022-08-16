from selenium.webdriver.common.by import By


class HomePageLocators:

    EMAIL_INPUT_FILED = (By.XPATH, '//input[@name="email"]')
    PASSWORD_INPUT_FIELD = (By.XPATH, '//input[@name="password"]')
    LOGIN_BUTTON = (By.XPATH, '//button[@name="login"]')
    LOGOUT_BUTTON = (By.XPATH, '(//a[@href="http://localhost/litecart/en/logout"])[1]')
    POP_UP_LINE = (By.XPATH, '//div[@class="notice success"]')
    CURRENT_CURRENCY = (By.XPATH, '//div[@class="currency"]/span')
    CURRENT_COUNTRY = (By.XPATH, '//div[@class="country"]')
    PRODUCTS_ON_THE_MAIN_PAGE = (By.XPATH, '//ul[@class="listing-wrapper products"]/*')
    SELECTED_PRODUCT_PRICE = (By.XPATH, '//span[@itemprop="price"]')
    SALE_PRODUCT_PRICE = (By.XPATH, '//strong[@class="campaign-price"]')
    ADD_TO_CART_BUTTON = (By.XPATH, '//button[@name="add_cart_product"]')
    PRODUCTS_OPTION_SIZE_SELECT = (By.XPATH, '//select[@name="options[Size]"]')
    CART_PRICE = (By.XPATH, '//span[@class="formatted_value"]')
    QUANTITY_INPUT_FIELD = (By.XPATH, '//input[@name="quantity"]')
    OPEN_THE_CART_BUTTON = (By.XPATH, '//a[contains(@href, "checkout")]')
    REMOVE_FROM_CART_BUTTON = (By.XPATH, '//button[@name="remove_cart_item"]')

    # Footer

    REGIONAL_SETTINGS_BUTTON = (By.XPATH, "//a[text()='Regional Settings']")
    CREATE_ACCOUNT_BUTTON = (By.XPATH, "//a[text()='Create Account']")
