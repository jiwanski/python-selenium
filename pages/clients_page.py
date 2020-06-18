from selenium.webdriver.remote.webelement import WebElement
from pages.base_page import BasePage
from typing import List


class ClientsPage(BasePage):
    """ Page Objects for clients page. """

    def __init__(self, driver):
        super().__init__(driver)
        self.CSS_CLIENTS_LIST = "ul.list-clients > li"

    def count_clients(self) -> int:
        self._driver: WebElement  # used to force code completion in IDE; not exactly necessary
        els: List[WebElement] = self._driver.find_elements_by_css_selector(self.CSS_CLIENTS_LIST)
        count = len(els)
        return count
