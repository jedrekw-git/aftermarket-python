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

class RegisteredOptionsListPage(BasePage):
    _title = "Registered options"

    _first_option_checkbox = (By.XPATH, "//td[3]/div/span/label/span")
    _renew_first_option_button = (By.XPATH, "//button[2]")
    _stage2_result_field = (By.XPATH, "//td[3]/label/span")
    _stage2_option_name_field = (By.XPATH, "//td[2]/label/span")
    _submit_button = (By.XPATH, "//button[2]")
    _result_domain_name_field = (By.XPATH, "/html/body/div[7]/div/div/form/div[2]/table/tbody/tr[1]/td[2]/span")
    _result_text_field = (By.XPATH, "/html/body/div[7]/div/div/form/div[2]/table/tbody/tr[1]/td[3]")
    _transfer_first_option_button = (By.XPATH, "//button[4]")
    _transfer_option_login_field = (By.XPATH, "//div[3]/div/input")
    _transfer_list_first_option_field = (By.XPATH, "//td[3]/div/span/label/span")
    _transfer_list_first_option_cancel_button = (By.XPATH, "//td/div/button")

    def __init__(self, driver):
        super(RegisteredOptionsListPage, self).__init__(driver, self._title)

    def first_option_text(self):
        self._first_option_text_value = self.get_text(self._first_option_checkbox)

    def renew_option(self):
        self.click(self._first_option_checkbox)
        self.click(self._renew_first_option_button)

    def stage2_option_text(self):
        return self.get_text(self._stage2_option_name_field)

    def submit_and_accept_alert(self):
        self.click(self._submit_button)
        sleep(2)
        self.accept_alert()

    def result_domain_text(self):
        return self.get_text(self._result_domain_name_field)

    def result_text(self):
        return self.get_text(self._result_text_field)

    def transfer_option(self):
        self.click(self._first_option_checkbox)
        self.click(self._transfer_first_option_button)

    def transfer_option_enter_login(self, login):
        self.clear_field_and_send_keys(login, self._transfer_option_login_field)

    def submit(self):
        self.click(self._submit_button)

    def transfer_list_first_domain_text(self):
        return self.get_text(self._transfer_list_first_option_field)

    def delete_first_transfer(self):
        self.click(self._transfer_list_first_option_field)
        self.click(self._transfer_list_first_option_cancel_button)



