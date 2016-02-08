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

class SellingHistoryPage(BasePage):
    _title = "Selling history"

    _second_domain_checkbox = (By.XPATH, "//tr[6]/td[2]/div/span/label/span")
    _first_domain_checkbox = (By.XPATH, "//label/span")
    _search_field = (By.NAME, "domain")
    _search_button = (By.XPATH, "//button")

    def __init__(self, driver):
        super(SellingHistoryPage, self).__init__(driver, self._title)

    def get_second_domain_text(self):
        self._second_domain_text = self.get_text(self._second_domain_checkbox)

    def search_for_domain(self, domain_name):
        self.clear_field_and_send_keys(domain_name, self._search_field)
        self.click(self._search_button)