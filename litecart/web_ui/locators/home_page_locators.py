from selenium.webdriver.common.by import By


class HomePageLocators:

    EMAIL_INPUT_FILED = (By.XPATH, '//input[@name="email"]')
    PASSWORD_INPUT_FIELD = (By.XPATH, '//input[@name="password"]')
    LOGIN_BUTTON = (By.XPATH, '//button[@name="login"]')
    LOGOUT_BUTTON = (By.XPATH, '(//a[@href="http://localhost/litecart/en/logout"])[1]')
    POP_UP_LINE = (By.XPATH, '//div[@class="notice success"]')
    CURRENT_CURRENCY = (By.XPATH, '//div[@class="currency"]/span')
    CURRENT_COUNTRY = (By.XPATH, '//div[@class="country"]')

    # Footer

    REGIONAL_SETTINGS_BUTTON = (By.XPATH, "//a[text()='Regional Settings']")
    CREATE_ACCOUNT_BUTTON = (By.XPATH, "//a[text()='Create Account']")
