from selenium.webdriver.chrome.webdriver import WebDriver
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager


class BaseApplication:

    def __init__(self):
        self.wd = self.create_driver()

    def create_driver(self) -> WebDriver:
        options = self.add_options()
        wd = webdriver.Chrome(ChromeDriverManager().install(), options=options)
        return wd

    def add_options(self) -> Options:
        """ If turn off "--headless mode", "--window-size=1920x1080" should be turned off too """

        options = Options()
        options.add_argument('--no-sandbox')
        options.add_argument('--headless')
        options.add_argument('--window-size=1920x1080')
        options.add_argument('--start-maximized')
        options.add_argument('--disable-gpu')
        options.add_argument('--disable-dev-shm-usage')
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        return options

    def destroy(self) -> None:
        self.wd.quit()
