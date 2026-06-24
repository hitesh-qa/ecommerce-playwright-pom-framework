import pytest
from test_data.data import (
    VALID_USERNAME, VALID_PASSWORD,
    PRODUCT_NAME, PRODUCT_PRICE,
    CART_PAGE_TITLE
)

class TestCart:
    """Test cases for Cart funtionality"""

#------------Smoke Test----------

@pytest.mark.smoke
@pytest.mark.cart
def test_cart_page_loads(self, login_page, home_page, cart_page):
    """Test cart page open loads correctly"""
    login_page.open()
    login_page.login(VALID_USERNAME, VALID_PASSWORD)
    home_page.go_to_cart()
    assert cart_page.is_cart_page_loaded(), \
        "Cart page did not load"

