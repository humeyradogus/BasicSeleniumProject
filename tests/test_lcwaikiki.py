import time
import unittest
from selenium.webdriver.common.by import By
from tests.test_run_lcwaikiki import TestRunLcwaikiki

class TestLcwaikiki(unittest.TestCase, TestRunLcwaikiki):

    def setUp(self):
        TestRunLcwaikiki.__init__(self)

    def test_lcwaikiki(self):
        print("\nOtomasyon Başladı!")
        test = TestLcwaikiki()
        test.navigate_to_home_page()
        self.assertEqual(self.driver.current_url, "https://www.lcwaikiki.com/tr-TR/TR", "URL Hatası")
        self.home_page.click_to_erkek_category_btn()
        category_page = self.driver.find_elements(By.CSS_SELECTOR, ".menu-header-item__title")[1].text
        self.assertEqual(category_page, "ERKEK", "KATEGORİ HATASI")
        print("Kategori Sayfası")
        self.category_page.click_to_category_banner()
        category_page_filter = self.driver.find_elements(By.CSS_SELECTOR, ".quick-filters__heading-text")[0].text
        self.assertEqual(category_page_filter, "Hızlı Filtre", "KATEGORİ SAYFASI HATASI")
        self.category_page.click_to_product()
        time.sleep(3)

        product_evaluation = self.driver.find_elements(By.CSS_SELECTOR, ".pr-button-text")[2].text
        self.assertEqual(product_evaluation, "Ürün Değerlendirmeleri", "PRODUCT SAYFASI HATASI")
        print("Product Sayfası")
        time.sleep(1)
        self.product_page.choose_size()
        time.sleep(2)
        self.product_page.choose_length()
        self.driver.execute_script("window.scrollTo(0, 300)")
        time.sleep(3)
        self.product_page.add_to_cart()
        self.product_page.go_to_homepage()

        print("Anasayfa")
        print("Otomasyon Tamamlandı!")

    def tear_down(self):
        self.driver.quit()
