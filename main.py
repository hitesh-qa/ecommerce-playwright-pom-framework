import subprocess
import sys

def run_all_test()
    """Run all tests with HTML report"""
    print("\n Running ALL tests...\n")
    subprocess.run([
        sys.executable, "-m", "pytest",
        "test/",
        "--html=report/report.html",
        "--self-contained-html",
        "-v"
    ])

def run_smoke_test():
    """Run only smoke tests."""
    print("\n Running smoke tests...\n")
    subprocess.run([
        "test/",
        "-m", "smoke"
        "--html=reports/smoke_report.html",
        "--self-contained-html"
        "-v"
    ])

def run_regression_test():
    """Run only regression tests."""
    print("\n Running REGRESSION tests...\n")
    subprocess.run([
        sys.executable, "-m", "pytest",
        "test/",
        "-m", "regression",
        "--html=reports/regression_report.html",
        "-v"
    ])

def run_login_test():
    """Run only login tests."""
    print("\n Running LOGIN tests...\n")
    subprocess.run([
        sys.executable, "-m", "pytest",
        "test/test_login.py"
        "--html=reports/login_report.html",
        "--self-contained-html"
        "-v"
    ])

def run_cart_tests():
    """Run only cart tests."""
    print("\n Running CART tests...\n")
    subprocess.run([
        sys.executable, "-m", "pytest",
        "tests/test_cart.py",
        "--html=reports/cart_report.html",
        "--self-contained-html"
        "-v"
    ])

def run_product_tests():
    """Run only product tests."""
    print("\n Running PRODUCT tests...\n")
    subprocess.run([
        sys.executable, "-m", "pytest",
        "tests/test_product.py",
        "--html=reports/product_report.html",
        "-v"
    ])

