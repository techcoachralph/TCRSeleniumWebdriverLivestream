from seleniumpagefactory import PageFactory


class Results(PageFactory):
    def __init__(self, driver):
        self.driver = driver
        self.timeout = 15
        self.highlight = True

    locators = {
        'pageHeading': ('CSS', 'main h1'),
        'secondRestaurantInResults':
            ('XPATH', "(//li[@data-testid='carousel-slide']//a[@data-testid='store-card']//h3)[2]")
    }

    def validate_results_page_header(self):
        page_heading = self.pageHeading.get_text()
        assert page_heading == "All stores", \
            "Expected: All stores\n" \
            f"Actual: {page_heading}"

    def restaurant_name(self):
        return self.secondRestaurantInResults.get_text()

    def click_restaurant(self):
        self.secondRestaurantInResults.click_button()
