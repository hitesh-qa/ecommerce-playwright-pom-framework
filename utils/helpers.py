import os
import time
from datetime import datetime

class Helpers:
    """Utility/helper functions for the test framework."""
#------------Screenshot Helpers--------------

@staticmethod
def create_screenshot_name(test_name: str):
    """Generate unique screenshot name with timestamp."""
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    return f"{test_name}_{timestamp}"

@staticmethod
def ensure_screenshots_folder():
    """Create screenshots folder if it doesn't exist."""
    if not os.path.exists("screenshots"):
        os.makedirs("screenshots")
        print("Screenshots folder created")

@staticmethod
def ensure_reports_folder():
    """Create reports folder if it doesn't exist."""
    if not os.path.exists("reports"):
        os.makedirs("reports")
        print("Reports folder created")

#----------wait Helpers-------------------