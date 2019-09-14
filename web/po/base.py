import logging
import unittest

from termcolor import colored

from amazon.web.drivers.TestData import TestData
from amazon.web.drivers.drivers import InitDriver

MESSAGE_TEST_START_RUNNING = '\n===============| Test "%s" Started Running |==============='
MESSAGE_TEST_FINISHED_RUNNING = '===============| Test "%s" Finished Running |===============\n'


class TestBase(unittest.TestCase):

    def setUp(self):
        logging.basicConfig(
            filename="/Users/doringber/PycharmProjects/homework/amazon/web/reports/logs/" + self._testMethodName + ".log",
            level=logging.DEBUG)
        print(colored(MESSAGE_TEST_START_RUNNING % self._testMethodName, "green"))
        driver = InitDriver.initChrome(self)
        InitDriver.initFirefox(self)
        InitDriver.initSafari(self)
        InitDriver.initAppium(self)
        InitDriver.initAPI(self)
        InitDriver.initGrid(self)

        self.PATH_SCREENSHOTS = '/Users/doringber/PycharmProjects/homework/amazon/web/reports/screenshots'
        self.driver = driver
        if TestData.BROWSER_TYPE.lower() != 'appium' and TestData.BROWSER_TYPE.lower() != 'api':
            self.driver.get(TestData.BASE_URL)
            self.driver.implicitly_wait(5)
            self.driver.delete_all_cookies()
        else:
            print("The tests are set on Appuim or API")

    def tearDown(self):
        print(colored(MESSAGE_TEST_FINISHED_RUNNING % self._testMethodName, "green"))
        if TestData.BROWSER_TYPE != 'appium' and TestData.BROWSER_TYPE.lower() != 'api':
            self.driver.close()
