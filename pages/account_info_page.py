"""Page object for the account information page."""


class AccountInfoPage:
    """Represents the account information page."""

    def __init__(self, page):
        """Initialize the page object."""
        self.page = page
# Locators

    def enter_account_information_heading(self):
        """Return the heading element for entering account information."""
        return self.page.get_by_text("Enter Account Information")

    def title_mr_radio(self):
        """Return the 'Mr' title radio input locator."""
        return self.page.locator("#id_gender1")

    def title_mrs_radio(self):
        """Return the 'Mrs' title radio input locator."""
        return self.page.locator("#id_gender2")

    def password_input(self):
        """Return the password input locator."""
        return self.page.locator('[data-qa="password"]')

    def day_dropdown(self):
        """Return the day dropdown locator."""
        return self.page.locator('[data-qa="days"]')

    def month_dropdown(self):
        """Return the month dropdown locator."""
        return self.page.locator('[data-qa="months"]')

    def year_dropdown(self):
        """Return the year dropdown locator."""
        return self.page.locator('[data-qa="years"]')

    def first_name_input(self):
        """Return the first name input locator."""
        return self.page.locator('[data-qa="first_name"]')

    def last_name_input(self):
        """Return the last name input locator."""
        return self.page.locator('[data-qa="last_name"]')

    def company_input(self):
        """Return the company input locator."""
        return self.page.locator('[data-qa="company"]')

    def address1_input(self):
        """Return the address input locator."""
        return self.page.locator('[data-qa="address"]')

    def address2_input(self):
        """Return the address2 input locator."""
        return self.page.locator('[data-qa="address2"]')

    def country_dropdown(self):
        """Return the country dropdown locator."""
        return self.page.locator('[data-qa="country"]')

    def state_input(self):
        """Return the state input locator."""
        return self.page.locator('[data-qa="state"]')

    def city_input(self):
        """Return the city input locator."""
        return self.page.locator('[data-qa="city"]')

    def zipcode_input(self):
        """Return the zipcode input locator."""
        return self.page.locator('[data-qa="zipcode"]')

    def mobile_number_input(self):
        """Return the mobile number input locator."""
        return self.page.locator('[data-qa="mobile_number"]')

    def create_account_button(self):
        """Return the create account button locator."""
        return self.page.locator('[data-qa="create-account"]')


# Methods


    def select_title(self, title):
        """Select the title radio button based on the provided title."""
        title = title.lower()

        if title == "mr":
            self.title_mr_radio().check()
        elif title == "mrs":
            self.title_mrs_radio().check()
        else:
            raise ValueError("Title must be 'Mr' or 'Mrs'.")

    def enter_password(self, password):
        """Enter the password in the password input field."""
        self.password_input().fill(password)

    def select_date_of_birth(self, day, month, year):
        """Select the date of birth from the dropdowns."""
        self.day_dropdown().select_option(str(day))
        self.month_dropdown().select_option(str(month))
        self.year_dropdown().select_option(str(year))

    def fill_personal_details(
                self, first_name, last_name, company, address1, address2,
                country, state, city, zipcode, mobile_number
            ):
        """Fill in the personal details form."""
        self.first_name_input().fill(first_name)
        self.last_name_input().fill(last_name)
        self.company_input().fill(company)
        self.address1_input().fill(address1)
        self.address2_input().fill(address2)
        self.country_dropdown().select_option(country)
        self.state_input().fill(state)
        self.city_input().fill(city)
        self.zipcode_input().fill(zipcode)
        self.mobile_number_input().fill(mobile_number)

    def click_create_account(self):
        """Click the create account button."""
        self.create_account_button().click()
