import pytest

from amazon.web.page_object.base_class import TestBase
from amazon.web.resources.Locators import Locators
from amazon.web.drivers.tests_data import TestData
from amazon.web.page_object.home_screen import SignInPage, HoverItems, CartPage, SubCartPage


class TestAMZNHomeScreen(TestBase):

    def test_empty_cart_text(self):
        self.SubCartPage = SubCartPage(self.driver)
        self.SubCartPage.click_cart_link()
        self.SubCartPage.assert_element_text(self.driver.find_element(*Locators.EMPTY_CART_SCREEN_LOCATOR).text, TestData.EMPTY_CART_SCREEN_TEXT)

    def test_add_item_cart(self):
        self.CartPage = CartPage(self.driver)
        self.CartPage.add_item_cart()
        self.CartPage.delete_item()

    def test_delete_cart(self):
        self.CartPage = CartPage(self.driver)
        self.CartPage.delete_item()

    def test_sign_in_screen(self):
        self.signInScreen = SignInPage(self.driver)
        self.signInScreen.sign_in_failed()
        self.signInScreen.assert_element_text(Locators.SIGN_IN_LOCATOR_ALERT, TestData.ALERT_SIGN_IN_SCREEN)

    @pytest.mark.base
    def test_hover_items(self):
        self.hover = HoverItems(self.driver)
        self.hover.hover_between_items()
