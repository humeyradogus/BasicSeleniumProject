from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from pages.category_page import CategoryPage
from pages.home_page import HomePage
from pages.product_page import ProductPage

class TestRunLcwaikiki():

    driver = webdriver.Chrome(ChromeDriverManager().install())
    url = "https://www.lcwaikiki.com/tr-TR/TR"
    home_page = HomePage(driver)
    category_page = CategoryPage(driver)
    product_page = ProductPage(driver)

    def navigate_to_home_page(self):

        self.driver.maximize_window()
        option = Options()
        option.add_argument("--disable-infobars")
        option.add_argument("start-maximized")
        option.add_argument("--disable-extensions")
        self.driver.get(self.url)
        self.wait = WebDriverWait(self.driver, 15)

if __name__ == '__main__':
    TestRunLcwaikiki()