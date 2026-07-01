"""Pytest fixtures used throughout the test suite."""
import pytest
from playwright.sync_api import sync_playwright
from faker import Faker
from pages.home_page import HomePage


@pytest.fixture
def fake_data():
    """Return a Faker instance."""
    return Faker()


@pytest.fixture
def page():
    """Provide a Playwright browser page instance."""
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        browser_page = browser.new_page()
        yield browser_page
        browser.close()


@pytest.fixture
def home_page(page):
    """Provide a HomePage instance and navigate to the home page."""
    home = HomePage(page)
    home.navigate()
    return home
