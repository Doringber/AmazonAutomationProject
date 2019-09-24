import logging
from datetime import datetime

from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from amazon.web.po.base import TestBase


class Actions(TestBase):
    def __init__(self, driver):
        self.driver = driver

    # this function performs click on web element whose locator is passed to it.
    def click(self, by_locator):
        try:
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).click()
            logging.debug("Element with locator was clicked")
        except Exception as error:
            name = str(self.driver.title)
            now = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
            self.driver.get_screenshot_as_file('/Users/doringber/PycharmProjects/homework/amazon/web/reports/screenshots/screenshot-%s_%s.png' % (now, name))
            logging.error(
                'Could not do the click on locator %s was click and this is the error %s' % (by_locator, error))

    def assert_element_text(self, by_locator, element_text):
        """Need to fix this fun"""
        try:
            web_element = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(by_locator))
            if web_element.text == element_text:
                logging.debug("Element with locator %s was enter text: %s" % by_locator)
        except Exception as error:
            # self.take_screenShot()
            logging.error('Element with locator: %s was not assert %s' % (by_locator, error))

    def enter_text(self, by_locator, text):
        try:
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).clear()
            item = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).send_keys(text)
            logging.debug("Element with locator %s was enter text:  %s" % (by_locator, text))
            return item
        except Exception as error:
            name = str(self.driver.title)
            now = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
            self.driver.get_screenshot_as_file(self.PATH_SCREENSHOTS + '/screenshot-%s_%s.png' % (now, name))
            logging.error('Element with locator:  %s was not enter text:  %s' % by_locator % error)

    # this function checks if the web element whose locator has been passed to it, is enabled or not and returns
    # web element if it is enabled.
    def is_enabled(self, by_locator):
        try:
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
            logging.debug("Item is enabled with locator %s " % by_locator)
        except Exception as error:
            logging.error('Item is not enabled %s' % error)

    # this function checks if the web element whose locator has been passed to it, is visible or not and returns
    # true or false depending upon its visibility.
    def is_visible(self, by_locator):
        try:
            element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
            logging.debug("Item is visible with locator %s " % by_locator)
            return bool(element)
        except Exception as error:
            logging.error('Item is not enabled %s' % error)

    # this function moves the mouse pointer over a web element whose locator has been passed to it.
    def hover_to(self, by_locator):
        try:
            element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
            ActionChains(self.driver).move_to_element(element).perform()
            logging.debug("Item is doing hover to  %s " % by_locator)
        except Exception as error:
            logging.error('Item is not enabled %s' % error)

    def driver_source_page(self):
        pass
