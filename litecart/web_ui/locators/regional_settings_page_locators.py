from selenium.webdriver.common.by import By


class RegionalSettingsPageLocators:

    SELECT_LANGUAGE_DROP_DOWN = (By.XPATH, '//select[@name="language_code"')
    SELECT_CURRENCY_DROP_DOWN = (By.XPATH, '//select[@name="currency_code"]')
    SELECT_COUNTRY_DROP_DOWN = (By.XPATH, '//span[@role="presentation"]')
    LIST_WITH_COUNTRIES = (By.XPATH, '//ul[@role="tree"]/*')
    SAVE_BUTTON = (By.XPATH, '//button[@type="submit"]')
