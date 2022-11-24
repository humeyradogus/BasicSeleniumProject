import time

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
"""
BASIC SELENIUM PROJECT
"""
class Lcwakiki():
    url = "https://www.lcwaikiki.com/tr-TR/TR"
    CATEGORY_PAGE = (By.CSS_SELECTOR, ".menu-header-item__title")
    CATEGORY_DISCOVER = (By.XPATH, ".//div[contains(@class,'col-sm-12 uzun visible-lg')]")
    PRODUCT_CARD_TITLE = (By.CSS_SELECTOR, ".product-card__title")
    CHOOSE_SIZE = (By.CSS_SELECTOR, "a[data-tracking-label='BedenSecenekleri']")
    PRODUCT_EVALUATION = (By.CSS_SELECTOR, ".pr-button-text")
    CHOOSE_LENGTH = (By.CSS_SELECTOR, "a[data-tracking-label='BoySecenekleri']")
    ADD_CART = (By.CSS_SELECTOR, ".add-to-cart.button-link.add-to-cart-button")
    GO_TO_HOMEPAGE = (By.CSS_SELECTOR, ".main-header-logo")
    CATEGORY_PAGE_FILTER = (By.CSS_SELECTOR, ".quick-filters__heading-text")

    def __init__(self):
        self.driver = webdriver.Chrome("/Users/humeyradogus/PycharmProjects/insiderOtomasyon/chromedriver")
        self.driver.maximize_window()
        option = Options()
        option.add_argument("--disable-infobars")
        option.add_argument("start-maximized")
        option.add_argument("--disable-extensions")
        self.driver.get(self.url)
        self.wait = WebDriverWait(self.driver, 15)

    def test_navigate(self):
        assert self.url == self.driver.current_url, "URL HATASI"
        category_page = self.wait.until(ec.presence_of_all_elements_located(self.CATEGORY_PAGE))[1].text
        self.wait.until(ec.presence_of_all_elements_located(self.CATEGORY_PAGE))[1].click()
        assert category_page == "ERKEK", "KATEGORİ HATASI"
        self.wait.until(ec.presence_of_all_elements_located(self.CATEGORY_DISCOVER))[1].click()
        print("Kategori Sayfası")
        category_page_filter = self.wait.until(ec.presence_of_all_elements_located(self.CATEGORY_PAGE_FILTER))[0].text
        assert category_page_filter == "Hızlı Filtre", "KATEGORİ SAYFASI HATASI"
        self.wait.until(ec.presence_of_all_elements_located(self.PRODUCT_CARD_TITLE))[0].click()
        print("Product Sayfası")
        time.sleep(3)
        product_evaluation = self.wait.until(ec.presence_of_all_elements_located(self.PRODUCT_EVALUATION))[2].text
        assert product_evaluation == "Ürün Değerlendirmeleri", "PRODUCT SAYFASI HATASI"
        time.sleep(1)
        self.wait.until(ec.presence_of_all_elements_located(self.CHOOSE_SIZE))[0].click()
        time.sleep(2)
        self.wait.until(ec.presence_of_all_elements_located(self.CHOOSE_LENGTH))[0].click()
        self.driver.execute_script("window.scrollTo(0, 300)")
        time.sleep(3)
        self.wait.until(ec.presence_of_all_elements_located(self.ADD_CART))[0].click()

        self.wait.until(ec.presence_of_all_elements_located(self.GO_TO_HOMEPAGE))[0].click()
        print("Anasayfa")
        print("Otomasyon Tamamlandı!")

    def tear_down(self):
        self.driver.quit()

def main():
    lcwakiki = Lcwakiki()
    lcwakiki.test_navigate()
    lcwakiki.tear_down()

if __name__ == '__main__':
    main()
