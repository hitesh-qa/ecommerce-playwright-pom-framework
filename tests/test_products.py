import pytest
from test_data import (
    VALID_USERNAME, VALID_PASSWORD,
    PRODUCT_NAME, PRODUCT_PRICE
)
from utils.helpers import Helpers

class TestProduct:
    """Test cases for Product funtionality."""

#------------Smoke Tests-----------
@pytest.mark.smoke
@pytest.mark.products
def test_home_page_loads(self, login_page, home_page):
    """Test inventory page loads after login."""
    login_page.open()
    login_page.login(VALID_USERNAME, VALID_PASSWORD)
    assert home_page.is_home_page_loaded(), \
    "Home page did not load after login"


