import unittest

from amazon.web.page_object.base_class import TestBase
from amazon.web.page_object.pages import KanHomePage


class TestKanSite(TestBase):
    def setUp(self):
        # to call the setUp() method of base class or super class.
        super().setUp()

    def test_home_search(self):
        # instantiate an object of HomePage class. Remember when the constructor of HomePage class is called
        # it opens up the browser and navigates to Home Page of the site under test.
        self.homePage = KanHomePage(self.driver)
        # assert if the title of Home Page contains Amazon.in


if __name__ == '__main__':
    unittest.main()
