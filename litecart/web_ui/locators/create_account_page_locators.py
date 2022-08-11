from selenium.webdriver.common.by import By


class CreateAccountPageLocators:

    FIRST_NAME_INPUT_FIELD = (By.XPATH, '//input[@name="firstname"]')
    LAST_NAME_INPUT_FIELD = (By.XPATH, '//input[@name="lastname"]')
    ADDRESS_1_INPUT_FIELD = (By.XPATH, '//input[@name="address1"]')
    POSTCODE_INPUT_FIELD = (By.XPATH, '//input[@name="postcode"]')
    CITY_INPUT_FIELD = (By.XPATH, '//input[@name="city"]')
    SELECT_COUNTRY_DROP_DOWN = (By.XPATH, '//span[@role="presentation"]')
    EMAIL_INPUT_FIELD = (By.XPATH, '//input[@name="email"]')
    PHONE_INPUT_FIELD = (By.XPATH, '//input[@name="phone"]')
    DESIRED_PASSWORD_INPUT_FIELD = (By.XPATH, '//input[@name="password"]')
    CONFIRM_PASSWORD_INPUT_FIELD = (By.XPATH, '//input[@name="confirmed_password"]')
    CREATE_ACCOUNT_BUTTON = (By.XPATH, '//button[@name="create_account"]')
    ERROR_POP_UP = (By.XPATH, '//div[@class="notice errors"][1]')

