import time

from bs4 import BeautifulSoup

from termcolor import colored

from amazon.web.page_object import sql_connection
from amazon.web.page_object.actions import Actions
from amazon.web.resources import csv_reader
from amazon.web.resources.Locators import Locators
from amazon.web.drivers.tests_data import TestData
from amazon.web.resources.csv_reader import CsveReader


class HomePage(Actions):
    """Home Page of Amazon India"""


    def search(self):
        print(colored('Step 1: Clear search box ', 'blue'))
        self.driver.find_element(*Locators.SEARCH_TEXTBOX).clear()

        print(colored('Step 2: Enter text: {} '.format(TestData.SEARCH_TERM), 'blue'))
        self.enter_text(Locators.SEARCH_TEXTBOX, TestData.SEARCH_TERM)

        print(colored('Step 3: Press on submit button ', 'blue'))
        self.click(Locators.SEARCH_SUBMIT_BUTTON)


class SearchResultsPage(Actions):
    """Search Results Page of Amazon India"""

    def __init__(self, driver):
        super().__init__(driver)

    def click_search_result(self):
        self.click(Locators.SEARCH_RESULT_LINK)


class ProductDetailsPage(Actions):
    """Product Details Page for the clicked product on Amazon India"""

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(TestData.BASE_URL)

    def click_add_to_cart_button(self):
        print(colored('Step 1: Tap on the Cart Button ', 'blue'))
        self.click(Locators.ADD_TO_CART_BUTTON)


class SubCartPage(Actions):
    """Sub Cart Page on Amazon India"""

    def __init__(self, driver):
        super().__init__(driver)

    def click_cart_link(self):
        self.click(Locators.CART_LINK)


class CartPage(Actions):
    """Cart Page on Amazon India"""

    def __init__(self, driver):
        super().__init__(driver)

    def add_item_cart(self):
        print(colored('Step 1: Enter text of: {} '.format('pool'), 'blue'))
        self.enter_text(Locators.SEARCH_TEXTBOX, "pool")

        source_page = self.driver.page_source
        soup = BeautifulSoup(source_page, 'lxml')

        links = soup.find_all("span", class_='navFooterDescText')
        listA = []
        for l in links:
            listA.append(l)

        if len(listA) == 9:
            print(colored('     Step 1.1: there is 9 items on the bottom of the website ', 'blue'))

        print(colored('Step 2: Tap on search submbit button ', 'blue'))
        self.click(Locators.SEARCH_SUBMIT_BUTTON)

        print(colored('Step 2: Tap on search submbit button ', 'blue'))
        self.click(Locators.ITEMS_SEARCH_RESULT)
        self.click(Locators.ADD_TO_CART_BUTTON)

    def delete_item(self):
        cartCount = int(self.driver.find_element(*Locators.CART_COUNT).text)
        # print ("Cart Count is"+ str(cartCount))
        if (cartCount < 1):
            print("Cart is empty")
            exit()
        if (self.driver.title.startswith("Amazon.in Shopping Cart")):
            # to delete an item from the Cart
            self.click(Locators.DELETE_ITEM_LINK)
            time.sleep(2)

    def click_proceed_to_checkout_button(self):
        self.click(Locators.PROCEED_TO_CHECKOUT_BUTTON)


class SignInPage(Actions):
    """SignIn Page on Amazon India"""

    def __init__(self, driver):
        super().__init__(driver)

    def sign_in_failed(self):
        login_name = CsveReader.read(self,'/Users/doringber/PycharmProjects/homework/amazon/web/resources/csv_files/login.csv')

        for i in range(4):
            print(colored('Step 1: Click on the sign in button ', 'blue'))
            self.click(Locators.SIGN_IN_HOME_SCREEN_BUTTON)

            print(colored('Step 2: Click on the inner sign in button ', 'blue'))
            self.click(Locators.SIGN_IN_INNER_BUTTON)

            print(colored('Step 3: Enter text to the email filed  ', 'blue'))
            self.enter_text(Locators.USER_EMAIL_OR_MOBIL_NO_TEXTBOX,login_name[i])

            print(colored('Step 4: Press continue button  ', 'blue'))
            self.click(Locators.CONTINUE_BUTTON)
            time.sleep(2)

            print(colored('Step 5: Verify there is error massage', 'blue'))


class ImdbHomePage(Actions):
    """Appium mobile tests"""

    def __init__(self, driver):
        super().__init__(driver)

    def search_text_and_click(self):
        print(colored('Step 1: Tap on Search box ', 'blue'))
        self.click(Locators.IMDB_SEARCH)

        print(colored('Step 2: Enter the text: {}'.format('star wars'), 'blue'))
        self.enter_text(Locators.IMDB_SEARCH_FILED, "star wars")

        time.sleep(5)
        print(colored('Step 3: Verify there is the title: "Star Wars: The Rise of Skywalker" on the screen' ), 'blue')
        self.assert_element_text(self.driver.find_element(*Locators.IMDB_RESULT_SUGGSTION).text, 'Star Wars: The Rise of Skywalker')

        print(colored('Step 4: Click on the movie ', 'blue'))
        self.click(Locators.IMDB_RESULT_SUGGSTION)

        print(colored('Step 5: Verify Movie page is : "Star Wars: The Rise of Skywalker" on the screen"'), 'blue')
        self.assert_element_text(self.driver.find_element(*Locators.IMDB_MOVIE_PAGE_ID).text, 'Star Wars: The Rise of Skywalker')


class SqlText(Actions):
    """Search text from SQL query """

    def __init__(self, driver):
        super().__init__(driver)

    def sql_search_text_pixel(self):

        print(colored('Step 1: Enter text from SQL table - Pixel ', 'blue'))
        self.enter_text(Locators.SEARCH_TEXTBOX, sql_connection.ENTER_TEXT_SQL_PIXEL)

        print(colored('Step 2: Press on submit button ', 'blue'))
        self.click(Locators.SEARCH_SUBMIT_BUTTON)

    def sql_search_text_redmi(self):

        print(colored('Step 1: Enter text from SQL table - redmi ', 'blue'))
        self.enter_text(Locators.SEARCH_TEXTBOX, sql_connection.ENTER_TEXT_SQL_REDMI)

        print(colored('Step 2: Press on submit button ', 'blue'))
        self.click(Locators.SEARCH_SUBMIT_BUTTON)

    def csv_devices_test(self):
        devices = CsveReader.read(self,'/Users/doringber/PycharmProjects/homework/amazon/web/resources/csv_files/devices.csv')
        print(devices)

        for i in range(len(devices)):

            print(colored('Step 1: Enter text from CSV file %s ', 'blue') % devices[i])
            self.enter_text(Locators.SEARCH_TEXTBOX, devices[i])

            print(colored('Step 2: Press on submit button ', 'blue'))
            self.click(Locators.SEARCH_SUBMIT_BUTTON)

            print(colored('Step 3: Verify %s not None ', 'blue') % self.driver.find_element(*Locators.RESULT_SCREEN_SQL).text)
            self.assertIsNotNone(self.driver.find_element(*Locators.RESULT_SCREEN_SQL).text)
            self.driver.execute_script("window.history.go(-1)")


class HoverItems(Actions):
    """Search text from SQL query """

    def __init__(self, driver):
        super().__init__(driver)

    def hover_between_items(self):
        print(colored('Step 1: hover to Today\'s deals ', 'blue'))

        self.select_dropdown(Locators.SELECT, 'Baby')
        time.sleep(3)

        self.hover_to(Locators.ORDERS)
        time.sleep(3)
        self.hover_to(Locators.HOVER_TO)


class KanHomePage(Actions):

    def __init__(self, driver):
        super().__init__(driver)

    def search_home(self):

        print(colored('Step 1: click on search ', 'blue'))
        self.click(Locators.SEARCH_BUTTON)

        print(colored('Step 2: enter text ', 'blue'))
        self.enter_text(Locators.KAN_SEARCH_TEXT_BOX, "ביבי")
        time.sleep(4)




















