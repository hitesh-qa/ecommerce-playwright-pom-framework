import pytest
from playwright.sync_api import sync_playwright
from pages.login_page import LoginPage
from pages.home_page import HomePage
from pages.product_page import ProductPage
from pages.cart_page import CartPage
from test_data.data import BASE_URL, BROWSER, HEADLESS

#----------- Browser and Page Fixture ---------------------

@pytest.fixture(scope="session")
def browser_instance():
    """Launch browser once for the entire test session."""
    with sync_playwright() as p
    browser = getattr(p, BROWSER).launch(headless=HEADLESS)
    yield browser
    browser.close()

    @pytest.fixture(scope="function")
    def page(browser_instance):
        """Create a fresh page (new context) for each test."""
        context = browser_instance.new_context()
        page = context.new_page()
        page.goto(BASE_URL)
        yield page
        context.close()

#---------Page Object Fixtures-----------

@pytest.fixture(scope="function")
def login_page(page):
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

#---------------Screenshot on Failure--------------

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        page = item.funcargs.get("page")
        if page:
             screenshots_path = f"screenshots/{item.name}.png"
             page.screenshot(path=screenshots_path)
             print(f"\n Screenshot saved: {screenshots_path}")


# browser_instance -> Launches browser once for all tests
# pytest_runtest_makereport -> Auto screenshot on failure -> saves to/screenshots