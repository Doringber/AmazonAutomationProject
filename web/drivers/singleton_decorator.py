from selenium import webdriver
from selenium.webdriver import DesiredCapabilities
from singleton_decorator import singleton

from amazon.web.drivers.tests_data import TestData
from amazon.web.drivers.drivers import InitDriver
from amazon.web.page_object.api_actions import ApiActions


class ClassicalSingleton2(object):
    """
    Singleton class based on overriding the __new__ method
    """

    def __new__(cls):
        """
        Override __new__ method to control the obj. creation
        :return: Singleton obj.
        """
        if not hasattr(cls, 'instance'):
            cls.instance = super(ClassicalSingleton2, cls).__new__(cls)

        return cls.instance


@singleton
class DriverClass:
    @staticmethod
    def get_driver():
        """

        :return: Selenium driver
        """
        if TestData.BROWSER_TYPE.lower() == "chrome":
            return webdriver.Chrome()

        elif TestData.BROWSER_TYPE.lower() == "firefox":
            cap = DesiredCapabilities().FIREFOX
            cap["marionette"] = False
            return webdriver.Firefox(capabilities=cap, executable_path=TestData.FIREFOX_EXECUTABLE_PATH)
        elif TestData.BROWSER_TYPE.lower() == "safari":
            return webdriver.Safari()

        elif TestData.BROWSER_TYPE.lower() == "appium":
            return InitDriver.appiunSetUp()

        elif TestData.BROWSER_TYPE.lower() == "api":
            return ApiActions()
