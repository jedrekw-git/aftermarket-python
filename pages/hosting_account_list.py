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

class HostingAccountList(BasePage):
    _title = "Hosting Account List"

    _new_hosting_account_button = (By.XPATH, "//button")
    _new_hosting_account_packet_dropdown = (By.XPATH, "//select")
    _new_hosting_account_login_field = (By.NAME, "login")
    _new_hosting_account_login_value = get_random_string(7)
    _new_hosting_account_type_your_password_radio = (By.XPATH, "//label[2]")
    _new_hosting_account_password1_field = (By.NAME, "password1")
    _new_hosting_account_password2_field = (By.NAME, "password2")
    _new_hosting_account_login_stage_2_field = (By.XPATH, "//div[2]/div[3]/div/span")
    _new_hosting_account_packet_type_stage_2_field = (By.XPATH, "//div[3]/div/span")
    _new_hosting_account_pay_later_radio = (By.XPATH, "//label[2]/span[3]")
    _new_hosting_account_result_text_field = (By.XPATH, "//p")
    _submit_button = (By.XPATH, "//button[2]")
    _first_hosting_account = (By.XPATH, "//label/b")
    _first_hosting_account_add_domains_button = (By.XPATH, "//td/div/button")
    _add_domains_button = (By.XPATH, "//button")
    _add_domains_domain_field = (By.NAME, "domain")
    _back_from_results_page_button = (By.XPATH, "//button")
    _remove_first_domain_button = (By.XPATH, "//div/span/img")


    def __init__(self, driver):
        super(HostingAccountList, self).__init__(driver, self._title)

    def new_hosting_account(self, password):
        self.click(self._new_hosting_account_button)
        self.select_index_from_dropdown(0, self._new_hosting_account_packet_dropdown)
        self.clear_field_and_send_keys(self._new_hosting_account_login_value, self._new_hosting_account_login_field)
        self.click(self._new_hosting_account_type_your_password_radio)
        self.clear_field_and_send_keys(password, self._new_hosting_account_password1_field)
        self.clear_field_and_send_keys(password, self._new_hosting_account_password2_field)
        self.click(self._submit_button)

    def get_text_login_stage_2(self):
        return self.get_text(self._new_hosting_account_login_stage_2_field)

    def get_text_packet_type_stage_2(self):
        return self.get_text(self._new_hosting_account_packet_type_stage_2_field)

    def new_hosting_account_stage_2(self):
        self.click(self._new_hosting_account_pay_later_radio)
        self.click(self._submit_button)

    def add_domains_to_hosting_account(self):
        self.click(self._first_hosting_account)
        self.click(self._first_hosting_account_add_domains_button)

    def add_domains_to_hosting_account_stage2(self, domain_name):
        self.click(self._add_domains_button)
        self.clear_field_and_send_keys(domain_name, self._add_domains_domain_field)
        self.click(self._submit_button)

    def back_from_results_page(self):
        self.click(self._back_from_results_page_button)

    def remove_first_domain(self):
        self.click(self._remove_first_domain_button)
        self.accept_alert()