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