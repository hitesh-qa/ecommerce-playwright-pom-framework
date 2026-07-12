# E-Commerce Playwright Automation Framework

A complete test automation framework for e-commerce web application using Playwright + Python + pytest with Page Object Model (POM) design pattern.

## 🛠️ Tech Stack

- **Playwright** - Browser automation
- **Python** - Programming language
- **pytest** - Test framework
- **Page Object Model** - Design pattern
- **pytest-html** - HTML test reports

## 📁 Project Structure

ecommerce-playwright-pom-framework/
├── pages/
│   ├── base_page.py        # Base class with common methods
│   ├── login_page.py       # Login page object
│   ├── home_page.py        # Home/inventory page object
│   ├── product_page.py     # Product detail page object
│   └── cart_page.py        # Cart page object
├── tests/
│   ├── test_login.py       # 6 login test cases
│   ├── test_products.py    # 7 product test cases
│   └── test_cart.py        # 7 cart test cases
├── test_data/
│   └── data.py             # Test data and config
├── utils/
│   └── helpers.py          # Utility functions
├── conftest.py             # pytest fixtures
├── main.py                 # Test runner with menu
└── pytest.ini              # pytest configuration

## ⚙️ Setup & Installation

**1. Clone the repository**

git clone https://github.com/hitesh-qa/ecommerce-playwright-pom-framework.git
cd ecommerce-playwright-pom-framework

**2. Install dependencies**

pip install -r requirements.txt

**3. Install Playwright browsers**

playwright install

## 🚀 How to Run Tests

**Run with interactive menu:**

python main.py

**Run all tests directly:**

python -m pytest tests/ -v

**Run by marker:**

python -m pytest tests/ -m smoke -v
python -m pytest tests/ -m regression -v
python -m pytest tests/ -m login -v

## 🧪 Test Cases

| Module | Tests | Markers |
|--------|-------|---------|
| Login | 6 tests | smoke, regression |
| Products | 7 tests | smoke, regression |
| Cart | 7 tests | smoke, regression |
| **Total** | **20 tests** | |

## ✅ Test Results

- **20/20 tests passing**
- HTML report generated at reports/report.html
- Screenshots captured on test failure

## Framework Features

- **Page Object Model** - Separate page classes for maintainability
- **Reusable fixtures** - conftest.py with shared browser and page setup
- **Test markers** - Run smoke or regression tests separately
- **Auto screenshots** - Captures screenshot on every test failure
- **HTML reports** - Detailed test execution reports
- **Test data module** - Centralized test data in test_data/data.py

## Key Concepts Demonstrated
- Playwright browser automation with python
- POM design pattern implementation
- pytest fixtures and conftest
- Centralized test data management
- Smoke and regression test separation 
- Screenshot capture on failure

## 🌐 Application Under Test

[SauceDemo](https://www.saucedemo.com) - A demo e-commerce application used for automation practice.