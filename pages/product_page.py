from selenium.webdriver.common.by import By
from base.base_page import BasePage

class ProductPage(BasePage):
    CHOOSE_SIZE = (By.CSS_SELECTOR, "a[data-tracking-label='BedenSecenekleri']")
    CHOOSE_LENGTH = (By.CSS_SELECTOR, "a[data-tracking-label='BoySecenekleri']")
    ADD_CART = (By.CSS_SELECTOR, ".add-to-cart.button-link.add-to-cart-button")
    GO_TO_HOMEPAGE = (By.CSS_SELECTOR, ".main-header-logo")

    def __init__(self, driver):
        self.driver = driver
        self.methods = BasePage(self.driver)

    def choose_size(self):
        self.find_elements(0, *self.CHOOSE_SIZE)

    def choose_length(self):
        self.find_elements(0, *self.CHOOSE_LENGTH)

    def add_to_cart(self):
        self.find_elements(0, *self.ADD_CART)

    def go_to_homepage(self):
        self.find_elements(0, *self.GO_TO_HOMEPAGE)
