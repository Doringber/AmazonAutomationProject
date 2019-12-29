from selenium import webdriver
from selenium.webdriver import DesiredCapabilities
from singleton_decorator import singleton
from amazon.web.drivers.tests_data import TestData


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
    def get_driver(self):
        """
        :return: Selenium driver
        """
        self.driver_instance = ClassicalSingleton2()
        if self.driver_instance is not None:

            if TestData.BROWSER_TYPE.lower() == "chrome":
                return webdriver.Chrome()

            elif TestData.BROWSER_TYPE.lower() == "firefox":
                cap = DesiredCapabilities().FIREFOX
                cap["marionette"] = False
                return webdriver.Firefox(capabilities=cap, executable_path=TestData.FIREFOX_EXECUTABLE_PATH)
            elif TestData.BROWSER_TYPE.lower() == "safari":
                return webdriver.Safari()

            elif TestData.BROWSER_TYPE.lower() == "appium":
                    self.dc = {}
                    self.dc['udid'] = TestData.UDID
                    self.dc['platformName'] = TestData.PLATFORM_NAME
                    self.dc['deviceName'] = TestData.DEVICE_NAME
                    self.dc['appActivity'] = TestData.APP_ACTIVITY
                    self.dc['appPackage'] = TestData.APP_PACKAGE
                    self.dc['noReset'] = TestData.NO_RESET
                    self.dc['autoAcceptAlerts'] = TestData.AUTO_ACCEPET_ALERTS
                    self.driver = webdriver.Remote(TestData.SERVER, self.dc)
                    return self.driver

            elif TestData.BROWSER_TYPE.lower() == "api":
                return True
            else:
                raise Exception('There was problem with your driver')
        else:
            raise Exception("More then one webdriver")


class OpenUrl:
    def __init__(self):
        super().__init__(DriverClass)

    def open(self):
        if TestData.BROWSER_TYPE.lower() is 'api':
            return True

        elif TestData.BROWSER_TYPE.lower() is not 'appium':
            self.driver = DriverClass().get_driver()
            self.driver.get(TestData.BASE_URL)
            self.driver.maximize_window()
            self.driver.implicitly_wait(5)

        elif TestData.BROWSER_TYPE.lower() is 'appium':
            pass

        else:
            raise Exception('Not able to open driver url with %s ' % self.driver)

    def init_api(self):
        if TestData.BROWSER_TYPE.lower( ) is 'api':
            return True

    def init_appium(self):
        if TestData.BROWSER_TYPE.lower( ) is 'appium':
            print("appium blaaaa")
