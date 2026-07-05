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

@staticmethod
def wait(seconds: int):
    """Pause execution for given seconds."""
    time.sleep(seconds)

#-------------String Helpers--------------
@staticmethod
def extract_price_value(price_str: str):
    """Convert price string to float """
    return float(price_str.replace("$", "").strip())

@staticmethod
def is_price_sorted_low_to_high(prices: list):
    """Check if list of price strings is sorted low ro high."""
    values =[Helpers.extract_price_value(p) for p in prices]
    return values == sorted (values)

@staticmethod
def is_name_sorted_a_to_z(names: list):
    """Check if list of names is sorted A to Z."""
    return names == sorted(names)

#----------------Logging helpers------------

@staticmethod
def log(message: str):
    """Print a formatted log message with timestamp."""
    timestamp = datetime.now().strftime("%H:%M:%S")
    print(f"{timestamp}: {message}")