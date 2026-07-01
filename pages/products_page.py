"""Page object for the products listing page."""


class ProductsPage:
    """Products page elements and actions."""

    def __init__(self, page):
        self.page = page

    def heading(self):
        """Return the page heading locator."""
        return self.page.get_by_role(
            "heading",
            name="All Products"
        )

    def product_cards(self):
        """Return the locator for product cards."""
        return self.page.locator(".product-card")
