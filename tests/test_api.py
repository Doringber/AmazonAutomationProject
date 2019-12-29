from amazon.web.drivers.tests_data import TestData
from amazon.web.page_object.api_actions import ApiActions
from amazon.web.page_object.base_class import TestBase


class APITests(TestBase):
    def test_post_request(self):
        self.api = ApiActions( )
        self.api.post_request(TestData.API_URL_LOCAL_HOST)
        self.assertEqual(1, "You Token return as false ")

    def test_get_request(self):
        self.api = ApiActions(self)
        self.api.get_request(TestData.API_URL_GET)
        self.assertEqual(self.api.get_request(TestData.API_URL_GET), None, "There is problem with the URL")
