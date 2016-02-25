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

class HireSellerList(BasePage):
    _title = "Hire Seller List"

    _second_domain_field = (By.XPATH, "//tr[4]/td[2]/div/span/label/span")
    _second_domain_login_field = (By.XPATH, "//tr[4]/td[3]/div/span/span/a")
    _second_domain_status_field = (By.XPATH, "//tr[4]/td[4]/div/span")
    _second_domain_price_field = (By.XPATH, "//tr[4]/td[5]/div/span/b")
    _second_domain_installments_field = (By.XPATH, "//tr[4]/td[6]/div/span")
    _first_domain_field = (By.XPATH, "//label/span")
    _first_domain_login_field = (By.XPATH, "//span/span/a")
    _first_domain_status_field = (By.XPATH, "//td[4]/div/span")
    _first_domain_price_field = (By.XPATH, "//div/span/b")
    _first_domain_installments_field = (By.XPATH, "//td[6]/div/span")
    _search_field = (By.NAME, "domain")
    _search_button = (By.XPATH, "//div[3]/button")
    _second_domain_details_button = (By.XPATH, "//tr[6]/td/div/button")
    _second_domain_add_note_button = (By.XPATH, "//tr[6]/td/div/button[3]")
    _add_note_field = (By.XPATH, "//div[3]/div[3]/div/div/div")
    _add_note_value = get_random_string(10)+" "+get_random_string(7)+" "+get_random_string(9)
    _submit_button = (By.XPATH, "//button[2]")
    _add_hire_transaction_button = (By.XPATH, "//button")
    _add_hire_transaction_domain_name_field = (By.XPATH, "//div/input")
    _add_hire_transaction_domain_name_first_checkbox = (By.XPATH, "//label")
    _add_hire_transaction_login_field = (By.XPATH, "//div[3]/div/input")
    _add_hire_transaction_monthly_installment_field = (By.XPATH, "//div[3]/div[3]/div/input")
    _add_hire_transaction_monthly_installment_value = get_random_integer(2)
    _add_hire_transaction_currency_dropdown = (By.XPATH, "//select")
    _add_hire_transaction_currency_index = randint(0, 3)
    _add_hire_transaction_number_of_installments_field = (By.XPATH, "//div[6]/div[3]/div/input")
    _add_hire_transaction_number_of_installments_value = randint(8, 15)
    _cancel_first_hire_transaction_button = (By.XPATH, "//td[9]/div/span/img")

    def __init__(self, driver):
        super(HireSellerList, self).__init__(driver, self._title)

    def get_text_second_domain_login_status_price_and_installments(self):
        self.second_domain_text = self.get_text(self._second_domain_field)
        self.second_domain_login_text = self.get_text(self._second_domain_login_field)
        self.second_domain_status_text = self.get_text(self._second_domain_status_field)
        self.second_domain_price_text = self.get_text(self._second_domain_price_field)
        self.second_domain_installments_text = self.get_text(self._second_domain_installments_field)

    def search_for_domain(self, domain_name):
        self.clear_field_and_send_keys(domain_name, self._search_field)
        self.click(self._search_button)

    def enter_second_domain_details(self):
        self.click(self._second_domain_field)
        self.click(self._second_domain_details_button)

    def second_domain_enter_add_note(self):
        self.click(self._second_domain_field)
        self.click(self._second_domain_add_note_button)

    def add_note(self):
        self.clear_field_and_send_keys(self._add_note_value, self._add_note_field)
        self.click(self._submit_button)

    def add_hire_transaction_stage1(self):
        self.click(self._add_hire_transaction_button)
        sleep(5)
        self.click(self._add_hire_transaction_domain_name_field)

    def add_hire_transaction_stage2(self, login):
        self._hire_domain_name_text = self.get_text(self._add_hire_transaction_domain_name_first_checkbox)
        self.click(self._add_hire_transaction_domain_name_first_checkbox)
        sleep(5)
        self.clear_field_and_send_keys(login, self._add_hire_transaction_login_field)
        self.clear_field_and_send_keys(self._add_hire_transaction_monthly_installment_value, self._add_hire_transaction_monthly_installment_field)
        self.select_index_from_dropdown(self._add_hire_transaction_currency_index, self._add_hire_transaction_currency_dropdown)
        self.clear_field_and_send_keys(self._add_hire_transaction_number_of_installments_value, self._add_hire_transaction_number_of_installments_field)
        self.click(self._submit_button)

    def add_hire_transaction_wrong_domain_name(self, login, domain_name):
        self.click(self._add_hire_transaction_button)
        sleep(5)
        self.clear_field_and_send_keys(domain_name, self._add_hire_transaction_domain_name_field)
        self.clear_field_and_send_keys(login, self._add_hire_transaction_login_field)
        self.clear_field_and_send_keys(self._add_hire_transaction_monthly_installment_value, self._add_hire_transaction_monthly_installment_field)
        self.select_index_from_dropdown(self._add_hire_transaction_currency_index, self._add_hire_transaction_currency_dropdown)
        self.clear_field_and_send_keys(self._add_hire_transaction_number_of_installments_value, self._add_hire_transaction_number_of_installments_field)
        self.click(self._submit_button)

    def add_hire_transaction_submit(self):
        self.click(self._submit_button)
        self.accept_alert()
        sleep(10)

    def cancel_first_hire_transaction(self):
        self.click(self._cancel_first_hire_transaction_button)

    def cancel_first_hire_transaction_submit(self):
        self.click(self._submit_button)
        self.accept_alert()
        sleep(10)