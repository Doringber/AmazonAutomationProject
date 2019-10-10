from selenium import webdriver
from selenium.webdriver import DesiredCapabilities
from appium import webdriver as appiumWebriver
from selenium.webdriver.chrome.options import Options

from amazon.web.drivers.tests_data import TestData
from amazon.web.page_object.api_actions import ApiActions

class ClassicalSingleton(object):
    """
    Singleton class based on overriding the __new__ method
    """

    def __new__(cls):
        """
        Override __new__ method to control the obj. creation
        :return: Singleton obj.
        """
        if not hasattr(cls, 'instance'):
            cls.instance = super(ClassicalSingleton, cls).__new__(cls)

        return cls.instance

# @staticmethod
# def get_driver():
#     """
#
#     :return: Selenium driver
#     """
#     return webdriver.Chrome()



class InitDriver(object):

    def initChrome(self):
        if TestData.BROWSER_TYPE.lower() == "chrome":
            self.driver = webdriver.Chrome()
            return self.driver

    def initFirefox(self):
        if TestData.BROWSER_TYPE.lower() == "firefox":
            cap = DesiredCapabilities().FIREFOX
            cap["marionette"] = False
            self.driver = webdriver.Firefox(capabilities=cap, executable_path=TestData.FIREFOX_EXECUTABLE_PATH)
            return self.driver

    def initSafari(self):
        if TestData.BROWSER_TYPE.lower() == "safari":
            self.driver = webdriver.Safari()
            return self.driver

    def initAppium(self):
        if TestData.BROWSER_TYPE.lower() == "appium":
            self.driver = InitDriver.appiunSetUp(self)

    def appiunSetUp(self):
        self.dc = {}
        self.dc['udid'] = TestData.UDID
        self.dc['platformName'] = TestData.PLATFORM_NAME
        self.dc['deviceName'] = TestData.DEVICE_NAME
        self.dc['appActivity'] = TestData.APP_ACTIVITY
        self.dc['appPackage'] = TestData.APP_PACKAGE
        self.dc['noReset'] = TestData.NO_RESET
        self.dc['autoAcceptAlerts'] = TestData.AUTO_ACCEPET_ALERTS
        self.driver = appiumWebriver.Remote(TestData.SERVER, self.dc)
        return self.driver

    def initAPI(self):
        if TestData.BROWSER_TYPE.lower() == "api":
            self.driver = ApiActions()
            return self.driver

    def initGrid(self):
        if TestData.BROWSER_TYPE.lower() == "grid":
            bro = "firefox"

            # desiredCapabilities = {
            #     "browserName": "chrome"
            # }
            #
            # self.driver = webdriver.Remote(command_executor='http://localhost:4446/wd/hub',
            #                           desired_capabilities=desiredCapabilities)

            # desiredCapabilities = {
            #     "browserName": "firefox"
            # }
            #
            # self.driver = webdriver.Remote(command_executor='http://localhost:4446/wd/hub',
            #                                desired_capabilities=desiredCapabilities)

            self.chrome = webdriver.Remote(
                command_executor='http://localhost:4446/wd/hub',
                desired_capabilities=DesiredCapabilities.CHROME)
            self.firefox = webdriver.Remote(
                command_executor='http://localhost:4446/wd/hub',
                desired_capabilities=DesiredCapabilities.FIREFOX)

            if bro == "chrome":
                self.driver = self.chrome
                return self.driver
            else:
                self.driver = self.firefox
                return self.driver
