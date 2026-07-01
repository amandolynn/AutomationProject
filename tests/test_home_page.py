"""Tests for home page"""
import re
from playwright.sync_api import expect
from pages.products_page import ProductsPage


def test_home_page_has_correct_title(home_page):
    """Verify the home page title is correct."""
    expect(home_page.page).to_have_title("Automation Exercise")


def test_home_page_displays_logo(home_page):
    """Verify the home page logo is visible."""
    expect(home_page.logo()).to_be_visible()


def test_signup_login_link_is_visible(home_page):
    """Verify the signup/login link is visible on the home page."""
    expect(home_page.signup_login_link()).to_be_visible()

def test_contact_us_link_is_visible(home_page):
    """Verify the contact us link is visible on the home page."""
    expect(home_page.contact_us_link()).to_be_visible()

def test_test_cases_link_is_visible(home_page):
    """Verify the test cases link is visible on the home page."""
    print(home_page.test_cases_link().count())
    expect(home_page.test_cases_link()).to_be_visible()

def test_products_link_is_visible(home_page):
    """Verify the products link is visible on the home page."""
    expect(home_page.products_link()).to_be_visible()

def test_home_link_is_visible(home_page):
    """Verify the home link is visible on the home page."""
    expect(home_page.home_link()).to_be_visible()

def test_api_testing_link_is_visible(home_page):
    """Verify the API testing link is visible on the home page."""
    print(home_page.api_testing_link().count())
    expect(home_page.api_testing_link()).to_be_visible()

def test_cart_link_is_visible(home_page):
    """Verify the cart link is visible on the home page."""
    expect(home_page.cart_link()).to_be_visible()

def test_video_tutorials_link_is_visible(home_page):
    """Verify the video tutorials link is visible on the home page."""
    expect(home_page.video_tutorials_link()).to_be_visible()

def test_home_page_displays_carousel(home_page):
    """Verify the homepage carousel is visible."""
    expect(home_page.carousel()).to_be_visible()

def test_user_can_navigate_to_products_page(home_page):
    """Verify that the user can navigate from home page to products page."""
    products = ProductsPage(home_page.page)
    home_page.click_products()
    expect(home_page.page).to_have_url(re.compile(r"./products"))
    expect(products.heading()).to_be_visible()
