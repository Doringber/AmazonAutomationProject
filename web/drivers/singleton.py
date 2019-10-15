from selenium import webdriver
from selenium.webdriver import DesiredCapabilities

from amazon.web.drivers.tests_data import TestData
from amazon.web.drivers.drivers import InitDriver
from amazon.web.page_object.api_actions import ApiActions


class MetaClassSingleton(type):
    """
    Meta class implementation
    """
    _instances = {}

    def __call__(cls, *args, **kwargs):
        """
        Override __call__ special method based on singleton pattern
        """
        if cls not in cls._instances:
            cls._instances[cls] = super(MetaClassSingleton, cls).__call__(*args, **kwargs)

        return cls._instances[cls]


class Driver(metaclass=MetaClassSingleton):
    """
    Driver class decorated by the meta class: MetaClassSingleton.
    Behaviour changed in singleton
    """
    connection = None

    def connect(self):
        """
        Set the connection with the web driver
        :return: web driver
        """
        if self.connection is None:

            if TestData.BROWSER_TYPE.lower() == "chrome":
                self.connection = webdriver.Chrome()
                print(self.connection)
                #
            elif TestData.BROWSER_TYPE.lower() == "firefox":
                cap = DesiredCapabilities().FIREFOX
                cap["marionette"] = False
                self.connection = webdriver.Firefox(capabilities=cap, executable_path=TestData.FIREFOX_EXECUTABLE_PATH)
            elif TestData.BROWSER_TYPE.lower() == "safari":
                self.connection = webdriver.Safari()

            elif TestData.BROWSER_TYPE.lower() == "appium":
                self.connection = InitDriver.appiunSetUp()

            elif TestData.BROWSER_TYPE.lower() == "api":
                self.connection = ApiActions()

            elif TestData.BROWSER_TYPE.lower() == "grid":
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
                    self.connection = self.chrome
                    return self.connection
                else:
                    self.connection = self.firefox
                    return self.connection

            self.connection.get("https://www.amazon.in")
            # self.connection.implicitly_wait(5)
            return self.connection




