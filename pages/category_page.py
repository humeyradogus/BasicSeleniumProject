from selenium.webdriver.common.by import By
from base.base_page import BasePage

class CategoryPage(BasePage):

    CATEGORY_DISCOVER = (By.XPATH, ".//div[contains(@class,'col-sm-12 uzun visible-lg')]")
    PRODUCT_CARD_TITLE = (By.CSS_SELECTOR, ".product-card__title")

    def __init__(self, driver):
        self.driver = driver
        self.methods = BasePage(self.driver)

    def click_to_category_banner(self):
        self.find_elements(1, *self.CATEGORY_DISCOVER)

    def click_to_product(self):
        self.find_elements(0, *self.PRODUCT_CARD_TITLE)



