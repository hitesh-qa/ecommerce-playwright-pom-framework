import pytest
from test_data.data import(
VALID_USERNAME, VALID_PASSWORD,
INVALID_USERNAME, INVALID_PASSWORD,
LOCKED_USER,LOGIN_ERROR_MSG, LOCKED_ERROR_MSG
)

class TestLogin:
    """Test cases for login functionality."""

#------------Smoke Tests----------------
@pytest.mark.smoke
@pytest.mark.login
def test_valid_login(self, login_page):
    """Test login with valid credentials."""
    login_page.open()
    login_page.login(VALID_USERNAME, VALID_PASSWORD)
    assert login_page.is_login_successful(), \
    "Login failed - inventory page not loaded"

@pytest.mark.smoke
@pytest.mark.login
def test_invalid_login(self, login_page):
    """Test login with invalid credentials shows error."""
    login_page.open()
    login_page.login(INVALID_USERNAME, INVALID_PASSWORD)
    assert login_page.is_error_visible(), \
        "Error message not displayed"
    assert LOGIN_ERROR_MSG in login_page.get_error_message(), \
        "Wrong error message displayed"

#--------------Regression Tests---------------

@pytest.mark.regression
@pytest.mark.login
def test_locked_out_user(self, login_page):
    """Test locked out user sees correct error."""
    login_page.open()
    login_page.login(LOCKED_USER, VALID_PASSWORD)
    assert login_page.is_error_visible(), \
        "Error message not displayed for locked user."
    assert LOCKED_ERROR_MSG in login_page.get_error_message(), \
        "Wrong error message for locked user."
