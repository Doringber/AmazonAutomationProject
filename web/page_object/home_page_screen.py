from selenium.webdriver.support.wait import WebDriverWait
from termcolor import colored

from amazon.web.drivers.tests_data import TestData
from amazon.web.page_object.actions import Actions
from amazon.web.page_object.seleniuem_wrapper import SeleniumWrapper
from amazon.web.resources.Locators import Locators
from selenium.webdriver.support import expected_conditions as EC

from amazon.web.utilities.logger import Logger
from amazon.web.utilities.web_scaping import WebScaping


class HomePageTests(SeleniumWrapper):

    def search_text(self):
        Webscaping_item = 'a'
        self.test = SeleniumWrapper

        print(colored('Step 1: Clear search box ', 'blue'))
        self.test.find_element(self, Locators.SEARCH_TEXTBOX).clear()

        from random_word import RandomWords
        r = RandomWords()
        random_words = r.get_random_word()

        print(colored('Step 2: Enter text: %s ', 'blue') % random_words)
        self.test.enter_text(self, Locators.SEARCH_TEXTBOX, random_words)

        print(colored('Step 3: Press on submit button ', 'blue'))
        self.test.click(self, Locators.SEARCH_SUBMIT_BUTTON)

        print(colored('Step 4: Verify WebScaping with %s tag', 'blue') % Webscaping_item)
        self.item = WebScaping.reutrn_data(self,Webscaping_item)
        Logger.get_instance().log_assert(self.item is not None, 'Failed finding button with id %s in screen')


class HomePageLoaded(SeleniumWrapper):
    def test_home_page_loaded_successfully(self):

        self.test = SeleniumWrapper

        print(colored('Step 1: Verify page title %s', 'blue')% TestData.HOME_PAGE_TITLE)
        self.assertIn(TestData.HOME_PAGE_TITLE, self.driver.title)

