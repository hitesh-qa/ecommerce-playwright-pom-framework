from pages.base_page import BasePage

class ProductPage(BasePage):
    """Page object for the Product Detail page."""

#--------------Locators----------
PRODUCT_NAME = ".inventory_details_name"
PRODUCT_PRICE = ".inventory_details_price"
PRODUCT_DESC = ".inventory_details_desc"
PRODUCT_IMAGE = ".inventory_details_img"
ADD_TO_CART_BUTTON = "button[data-test^='add-to-cart']"
REMOVE_BUTTON = "button[data-test^='remove']"
BACK_BUTTON = "#back-to-products"

#------------Actions-------------