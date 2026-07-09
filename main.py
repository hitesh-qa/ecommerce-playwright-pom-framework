import subprocess
import sys
import os

def run_tests(args):
    cmd = [sys.executable, "-m", "pytest"] + args
    subprocess.run(cmd, cwd=os.getcwd())

def run_all_tests():
    print("\n🚀 Running ALL tests...\n")
    run_tests(["tests/", "--html=reports/report.html", "--self-contained-html", "--headed", "-v"])

def run_smoke_tests():
    print("\n💨 Running SMOKE tests...\n")
    run_tests(["tests/", "-m", "smoke", "--headed", "-v"])

def run_regression_tests():
    print("\n🔁 Running REGRESSION tests...\n")
    run_tests(["tests/", "-m", "regression", "--headed", "-v"])

def run_login_tests():
    print("\n🔐 Running LOGIN tests...\n")
    run_tests(["tests/test_login.py", "--headed", "-v"])

def run_cart_tests():
    print("\n🛒 Running CART tests...\n")
    run_tests(["tests/test_cart.py", "--headed", "-v"])

def run_product_tests():
    print("\n📦 Running PRODUCT tests...\n")
    run_tests(["tests/test_products.py", "--headed", "-v"])

if __name__ == "__main__":
    print("=" * 50)
    print("   E-Commerce Playwright Automation Framework")
    print("=" * 50)
    print("\nSelect test suite to run:")
    print("  1 - All Tests")
    print("  2 - Smoke Tests")
    print("  3 - Regression Tests")
    print("  4 - Login Tests")
    print("  5 - Cart Tests")
    print("  6 - Product Tests")
    print()

    choice = input("Enter choice (1-6): ").strip()

    if choice == "1":
        run_all_tests()
    elif choice == "2":
        run_smoke_tests()
    elif choice == "3":
        run_regression_tests()
    elif choice == "4":
        run_login_tests()
    elif choice == "5":
        run_cart_tests()
    elif choice == "6":
        run_product_tests()
    else:
        print("❌ Invalid choice!")