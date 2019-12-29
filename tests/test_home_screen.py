
from amazon.web.page_object.base_class import TestBase
from amazon.web.page_object.home_page_screen import HomePageTests, HomePageLoaded


class TestHomeScreen(TestBase):

    def test_home_search_filed(self):
        self.test = HomePageTests(self.driver)
        self.test.search_text()

    def test_home_loaded(self):
        self.test = HomePageLoaded(self.driver)
        self.test.test_home_page_loaded_successfully()

