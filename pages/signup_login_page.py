"""Signup/login page object model."""


class SignupLoginPage:
    """Page object for the signup page."""

    def __init__(self, page):
        self.page = page

# Locators
    def new_user_signup_heading(self):
        """Get the new user signup heading element."""
        return self.page.get_by_text("New User Signup!")

    def name_input(self):
        """Get the signup name input element."""
        return self.page.locator('input[data-qa="signup-name"]')

    def email_input(self):
        """Get the signup email input element."""
        return self.page.locator('input[data-qa="signup-email"]')

    def signup_button(self):
        """Get the signup button element."""
        return self.page.locator('button[data-qa="signup-button"]')

    def login_heading(self):
        """Get the login heading element."""
        return self.page.get_by_text("Login to your account")

    def login_email_input(self):
        """Get the login email input element."""
        return self.page.locator('input[data-qa="login-email"]')

    def login_password_input(self):
        """Get the login password input element."""
        return self.page.locator('input[data-qa="login-password"]')

    def login_button(self):
        """Get the login button element."""
        return self.page.locator('button[data-qa="login-button"]')
    def logged_in_user(self, first_name):
        """Get the logged-in user element."""
        return self.page.get_by_text(f"Logged in as {first_name}")

    def logout_link(self):
        """Get the logout link element."""
        return self.page.get_by_text("Logout")


# Methods


    def start_signup(self, name, email):
        """Fill signup fields and submit the signup form."""
        self.name_input().fill(name)
        self.email_input().fill(email)
        self.signup_button().click()
        self.page.locator("#id_gender1").wait_for(state="visible")

    def login(self, email, password):
        """Fill login fields and submit the login form."""
        self.login_email_input().fill(email)
        self.login_password_input().fill(password)
        self.login_button().click()

    def click_logout(self):
        """Click the logout link."""
        self.logout_link().click()
