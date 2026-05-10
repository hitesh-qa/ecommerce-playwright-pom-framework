from playwright.sync_api import Page

class  BasePage:
    """Base class for all page objects - contains common methods."""

    def __init__(self, page:Page):
        self.page = page

#----------------Navigation---------------
def navigate(self, url:str):
    """Go to a specific URL"""
        self.page.goto(url)

def get_title(self):
        """Return current page title."""
        return self.page.title()

def get_title(self):
    """Return current page title."""
    return self.page.title()

#------------Element Action-------------
def click(self, locator:str):
    """Click an element."""
    self.page.locator(locator).click()

def fill(self, locator:str, text:str):
    """type text into an input field."""
    self.page.locator(locator).fill(text)

def get_text(self, locator:str):
    """Get text content of an element."""
    return self.page.locator(locator).text_content()

def is_visible(self, locator:str):
    """Check if element is visible."""
    return self.page.locator(locator).is_visible()

#-----------wait Methods------------
def wait_for_element(self, locator:str):
    """Wait for an element to appear."""
    self.page.locator(locator).wait_for(state="visible")

def wait_for_url(self, url:str):
    """Wait until page URL matches."""
    self.page.wait_for_url(url)

#-----------Screenshot---------
def take_screenshot(self, name: str):
    """Take a screenshot and save to screenshot folder."""
    self.page.screenshot(path=f"screenshots/{name}.png")
    print(f" Screenshot saved: screenshot/{name}.png")