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