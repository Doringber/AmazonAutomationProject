from amazon.web.page_object.base_class import TestBase
from amazon.web.page_object.home_screen import ImdbHomePage


class TestImdbMobile(TestBase):
    """ Appium Test """
    def test_imdb_home_page(self):
        self.ImdbHomePage = ImdbHomePage(self.driver)
        self.ImdbHomePage.search_text_and_click()