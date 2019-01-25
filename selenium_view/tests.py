from django.test import LiveServerTestCase
from selenium import webdriver
import logging

class SinaTestCase(LiveServerTestCase):

    def setUp(self):
        self.selenium = webdriver.PhantomJS()
        super(SinaTestCase, self).setUp()

    def tearDown(self):
        self.selenium.quit()
        super(SinaTestCase, self).tearDown()

    def test_content(self):
        selenium = self.selenium
        #Opening the link we want to test
        url = '{}/compare/'.format(self.live_server_url)
        selenium.get(url)
        print("URL is : {}".format(url))
        #find the form element
        page_html = selenium.page_source
        print(page_html)
        xpath = '//ul[contains(@class, "list-a news_top")]'
        news_list = selenium.find_element_by_xpath(xpath)
        #print(news_list)
        assert news_list is not None, "new list is empty"


# Create your tests here.
