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

@pytest.mark.smoke
@pytest.mark.cart
def test_add_item_to_cart(self, login_page, home_page, cart_page):
    """Test item added from home appears in cart."""
    login_page.open()
    login_page.loin(VALID_USERNAME, VALID_PASSWORD)
    home_page.add_product_by_name(PRODUCT_NAME)
    home_page.go_to_cart()
    assert cart_page.is_item_in_cart(PRODUCT_NAME), \
        f"{PRODUCT_NAME} was not added to cart"

#------------ Regression Test-------------

@pytest.mark.regression
@pytest.mark.cart
def test_cart_item_count(self, login_page, home_page, cart_page):
    """Test cart shows correct item count."""
    login_page.open()
    login_page.login(VALID_USERNAME, VALID_PASSWORD)
    home_page.add_product_by_name(PRODUCT_NAME)
    home_page.go_to_cart()
    assert cart_page.get_cart_item_count() == 1, \
        "Cart item count is not 1"

@pytest.mart.regression
@pytest.mark.cart
def test_cart_item_price(self, login_page, home_page, cart_page):
    """Test cart shows correct item price."""
    login_page.open()
    login_page.login(VALID_USERNAME, VALID_PASSWORD)
    home_page.add_product_by_name(PRODUCT_NAME)
    home_page.go_to_cart()
    price = cart_page.get_cart_item_price()
    assert PRODUCT_PRICE in price, \
        f"Expected price {PRODUCT_PRICE} was not found in cart"











