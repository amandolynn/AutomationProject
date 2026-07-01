"""Tests for signup page"""
import requests
from faker import Faker
from playwright.sync_api import expect
from pages.account_info_page import AccountInfoPage
from pages.account_created_page import AccountCreatedPage
from pages.signup_login_page import SignupLoginPage


fake = Faker()

name = fake.first_name()
email = fake.email()


def test_user_can_navigate_to_signup_page(home_page):
    """Verify that the signup page can be opened from the home page."""

    signup = SignupLoginPage(home_page.page)
    home_page.click_signup_login_link()
    expect(signup.new_user_signup_heading()).to_be_visible()


def test_user_can_start_signup_process(home_page, fake_data):
    """Verify that user can start the signup process and reach account information page."""
    signup = SignupLoginPage(home_page.page)
    account_info = AccountInfoPage(home_page.page)

    home_page.click_signup_login_link()

    signup.start_signup(
        fake_data.first_name(),
        fake_data.email()
    )

    expect(account_info.enter_account_information_heading()).to_be_visible()


def test_user_can_create_account(home_page, fake_data):
    """Verify that user can create an account and reach the account created page."""
    account_info = AccountInfoPage(home_page.page)
    account_created = AccountCreatedPage(home_page.page)
    signup = SignupLoginPage(home_page.page)
    first_name = fake_data.first_name()
    password = "Password123!"
    user_email = fake_data.email()
    dob = fake_data.date_of_birth()
    title = fake_data.random_element(elements=("Mr", "Mrs"))
    country = "United States"

    home_page.click_signup_login_link()
    signup.start_signup(first_name, user_email)
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


def test_create_user_api(fake_data):
    """Verify a new user can be created through the API."""

    api_url = "https://automationexercise.com/api/createAccount"

    first_name = fake_data.first_name()
    last_name = fake_data.last_name()
    user_email = fake_data.email()
    password = "Password123!"
    company = fake_data.company()
    address = fake_data.street_address()
    state = fake_data.state()
    city = fake_data.city()
    zipcode = fake_data.postcode()
    mobile = fake_data.phone_number()
    dob = fake_data.date_of_birth()

    payload = {
        "name": f"{first_name} {last_name}",
        "email": user_email,
        "password": password,
        "title": "Mr",
        "birth_date": str(dob.day),
        "birth_month": str(dob.month),
        "birth_year": str(dob.year),
        "firstname": first_name,
        "lastname": last_name,
        "company": company,
        "address1": address,
        "address2": fake_data.secondary_address(),
        "country": "United States",
        "zipcode": zipcode,
        "state": state,
        "city": city,
        "mobile_number": mobile,
    }

    # provide a timeout to avoid hanging indefinitely
    response = requests.post(api_url, data=payload, timeout=10)
    assert response.status_code == 200
    print(response.json())

    assert response.status_code == 200

    data = response.json()

    assert data["responseCode"] == 201
    assert data["message"] == "User created!"
