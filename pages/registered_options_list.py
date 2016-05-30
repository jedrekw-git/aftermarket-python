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
    _second_option_checkbox = (By.XPATH, "//tr[8]/td[3]/div/span/label/span")
    _renew_first_option_button = (By.XPATH, "//button[2]")
    _change_profile_data_button = (By.XPATH, "//div[7]/div/button[2]")
    _stage2_result_field = (By.XPATH, "//td[3]/label/span")
    _stage2_option_name_field = (By.XPATH, "//td[2]/label/span")
    _submit_button = (By.XPATH, "//button[2]")
    _result_domain_name_field = (By.XPATH, "/html/body/div[7]/div/div/form/div[2]/table/tbody/tr[1]/td[2]/span")
    _result_text_field = (By.XPATH, "/html/body/div[7]/div/div/form/div[2]/table/tbody/tr[1]/td[3]")
    _transfer_first_option_button = (By.XPATH, "//button[4]")
    _transfer_button = (By.XPATH, "//div[7]/div/button[4]")
    _transfer_option_login_field = (By.XPATH, "//div[3]/div/input")
    _transfer_list_first_option_field = (By.XPATH, "//td[3]/div/span/label/span")
    _transfer_list_first_option_cancel_button = (By.XPATH, "//td/div/button")
    _get_option_authinfo_button = (By.XPATH, "//div[7]/div/button[3]")
    _second_stage_send_email_after_oparation_radio = (By.XPATH, "//label/span[2]")
    _second_stage_stop_realization_until_manual_activation_radio = (By.XPATH, "//div[3]/div[3]/div/label[2]/span[2]")

    def __init__(self, driver):
        super(RegisteredOptionsListPage, self).__init__(driver, self._title)

    def first_option_text(self):
        self._first_option_text_value = self.get_text(self._first_option_checkbox)

    def second_option_text(self):
        self._second_option_text_value = self.get_text(self._second_option_checkbox)

    def change_option_profile_data(self):
        self.click(self._first_option_checkbox)
        self.click(self._change_profile_data_button)
        self.click(self._submit_button)

    def renew_option(self):
        self.click(self._first_option_checkbox)
        self.click(self._renew_first_option_button)

    def stage2_option_text(self):
        return self.get_text(self._stage2_option_name_field)

    def submit_and_accept_alert(self):
        sleep(3)
        self.click(self._submit_button)
        sleep(3)
        self.accept_alert()

    def result_domain_text(self):
        return self.get_text(self._result_domain_name_field)

    def result_text(self):
        return self.get_text(self._result_text_field)

    def transfer_option_from_account(self):
        self.click(self._second_option_checkbox)
        self.click(self._transfer_button)

    def transfer_option_enter_login(self, login):
        self.clear_field_and_send_keys(login, self._transfer_option_login_field)

    def submit(self):
        self.click(self._submit_button)

    def transfer_list_first_domain_text(self):
        return self.get_text(self._transfer_list_first_option_field)

    def delete_first_transfer(self):
        self.click(self._transfer_list_first_option_field)
        self.click(self._transfer_list_first_option_cancel_button)

    def get_option_authinfo(self):
        self.click(self._second_option_checkbox)
        self.click(self._get_option_authinfo_button)
        self.click(self._submit_button)

    def store_option_authinfo(self):
        self._result_text = self.get_text(self._result_text_field)
        self._option_authinfo = self._result_text[14:]

    def second_stage_checkboxes_and_submit(self):
        self.click(self._second_stage_send_email_after_oparation_radio)
        self.click(self._second_stage_stop_realization_until_manual_activation_radio)
        self.click(self._submit_button)
        self.accept_alert()


