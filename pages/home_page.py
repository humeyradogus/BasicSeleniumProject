from selenium.webdriver.common.by import By
from base.base_page import BasePage

class HomePage(BasePage):
    CATEGORY_PAGE_BTN = (By.CSS_SELECTOR, ".menu-header-item__title")

    def __init__(self, driver):
        self.driver = driver
        self.methods = BasePage(self.driver)

    def click_to_erkek_category_btn(self):
        self.find_elements(1, *self.CATEGORY_PAGE_BTN)