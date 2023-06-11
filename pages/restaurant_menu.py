from seleniumpagefactory import PageFactory


class RestaurantMenu(PageFactory):
    def __init__(self, driver):
        self.driver = driver

    locators = {
        'menuTitle': ('CSS', "h1[data-testid='store-title-summary']"),
        'productImageLink': ('XPATH', "//div[contains(@class,'lazyload-wrapper')][./picture]/following-sibling::div")
    }

    def validate_the_heading_has_correct_text(self, restaurant_name):
        menu_title = self.menuTitle.get_text()
        assert menu_title == f"{restaurant_name}", \
            f"Expected: {restaurant_name}\n" \
            f"Actual: {menu_title}"
