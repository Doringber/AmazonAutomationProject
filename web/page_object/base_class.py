import logging
import unittest

from termcolor import colored
from amazon.web.drivers.tests_data import TestData
from amazon.web.drivers.singleton_decorator import DriverClass

MESSAGE_TEST_START_RUNNING = '\n===============| Test "%s" Started Running |==============='
MESSAGE_TEST_FINISHED_RUNNING = '===============| Test "%s" Finished Running |===============\n'


class TestBase(unittest.TestCase):

    def setUp(self):
        logging.basicConfig(
            filename=TestData.LOGGING_PATH + self._testMethodName + ".log",
            level=logging.DEBUG)
        print(colored(MESSAGE_TEST_START_RUNNING % self._testMethodName, "green"))
        self.PATH_SCREENSHOTS = TestData.SCREEN_PATH

        if TestData.BROWSER_TYPE.lower() != 'appium' \
                and TestData.BROWSER_TYPE.lower() != 'api':
            self.driver = DriverClass().get_driver()
            self.driver.get(TestData.BASE_URL)
            self.driver.implicitly_wait(5)

    def tearDown(self):
        print(colored(MESSAGE_TEST_FINISHED_RUNNING % self._testMethodName, "green"))
        if TestData.BROWSER_TYPE != 'appium' \
                and TestData.BROWSER_TYPE.lower() != 'api':
            self.driver.close()
