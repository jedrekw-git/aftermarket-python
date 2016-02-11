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

class OptionEscrowSellingTransactionList(BasePage):
    _title = "Option Escrow Selling Transaction"

    _add_new_transaction_button = (By.XPATH, "//button")
    _option_name_field = (By.NAME, "domain")
    _buyer_login_field = (By.NAME, "login")
    _price_field = (By.NAME, "amount")
    _price_value = get_random_integer(2)
    _currency_dropdown = (By.NAME, "currency")
    _currency_index = randint(0,3)
    _days_to_pay_dropdown = (By.NAME, "days")
    _days_to_pay_index = randint(0,7)
    _submit_button = (By.XPATH, "//button[2]")
    _stage2_option_text_field = (By.XPATH, "//div[3]/div/span")
    _stage2_login_text_field = (By.XPATH, "//div[3]/div[3]/div/span")
    _delete_first_auction_button = (By.XPATH, "//div/span/img")
    _filter_new_button = (By.XPATH, "//div[7]/div/div/ul/li[2]")
    _third_domain_field = (By.XPATH, "//tr[7]/td[2]/div/span/label/span")
    _third_domain_login_field = (By.XPATH, "//tr[7]/td[3]/div/span/span/a")
    _third_domain_price_field = (By.XPATH, "//tr[7]/td[5]/div/span/b")
    _first_domain_field = (By.XPATH, "//label/span")
    _first_domain_login_field = (By.XPATH, "//span/span/a")
    _first_domain_price_field = (By.XPATH, "//div/span/b")
    _search_field = (By.NAME, "domain")
    _search_button = (By.XPATH, "//div[3]/button")

    def __init__(self, driver):
        super(OptionEscrowSellingTransactionList, self).__init__(driver, self._title)

    def add_escrow_option_transaction(self, buyer_login, option_name):
        self.click(self._add_new_transaction_button)
        self.clear_field_and_send_keys(option_name, self._option_name_field)
        self.clear_field_and_send_keys(buyer_login, self._buyer_login_field)
        self.clear_field_and_send_keys(self._price_value, self._price_field)
        self.select_index_from_dropdown(self._currency_index, self._currency_dropdown)
        self.select_index_from_dropdown(self._days_to_pay_index, self._days_to_pay_dropdown)
        self.click(self._submit_button)

    def stage2_option_text(self):
        return self.get_text(self._stage2_option_text_field)

    def stage2_login_text(self):
        return self.get_text(self._stage2_login_text_field)

    def stage2_submit_and_accept_alert(self):
        self.click(self._submit_button)
        self.accept_alert()

    def delete_first_auction(self):
        self.click(self._delete_first_auction_button)

    def filter_new(self):
        self.click(self._filter_new_button)

    def get_text_third_domain_login_and_price(self):
        self.third_domain_text = self.get_text(self._third_domain_field)
        self.third_domain_login_text = self.get_text(self._third_domain_login_field)
        self.third_domain_price_text = self.get_text(self._third_domain_price_field)

    def search_for_auction(self, domain_name):
        self.clear_field_and_send_keys(domain_name, self._search_field)
        self.click(self._search_button)
