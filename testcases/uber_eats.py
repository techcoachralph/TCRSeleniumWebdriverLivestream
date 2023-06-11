import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from pages.home import HomePage
from pages.navigation import NavigationPage
from pages.product_page import ProductPage
from pages.restaurant_menu import RestaurantMenu
from pages.results import Results

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

home = HomePage(driver)
results = Results(driver)
menu = RestaurantMenu(driver)
products = ProductPage(driver)
navigation = NavigationPage(driver)

driver.maximize_window()
driver.implicitly_wait(10)
driver.get("http://www.ubereats.com")
home.click_accept_cookies_button()
home.search_for_restaurants_based_on_user_entered_delivery_address("8R37+95 Coconut Creek, Florida")
time.sleep(10)
results.validate_results_page_header()
restaurant_name = results.restaurant_name()
results.click_restaurant()
menu.validate_the_heading_has_correct_text(restaurant_name)
time.sleep(5)
driver.execute_script("window.scrollTo(0,500)")
time.sleep(3)
products.click_product_image()
time.sleep(5)
products.add_item_to_cart()
time.sleep(5)
navigation.validate_item_count_in_cart(1)
