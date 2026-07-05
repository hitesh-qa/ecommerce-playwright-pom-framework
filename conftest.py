import pytest
from pages.login_page import LoginPage
from pages.home_page import HomePage
from pages.product_page import ProductPage
from pages.cart_page import CartPage
from test_data.data import BASE_URL


# ─── Page Object Fixtures ──────────────────────────────────────────────────────

@pytest.fixture(scope="function")
def login_page(page):
    page.goto(BASE_URL)
    return LoginPage(page)


@pytest.fixture(scope="function")
def home_page(page):
    return HomePage(page)


@pytest.fixture(scope="function")
def product_page(page):
    return ProductPage(page)


@pytest.fixture(scope="function")
def cart_page(page):
    return CartPage(page)


# ─── Screenshot on Failure ─────────────────────────────────────────────────────

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    if report.when == "call" and report.failed:
        page = item.funcargs.get("page")
        if page:
            screenshot_path = f"screenshots/{item.name}.png"
            page.screenshot(path=screenshot_path)
            print(f"\n📸 Screenshot saved: {screenshot_path}")