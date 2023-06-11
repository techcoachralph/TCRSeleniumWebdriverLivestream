from seleniumpagefactory import PageFactory


class ProductPage(PageFactory):
    def __init__(self, driver):
        self.driver = driver

    locators = {
        'productImage': ('XPATH', "//div[contains(@class,'lazyload-wrapper')][./picture]/following-sibling::div"),
        'addItemToCartButton': ('CSS', 'main#main-content button'),
    }

    def click_product_image(self):
        print("Click on a product image")
        self.productImage.click_button()

    def add_item_to_cart(self):
        print("Click Add item to cart button")
        self.addItemToCartButton.click_button()
