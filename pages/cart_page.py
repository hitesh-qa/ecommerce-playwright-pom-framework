from pages.base_page import BasePage

class CartPage(BasePage):
    """Page object for the Cart page."""

#--------------Locattors-----------
CART_TITLE = ".title"
CART_ITEMS = ".cart_item"
ITEM_NAME = ".inventory_item_name"
ITEM_PRICES = ".inventory_item_price"
ITEM_QUANTITY = ".cart_quantity"
REMOVE_BUTTON = ".button[data-test^='remove']"
CONTINUE_SHOPPING = "#continue-shopping"
CHECKOUT_BUTTON = "#checkout"

#------------Action---------
def get_cart_title(self):
    """Return cart page title."""
    return self.get_text(self.CART_TITLE)

def get_cart_item_names(self):
    """Return list of all item names in cart."""
    return self.page.locator(self.ITEM_NAME).all_text_contents()

def get_cart_item_prices(self):
    """Return list of all item prices in cart."""
    return self.page.locator(self.ITEM_PRICES).all_text_contents()

def get_cart_item_count(self):
    """Return number of all items in cart."""
    return self.page.locator(self.CART_ITEMS).count()

def remove_item_from_cart(self):
    """Click Remove on first item in cart."""
    self.page.locator(self.REMOVE_BUTTON).first.click()

def continue_shopping(self):
    """Click continue Shopping button."""
    self.click(self.CONTINUE_SHOPPING)

def proceed_to_checkout(self):
    """Click Checkout button."""
    self.click(self.CHECKOUT_BUTTON)

#-----------Assertions------------