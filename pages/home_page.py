from pages.base_page import BasePage
from test_data.data import PRODUCT_NAME, PRODUCT_PRICE


class HomePage(BasePage):
    """Page object for the Home/Inventory page."""

#-----------Locators----------
PAGE_TITLE = ".title"
PRODUCT_LIST = ".inventory_list"
PRODUCT_ITEMS = ".inventory_items"
PRODUCT_NAMES = ".inventory_item_name"
PRODUCT_PRICE = ".inventory_item_price"
ADD_TO_CART_BUTTON ="button[data-test^='add-to-cart']"
CART_ICON = ".shopping_cart_link"
CART_BADGE = ".shopping_cart_badge"
SORT_DROPDOWN = ".product_sort_container"
BURGER_MENU = "#react-burger-menu-btn"
LOGOUT_LINK = "#logout_sidebar_link"

#----------Actions----------------
def get_page_title(self):
    """Return the page title text"""
    return self.get_text(self.PAGE_TITLE)

def get_all_product_names(self):
    """Return list of all product names."""
    return self.page.locator(self.PRODUCT_NAMES).all_text_content()

def get_all_product_prices(self):
    """Return list of all product prices."""
    return self.page.locator(self.PRODUCT_PRICE).all_text_content()

def add_first_product_to_cart(self):
    """Click Add to Cart on the first product."""
    self.page.locator(self.ADD_TO_CART_BUTTON).first.click()

def add_product_by_name(self, product_name: str):
    """Add a specific product to cart by name."""
    self.page.locator(
        f"//div[text()='{product_name}']/ancestor::div[@class='inventory_item']//button"
    ).click()

def get_cart_count(self):
    """Return number shown on cart badge."""
    if self.is_visible(self.CART_BADGE):
        return self.get_text(self.CART_BADGE)
    return "0"

def go_to_cart(self):
    """Click cart icon to open cart."""
    self.click(self.CART_ICON)

def sort_products(self, option: str):
    """Sort products - options: az, za, lohi, hilo."""
    self.page.locator(self.SORT_DROPDOWN).select_option(option)

def logout(self):
    """Open burger menu and click logout."""
    self.click(self.BURGER_MENU)
    self.page.wait_for_selector(self.LOGOUT_LINK)
    self.click(self.LOGOUT_LINK)

#------------Assertions---------------

