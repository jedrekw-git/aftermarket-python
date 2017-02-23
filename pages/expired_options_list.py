# coding=utf-8
from selenium.webdriver.common.by import By
from pages.base import BasePage
from utils.utils import *
from random import randint
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from random import randint

class ExpiredOptionsList(BasePage):
    _title = "Expired Options List"

    _sixth_option_value = (By.XPATH, "//tbody[6]/tr/td[3]/div/label/span")
    _first_option_value = (By.XPATH, "//div/label/span")
    _search_field = (By.NAME, "domain")
    _search_button_submit = (By.XPATH, "//button")

    def __init__(self, driver):
        super(ExpiredOptionsList, self).__init__(driver, self._title)

    def get_text_sixth_option(self):
        self.sixth_option_text = self.get_text(self._sixth_option_value)

    def search_for_option(self, option):
        self.clear_field_and_send_keys(option, self._search_field)
        self.click(self._search_button_submit)