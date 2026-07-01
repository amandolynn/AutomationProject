"""Page object for the account information page."""


class HomePage:

    """Represents the home page."""

    def __init__(self, page):
        self.page = page

    def navigate(self):
        """Navigate to the home page."""
        self.page.goto("https://automationexercise.com")

    # Locators

    def logo(self):
        """Return the home page logo element."""
        return self.page.get_by_alt_text(
            "Website for automation practice"
        )

    def signup_login_link(self):
        """Return the signup/login link element."""
        return self.page.get_by_role(
            "link", name="Signup / Login"
        )

    def products_link(self):
        """Return the products link element."""
        return self.page.get_by_role(
            "link", name="Products"
        )

    def contact_us_link(self):
        """Return the contact us link element."""
        return self.page.get_by_role(
            "link", name="Contact us"
        )

    def test_cases_link(self):
        """Return the test cases link element."""
        return self.page.locator(
            "ul.nav.navbar-nav > li > a[href='/test_cases']"
        )

    def home_link(self):
        """Return the home link element."""
        return self.page.get_by_role(
            "link", name="Home"
        )

    def api_testing_link(self):
        """Return the API testing link element."""
        return self.page.locator(
            "ul.nav.navbar-nav > li > a[href='/api_list']"
        )

    def cart_link(self):
        """Return the cart link element."""
        return self.page.get_by_role(
            "link", name="Cart"
        )

    def video_tutorials_link(self):
        """Return the video tutorials link element."""
        return self.page.get_by_role(
            "link", name="Video Tutorials"
        )

    def carousel(self):
        """Return the carousel element."""
        return self.page.locator("#slider")

    # Methods

    def click_products(self):
        """Click the products link and handle Google vignette redirect."""
        self.products_link().click()
        self._handle_google_vignette()

    def _handle_google_vignette(self):
        if "#google_vignette" in self.page.url:
            self.page.go_back()
            self.products_link().click()

    def click_signup_login_link(self):
        """Click the signup/login link."""
        self.signup_login_link().click()
