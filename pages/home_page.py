from selenium.webdriver.remote.webelement import WebElement
from pages.base_page import BasePage
from typing import List


class HomePage(BasePage):
    """ Page Objects for home page. """

    def __init__(self, driver):
        super().__init__(driver)
        self.XPATH_PROMO_TITLE_START = "//h1[contains(@class, 'promo__title')]/*[contains(@class, 'd-none')]"
        self.XPATH_INITIAL_MESSAGE = "//div[@class='initial-message-bubble']"
        self.XPATH_IFRAME_CHAT = "//iframe[@title='chat widget']"

    def get_promo_title(self) -> str:
        """ Extracts promotion headline. """
        els: List[WebElement] = self._driver.find_elements_by_xpath(self.XPATH_PROMO_TITLE_START)
        els_text = [el.text for el in els]
        return ' '.join(els_text)

    def is_chat_box_visible(self) -> bool:
        """ Checks visibility of element. """
        el: WebElement = self._driver.find_element_by_xpath(self.XPATH_INITIAL_MESSAGE)
        return el.is_displayed()

    def switch_to_iframe(self) -> None:
        """ Switches to iframe."""
        self._driver.switch_to.frame(self._driver.find_element_by_xpath(self.XPATH_IFRAME_CHAT))
