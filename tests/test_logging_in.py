"""Tests for signup page"""
from playwright.sync_api import expect
import requests
from pages.signup_login_page import SignupLoginPage
from pages.account_info_page import AccountInfoPage
from pages.account_created_page import AccountCreatedPage


def test_user_id_logged_in_after_creation(home_page, fake_data):
    """Verify that a registered user is logged in after account creation."""
    account_info = AccountInfoPage(home_page.page)
    account_created = AccountCreatedPage(home_page.page)
    auth = SignupLoginPage(home_page.page)
    first_name = fake_data.first_name()
    password = "Password123!"
    user_email = fake_data.email()
    dob = fake_data.date_of_birth()
    title = fake_data.random_element(elements=("Mr", "Mrs"))
    country = "United States"

    home_page.click_signup_login_link()
    auth.start_signup(first_name, user_email)
    account_info.select_title(title)
    account_info.enter_password(password)
    account_info.select_date_of_birth(dob.day, dob.month, dob.year)
    account_info.fill_personal_details(
        first_name=first_name,
        last_name=fake_data.last_name(),
        company=fake_data.company(),
        address1=fake_data.address(),
        address2=fake_data.address(),
        country=country,
        state=fake_data.state(),
        city=fake_data.city(),
        zipcode=fake_data.zipcode(),
        mobile_number=fake_data.phone_number()
    )
    account_info.click_create_account()
    expect(account_created.account_created_heading()).to_be_visible()
    account_created.click_continue()
    expect(auth.logged_in_user(first_name)).to_be_visible()

def test_registered_user_can_log_in_with_valid_credentials(home_page,fake_data):
    """Verify a registered user can log in with valid credentials."""
    account_info = AccountInfoPage(home_page.page)
    account_created = AccountCreatedPage(home_page.page)
    auth = SignupLoginPage(home_page.page)
    first_name = fake_data.first_name()
    password = "Password123!"
    user_email = fake_data.email()
    dob = fake_data.date_of_birth()
    title = fake_data.random_element(elements=("Mr", "Mrs"))
    country = "United States"

    home_page.click_signup_login_link()
    auth.start_signup(first_name, user_email)
    account_info.select_title(title)
    account_info.enter_password(password)
    account_info.select_date_of_birth(dob.day, dob.month, dob.year)
    account_info.fill_personal_details(
        first_name=first_name,
        last_name=fake_data.last_name(),
        company=fake_data.company(),
        address1=fake_data.address(),
        address2=fake_data.address(),
        country=country,
        state=fake_data.state(),
        city=fake_data.city(),
        zipcode=fake_data.zipcode(),
        mobile_number=fake_data.phone_number()
    )
    account_info.click_create_account()
    expect(account_created.account_created_heading()).to_be_visible()
    account_created.click_continue()
    expect(auth.logged_in_user(first_name)).to_be_visible()
    auth.click_logout()
    expect(auth.login_heading()).to_be_visible()
    auth.login(user_email, password)
    expect(auth.logged_in_user(first_name)).to_be_visible()

def test_verify_login_api():
    """Verify the login API accepts valid credentials."""
    email = "testamanda123@gmail.com"
    password = "Password123!"
    url = "https://automationexercise.com/api/verifyLogin"
    payload = {
    "email": email,
    "password": password,
}
    # provide a timeout to avoid hanging indefinitely
    response = requests.post(url, data=payload, timeout=10)
    assert response.status_code == 200
    print(response.json())

    data = response.json()
    assert data["responseCode"] == 200
    assert data["message"] == "User exists!"
    