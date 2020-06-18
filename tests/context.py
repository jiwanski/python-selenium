import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from pages.home_page import HomePage
from pages.clients_page import ClientsPage
import fixtures.driver as fixtures
