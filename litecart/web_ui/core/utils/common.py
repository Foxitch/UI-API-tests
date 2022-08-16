from typing import List
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.select import Select


class Common:

    def __init__(self, app):
        self.app = app

    def is_present(self, locator: tuple, timeout: int = 10) -> WebElement:
        return wait(self.app.wd, timeout).until(
            ec.presence_of_element_located(locator)
        )

    def are_present(self, locator: tuple, timeout: int = 10) -> List[WebElement]:
        return wait(self.app.wd, timeout).until(
            ec.presence_of_all_elements_located(locator)
        )

    def validate_element_visible_on_the_page(self, locator: tuple, timeout: int = 5) -> bool:
        try:
            self.app.common.is_present(locator, timeout)
            return True
        except (TimeoutException, NoSuchElementException):
            return False

    @staticmethod
    def select_element(element: WebElement) -> Select:
        return Select(element)

    def execute_script(self, java_script: str, element: WebElement = None) -> None:
        return self.app.wd.execute_script(java_script, element)
