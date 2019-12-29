import pytest

from amazon.web.page_object.base_class import TestBase
from amazon.web.page_object.home_screen import SqlText
from amazon.web.resources.Locators import Locators


class TestDataDriven(TestBase):
    @pytest.mark.base
    def test_sql_enter_text_pixel(self):
        self.sqlText = SqlText(self.driver)
        self.sqlText.sql_search_text_pixel()
        self.assertEqual(self.driver.find_element(*Locators.RESULT_SCREEN_SQL).text, '"Pixel"')

    @pytest.mark.base
    def test_sql_enter_text_redmi(self):
        self.sqlText = SqlText(self.driver)
        self.sqlText.sql_search_text_redmi()
        self.assertEqual(self.driver.find_element(*Locators.RESULT_SCREEN_SQL).text, '"redmi 6"')

    def test_csv_device(self):
        self.sqlText = SqlText(self.driver)
        self.sqlText.csv_devices_test()
