import pytest
from .context import ClientsPage


class TestClientsPage:
    """ Test class for clients page. """

    @pytest.mark.usefixtures("chrome_headless")
    def test_count_clients_list(self):
        url = "https://macopedia.com/clients"
        self.driver.get(url)
        clients_page = ClientsPage(self.driver)
        clients_count = clients_page.count_clients()
        assert clients_count == 15
