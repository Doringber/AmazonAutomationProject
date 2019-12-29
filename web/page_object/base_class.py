import logging
import unittest


from termcolor import colored
from amazon.web.drivers.tests_data import TestData
from amazon.web.drivers.drivers_ton import OpenUrl

from amazon.web.utilities.logger import Logger

MESSAGE_TEST_START_RUNNING = '\n===============| Test "%s" Started Running |==============='
MESSAGE_TEST_FINISHED_RUNNING = '===============| Test "%s" Finished Running |===============\n'


class TestBase(unittest.TestCase):

    def setUp(self):
        print(colored(MESSAGE_TEST_START_RUNNING % self._testMethodName, "green"))
        self.PATH_SCREENSHOTS = TestData.SCREEN_PATH

        # Boot step 1: Setup logger
        Logger.get_instance().initialization(self)

        # Boot step 2: Open URL
        OpenUrl.open(self)


    def tearDown(self):
        print(colored(MESSAGE_TEST_FINISHED_RUNNING % self._testMethodName, "green"))

        if TestData.BROWSER_TYPE != 'appium' \
                and TestData.BROWSER_TYPE.lower() != 'api':
            self.driver.close()
