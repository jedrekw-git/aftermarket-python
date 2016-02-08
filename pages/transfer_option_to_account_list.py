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

class TransferOptionToAccountList(BasePage):
    _title = "Transfer Option To Account List"

    _new_option_transfer_button = (By.XPATH, "//button")
    _domain_name_field = (By.NAME, "domain")
    _authinfo_field = (By.NAME, "authinfo")
    _submit_button = (By.XPATH, "//button[2]")
    _first_option_checkbox = (By.XPATH, "//td[3]/div/span/label/span")
    _first_option_remove_button = (By.XPATH, "//td/div/button")
    _stage2_result_field = (By.XPATH, "//td[3]/label/span")
    _stage2_option_name_field = (By.XPATH, "//td[2]/label/span")

    def __init__(self, driver):
        super(TransferOptionToAccountList, self).__init__(driver, self._title)

    def new_option_transfer(self, domain, authinfo):
        self.click(self._new_option_transfer_button)
        self.clear_field_and_send_keys(domain, self._domain_name_field)
        self.clear_field_and_send_keys(authinfo, self._authinfo_field)
        self.click(self._submit_button)

    def remove_first_transfer(self):
        self.click(self._first_option_checkbox)
        self.click(self._first_option_remove_button)

    def stage2_option_text(self):
        return self.get_text(self._stage2_option_name_field)
