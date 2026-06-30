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

