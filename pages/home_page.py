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