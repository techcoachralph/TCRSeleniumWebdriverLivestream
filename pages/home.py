import time
from seleniumpagefactory import PageFactory


class HomePage(PageFactory):
    def __init__(self, driver):
        self.driver = driver

    locators = {
        "accept_cookies_button": ('XPATH', "//div[@id='cookie-banner']//button[.='Got it']"),
        "delivery_address_input_field": ('ID', "location-typeahead-home-input"),
        "find_food_button": ('XPATH', "//button[.='Find Food']")
    }

    def click_accept_cookies_button(self):
        print("Click Accept cookies button")
        self.accept_cookies_button.click_button()

    def enter_delivery_address(self, address):
        print(f"Enter deliver address: {address}")
        self.delivery_address_input_field.set_text(address)

    def click_find_food_button(self):
        print("Click Find Food")
        self.find_food_button.click_button()

    def search_for_restaurants_based_on_user_entered_delivery_address(self, address):
        self.enter_delivery_address(address)
        time.sleep(5)
        self.click_find_food_button()
