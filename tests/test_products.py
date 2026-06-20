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

@pytest.mark.smoke
@pytest.mark.products
def test_products_are_displayed(self, login_page, home_page):
    """Test products are visible on home page."""
    login_page.open()
    login_page.login(VALID_USERNAME, VALID_PASSWORD)
    names = home_page.get_all_products_names()
    assert len(names) > 0, \
        "No products displayed on home page"

#-------------Regression Testings -----------
@pytest.mark.regression
@pytest.mark.products
def test_products_count(self, login_page, home_page):
    """Test exactly 6 products are displayed."""
    login_page.open()
    login_page.login(VALID_USERNAME, VALID_PASSWORD)
    name = home_page.get_all_product_names()
    assert len(names) == 6, \
    f"Expected 6 products but got {len(names)}"

@pytest.mark.regression
@pytest.mark.products
def test_sort_products_a_to_z(self, login_page, home_page):
    """Test products sort A to Z correctly."""
    login_page.open()
    login_page.login(VALID_USERNAME, VALID_PASSWORD)
    home_page.sort_products("az")
    names = home_page.get_all_products_names()
    assert Helpers.is_names_sorted_a_to_z(names), \
        "Products not sorted A to Z"


































