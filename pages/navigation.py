from seleniumpagefactory import PageFactory


class NavigationPage(PageFactory):
    def __init__(self, driver):
        self.driver = driver

    locators = {
        'shoppingCartIconInHeader': ('CSS', "button[data-test='cart-btn']"),
        'loginButtonInHeader': ('XPATH', "//a[@data-test='header-sign-in'][.='Log in']"),
        'signUpButtonInHeader': ('XPATH', "//a[@data-test='header-sign-in'][.='Sign up']")
    }

    def click_cart_icon_in_header(self):
        print("Click Cart icon in header")
        self.shoppingCartIconInHeader.click_button()

    def click_login_link_in_header(self):
        print("Click Log in link in header")
        self.loginButtonInHeader.click_button()

    def click_sign_up_button_in_header(self):
        print("Click Sign Up button in header")
        self.signUpButtonInHeader.click_button()

    def validate_item_count_in_cart(self, item_count_in_cart):
        cart_button = self.shoppingCartIconInHeader.get_text()
        assert cart_button == f"Cart • {item_count_in_cart}", \
            f"Expected: Cart  •  {item_count_in_cart}\n" \
            f"Actual: {cart_button}"
