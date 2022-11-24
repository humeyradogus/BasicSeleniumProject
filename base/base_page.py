from selenium.webdriver.support.wait import WebDriverWait

class BasePage(object):
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def find_element(self, *locator):
        return self.driver.find_element(*locator)

    def click_element(self, *locator):
        self.find_element(*locator).click()

    def find_elements(self, index, *element):
        self.driver.find_elements(*element)[index].click()
