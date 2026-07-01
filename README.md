# Playwright Automation Framework

A UI and API automation framework built with **Python**, **Playwright**, **Pytest**, and the **Page Object Model (POM)**. This project uses the public practice site Automation Exercise to demonstrate end-to-end web automation, API testing, and maintainable test design.

## Technologies

- Python 3.11
- Playwright
- Pytest
- Requests
- Faker
- Page Object Model (POM)

## Features

### UI Automation
- Home page verification
- Navigation testing
- User signup
- User login
- Account creation
- Dynamic test data using Faker
- Reusable page objects and fixtures

### API Automation
- Verify Login API (`POST /api/verifyLogin`)
- Create User API (`POST /api/createAccount`)
- HTTP status code validation
- JSON response validation

## Project Structure

AutomationProject/
│
├── pages/
│   ├── account_created_page.py
│   ├── account_info_page.py
│   ├── home_page.py
│   ├── products_page.py
│   └── signup_login_page.py
│
├── tests/
│   ├── test_home_page.py
│   ├── test_login.py
│   └── test_signup.py
│
├── conftest.py
├── requirements.txt
├── README.md
└── .gitignore

## Test Coverage

Current automated scenarios include:

### Home Page
- Verify page title
- Verify logo is visible
- Verify navigation links are visible
- Navigate to Signup/Login page

### Signup
- Navigate to Signup page
- Start signup process
- Create a new account using generated test data

### Login
- Login with valid credentials
- Verify the user is logged in

### API Tests
- Verify Login API
- Create User API

## Running the Tests

Install dependencies:

```bash
pip install -r requirements.txt
```

Install Playwright browsers:

```bash
playwright install
```

Run all tests:

```bash
pytest
```

Run a specific test file:

```bash
pytest tests/test_signup.py
```

Show print statements during execution:

```bash
pytest -s
```

## Design Principles

This framework follows the Page Object Model to improve readability, maintainability, and reusability.

Features include:

- Page Objects for UI interactions
- Reusable Pytest fixtures
- Dynamic test data with Faker
- Separation of locators and page actions
- API testing using the Requests library
- Clear test organization by feature

## Website Under Test

https://automationexercise.com

This public website is designed specifically for practicing UI and API automation.

## Future Improvements

- Product search automation
- Cart functionality
- Checkout flow
- Negative login scenarios
- Additional API coverage
- GitHub Actions CI/CD pipeline
- HTML test reporting

---

Created as a personal automation project to strengthen QA Automation skills using Python and Playwright.
