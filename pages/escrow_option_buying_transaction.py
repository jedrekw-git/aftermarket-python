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

class OptionEscrowBuyingTransactionList(BasePage):
    _title = "Option Escrow Buying Transaction"

    _second_domain_field = (By.XPATH, "//tr[4]/td[2]/div/span/label/span")
    _second_domain_status_field = (By.XPATH, "//tr[4]/td[3]/div/span")
    _second_domain_price_field = (By.XPATH, "//tr[4]/td[4]/div/span/b")
    _first_domain_field = (By.XPATH, "//label/span")
    _first_domain_status_field = (By.XPATH, "//td[3]/div/span")
    _first_domain_price_field = (By.XPATH, "//div/span/b")
    _search_field = (By.NAME, "domain")
    _search_button = (By.XPATH, "//div[3]/button")

    def __init__(self, driver):
        super(OptionEscrowBuyingTransactionList, self).__init__(driver, self._title)

    def get_text_second_domain_status_and_price(self):
        self.second_domain_text = self.get_text(self._second_domain_field)
        self.second_domain_status_text = self.get_text(self._second_domain_status_field)
        self.second_domain_price_text = self.get_text(self._second_domain_price_field)

    def search_for_auction(self, domain_name):
        self.clear_field_and_send_keys(domain_name, self._search_field)
        self.click(self._search_button)

