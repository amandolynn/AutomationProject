"""Page object for the account created page."""

class AccountCreatedPage:
    """Represents the account created page."""

    def __init__(self, page):
        """Initialize the page object."""
        self.page = page
##Locators

    def account_created_heading(self):
        """Return the account created heading locator."""
        return self.page.get_by_text("Account Created!")
    def continue_button(self):
        """Return the continue button locator."""
        return self.page.locator('[data-qa="continue-button"]')


##Methods
    def click_continue(self):
        """Click the continue button."""
        self.continue_button().click()
