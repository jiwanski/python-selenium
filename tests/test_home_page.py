import pytest
from .context import HomePage


class TestHomePage:
    """ Test class for home page. """

    @pytest.mark.usefixtures("chrome_headless")
    def test_promo_title(self):
        url = "https://macopedia.com"
        self.driver.get(url)
        home_page = HomePage(self.driver)
        title = home_page.get_promo_title()
        assert title == 'Grow your business\nwith a technical partner you can trust'

    @pytest.mark.usefixtures("chrome_headless")
    def test_initial_message_visibility_default(self):
        url = "https://macopedia.com"
        self.driver.get(url)
        home_page = HomePage(self.driver)
        home_page.switch_to_iframe()
        initial_message_visible = home_page.is_chat_box_visible()
        assert initial_message_visible is True
