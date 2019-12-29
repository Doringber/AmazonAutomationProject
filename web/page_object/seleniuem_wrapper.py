from selenium.webdriver.support.wait import WebDriverWait
from termcolor import colored
from amazon.web.page_object.actions import Actions
from amazon.web.page_object.base_class import TestBase
from amazon.web.resources.Locators import Locators
from selenium.webdriver.support import expected_conditions as EC


class SeleniumWrapper(TestBase):
    def __init__(self, driver):
        self.driver = driver

    def click(self, by_locator):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).click()

    def enter_text(self, by_locator, text):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).clear()
        item = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).send_keys(text)
        return item

    def assert_text(self, by_locator, element_text):
        web_element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(by_locator))
        if web_element.text == element_text:
            print("Good")

    def find_element_by_xpath(self,by_locator):
        return self.driver.find_element_by_xpath(by_locator)

    def find_element(self, by_locator):
        return self.driver.find_element(*by_locator)

    def current_url(self):
        return self.driver.current_url


