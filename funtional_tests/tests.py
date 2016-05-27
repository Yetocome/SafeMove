from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class NewVisitorTest(LiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Chrome('/Users/xmh/Desktop/python3/chromedriver')
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def test_title_of_web(self):
        self.browser.get(self.live_server_url)

        self.assertIn('SafeMove', self.browser.title)

        self.fail('Finish the test')
