import requests
import bs4

# Sending requset via url
from amazon.web.drivers.tests_data import TestData
from amazon.web.page_object.seleniuem_wrapper import SeleniumWrapper


class WebScaping(SeleniumWrapper):
    def return_data(self, tag):
        test = SeleniumWrapper

        response = requests.get(test.current_url(self))
        response_code = response.status_code

        if response_code == 200:
            parred_data = bs4.BeautifulSoup(response.text)
            all_links = parred_data.select(tag)
            print('Number of the tag on the page: ' + str(len(all_links)) + '\n')
            for i in all_links:
                print('Get text: ' + i.getText())
                print('Get href:  ' + i.get('href'))
                print('Get Attrs: ' + str(i.attrs) + '\n')
            return all_links
        else:
            raise Exception(print('The url of web scarping is not good, status code: %s' % response_code))
