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
