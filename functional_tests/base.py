import sys
import os.path
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException


class FunctionalTest(StaticLiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        # self.browser.implicitly_wait(5)
        self.browser.wait = WebDriverWait(self.browser, 5)

    def tearDown(self):
        self.browser.quit()

    def login(self):
        self.browser.get(self.server_url)
        self.browser.wait.until(EC.text_to_be_present_in_element(
            (By.XPATH, '//*[@id="bs-navbar-collapse-1"]/ul[2]/li[2]/a'), "Log In"
        ))
        link = self.browser.find_element_by_link_text('Log In')
        link.click()
        self.browser.find_element_by_id('id_login').send_keys('steve.smith@test.com')
        self.browser.find_element_by_id('id_password').send_keys('Password1@')
        self.browser.find_element_by_id('id_btn_login').click()

    def fill_text_box_by_id(self, id_, value):
        tb = self.browser.find_element_by_id(id_)
        tb.clear()
        tb.send_keys(value)

    def set_select_value_by_id(self, id_, value):
        slt = Select(self.browser.find_element_by_id(id_))
        slt.select_by_value(value)

    def check_element_exists_by_id(self, id_):
        try:
            self.browser.find_element_by_id(id_)
        except NoSuchElementException:
            return False
        return True
