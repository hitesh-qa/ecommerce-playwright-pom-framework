from pages.base_page import BasePage
from test_data.data import BASE_URL

class LoginPage(BasePage):
    """Page object for the Login page."""

#------------Locators-------
USERNAME_INPUT = "#user-name"
PASSWORD_INPUT = "#password"
LOGIN_BUTTON = "#login-button"
ERROR_MESSAGE = "[data-test='error']"

#-----------Action-----------
def open(self):
    """Navigate to login page."""
    self.navigate(BASE_URL)

def enter_username(self, username: str):
    """Type username into username field."""
    self.fill(self.USERNAME_INPUT, username)

def enter_password(self, password: str):
    """Type password into password field."""
    self.fill(self.PASSWORD_INPUT, password)

def click_login(self):
    """Click login button."""
    self.click(self.LOGIN_BUTTON)

def login(self, username: str, password: str):
    """Complete login in one step"""
    self.enter_username(username)
    self.enter_password(password)
    self.click_login()

#-----------Assertions------------
def get_error_message(self):
    """Return error message text."""
    return self.get_text(self.ERROR_MESSAGE)

def is_error_visible(self):
    """Check if error message is displayed."""
    return self.is_visible(self.ERROR_MESSAGE)

def is_login_successful(self):
    """Check is login redirected to inventory page."""
    return "inventory" in self.get_current_url()