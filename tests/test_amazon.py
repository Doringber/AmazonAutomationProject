import unittest

import pytest

from amazon.web.po.api_actions import ApiActions
from amazon.web.po.base import TestBase
from amazon.web.resources.Locators import Locators
from amazon.web.drivers.TestData import TestData
from amazon.web.po.Pages import SignInPage, \
    SqlText, HoverItems, CartPage, ImdbHomePage


class TestAMZNSearch(TestBase):
    def setUp(self):
        # to call the setUp() method of base class or super class.
        super().setUp()

    # def test_home_page_loaded_successfully(self):
    #     # instantiate an object of HomePage class. Remember when the constructor of HomePage class is called
    #     # it opens up the browser and navigates to Home Page of the site under test.
    #     self.homePage = HomePage(self.driver)
    #     # assert if the title of Home Page contains Amazon.in
    #     self.assertIn(TestData.HOME_PAGE_TITLE, self.homePage.driver.title)
    #
    # def test_home_search_filed(self):
    #     self.homePage = HomePage(self.driver)
    #     self.homePage.search()
    #
    # def test_empty_cart_text(self):
    #     self.SubCartPage = SubCartPage(self.driver)
    #     self.SubCartPage.click_cart_link()
    #     time.sleep(2)
    #     self.SubCartPage.assert_element_text(self.driver.find_element(*Locators.EMPTY_CART_SCREEN_LOCATOR).text, TestData.EMPTY_CART_SCREEN_TEXT)
    # #
    # def test_add_item_cart(self):
    #     self.CartPage = CartPage(self.driver)
    #     self.CartPage.add_item_cart()
    #     self.CartPage.delete_item()
    #
    # def test_delete_cart(self):
    #     self.CartPage = CartPage(self.driver)
    #     self.CartPage.delete_item()
    #
    @pytest.mark.base
    def test_sign_in_screen(self):
        self.signInScreen = SignInPage(self.driver)
        self.signInScreen.sign_in_failed()
        self.signInScreen.assert_element_text(Locators.SIGN_IN_LOCATOR_ALERT, TestData.ALERT_SIGN_IN_SCREEN)

    """ Appium Test """
    def test_imdb_home_page(self):
        self.ImdbHomePage = ImdbHomePage(self.driver)
        self.ImdbHomePage.search_text_and_click()

    @pytest.mark.base
    def test_sql_enter_text_pixel(self):
        self.sqlText = SqlText(self.driver)
        self.sqlText.sql_search_text_pixel()
        self.assertEqual(self.driver.find_element(*Locators.RESULT_SCREEN_SQL).text, '"Pixel"')
    #
    # def test_sql_enter_text_redmi(self):
    #     self.sqlText = SqlText(self.driver)
    #     self.sqlText.sql_search_text_redmi()
    #     self.assertEqual(self.driver.find_element(*Locators.RESULT_SCREEN_SQL).text, '"redmi 6"')

    def test_csv_device(self):
        self.sqlText = SqlText(self.driver)
        self.sqlText.csv_devices_test()

    @pytest.mark.base
    def test_hover_items(self):
        self.hover = HoverItems(self.driver)
        self.hover.hover_between_items()

    def test_get_request(self):
        self.api = ApiActions()
        self.api.get_request(TestData.API_URL_GET)

    def test_post_request(self):
        self.api = ApiActions()
        self.api.post_request(TestData.API_URL_POST)


if __name__ == '__main__':
    unittest.main()
