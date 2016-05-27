# -*- coding: utf-8 -*-
from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class NewVisitorTest(LiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Chrome('/Users/xmh/Desktop/python3/chromedriver')
        self.browser.implicitly_wait(3)

    def tearDown(self):
        time.sleep(10)
        self.browser.quit()

    def test_title_of_web(self):
        self.browser.get(self.live_server_url)

        self.assertIn('SafeMove', self.browser.title)
        self.browser.quit()
        # self.fail('Finish the test')

    def test_upload_event_as_a_visitor(self):
        self.browser.get('localhost:8000/upload_event/')
        col_0 = self.browser.find_element_by_id('name_id')
        col_0.send_keys('王新澳')
        time.sleep(3)
        col_1 = self.browser.find_element_by_id('email_id')
        col_1.send_keys('88888888@vip.com')
        time.sleep(3)
        col_2 = self.browser.find_element_by_id('tel_id')
        col_2.send_keys('18888888888')
        time.sleep(3)
        col_3 = self.browser.find_element_by_id('event_type_id')
        col_3.send_keys("1")
        col_3.find_element_by_xpath("//option[@value='2']").click()
        time.sleep(3)
        col_4 = self.browser.find_element_by_id('description_id')
        col_4.send_keys('被打了')
        time.sleep(3)

        click_button = self.browser.find_element_by_id('incident_submit')
        click_button.click()


        # form = self.browser.find_element_by_id('contact')
        # form.summit()

        time.sleep(3)
