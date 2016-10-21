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

class OptionEscrowTransactionPage(BasePage):
    _title = "Option Escrow Transaction"
    _option_name_field = (By.NAME, "domain")
    _first_option_checkbox = (By.XPATH, "//label")
    _buyer_login_field = (By.NAME, "login")
    _price_field = (By.NAME, "amount")
    _price_value = get_random_integer(2)
    _currency_dropdown = (By.NAME, "currency")
    _currency_index = randint(1,4)
    _days_to_pay_dropdown = (By.NAME, "days")
    _days_to_pay_index = randint(1,8)
    _submit_button = (By.XPATH, "//button[2]")


    def __init__(self, driver):
        super(OptionEscrowTransactionPage, self).__init__(driver, self._title)

    def add_escrow_option_transaction(self, buyer_login):
        self.click(self._option_name_field)
        self.click(self._first_option_checkbox)
        self.clear_field_and_send_keys(buyer_login, self._buyer_login_field)
        self.clear_field_and_send_keys(self._price_value, self._price_field)
        self.select_index_from_dropdown(self._currency_index, self._currency_dropdown)
        self.select_index_from_dropdown(self._days_to_pay_index, self._days_to_pay_dropdown)
        self.click(self._submit_button)


