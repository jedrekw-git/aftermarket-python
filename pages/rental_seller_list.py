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

class RentalSellerList(BasePage):
    _title = "Rental Seller List"

    _second_domain_field = (By.XPATH, "//tr[4]/td[2]/div/span/label/span")
    _second_domain_login_field = (By.XPATH, "//tr[4]/td[3]/div/span/span/a")
    _second_domain_status_field = (By.XPATH, "//tr[4]/td[4]/div/span")
    _second_domain_price_field = (By.XPATH, "//tr[4]/td[5]/div/span/b")
    _first_domain_field = (By.XPATH, "//label/span")
    _first_domain_login_field = (By.XPATH, "//span/span/a")
    _first_domain_status_field = (By.XPATH, "//td[4]/div/span")
    _first_domain_price_field = (By.XPATH, "//div/span/b")
    _search_field = (By.NAME, "domain")
    _search_button = (By.XPATH, "//div[3]/button")
    _second_domain_details_button = (By.XPATH, "//tr[6]/td/div/button")
    _second_domain_add_note_button = (By.XPATH, "//tr[6]/td/div/button[3]")
    _add_note_field = (By.XPATH, "//div[3]/div[3]/div/div/div")
    _add_note_value = get_random_string(10)+" "+get_random_string(7)+" "+get_random_string(9)
    _submit_button = (By.XPATH, "//button[2]")
    _add_rental_transaction_button = (By.XPATH, "//button")
    _add_rental_transaction_domain_name_field = (By.XPATH, "//div/input")
    _add_rental_transaction_domain_name_first_checkbox = (By.XPATH, "//label")
    _add_rental_transaction_login_field = (By.XPATH, "//div[3]/div/input")
    _add_rental_transaction_monthly_rent_field = (By.XPATH, "//div[3]/div[3]/div/input")
    _add_rental_transaction_monthly_rent_value = get_random_integer(2)
    _add_rental_transaction_currency_dropdown = (By.XPATH, "//select")
    _add_rental_transaction_currency_index = randint(0, 3)
    _add_rental_transaction_rent_for_certain_time_radio = (By.XPATH, "//label[2]/span[2]")
    _add_rental_transaction_rent_duration_field = (By.XPATH, "//div[7]/div[3]/div/input")
    _add_rental_transaction_rent_duration_value = randint(8, 15)
    _add_rental_transaction_renter_can_terminate_agreement_checkbox = (By.XPATH, "//div[8]/div[3]/div/label/span[2]")
    _add_rental_transaction_lessee_can_terminate_agreement_checkbox = (By.XPATH, "//div[2]/label/span[2]")
    _add_rental_transaction_notice_period_field = (By.XPATH, "//div[10]/div[3]/div/input")
    _add_rental_transaction_notice_period_value = randint(1, 8)
    _add_rental_transaction_lessee_has_preemptive_right_checkbox = (By.XPATH, "//div[11]/div[3]/div/label/span[2]")
    _add_rental_transaction_preemption_price_field = (By.XPATH, "//div[12]/div[3]/div/input")
    _add_rental_transaction_preemption_price_value = randint(100, 200)
    _cancel_first_rental_transaction_button = (By.XPATH, "//td[8]/div/span/img")

    def __init__(self, driver):
        super(RentalSellerList, self).__init__(driver, self._title)

    def get_text_second_domain_login_status_and_price(self):
        self.second_domain_text = self.get_text(self._second_domain_field)
        self.second_domain_login_text = self.get_text(self._second_domain_login_field)
        self.second_domain_status_text = self.get_text(self._second_domain_status_field)
        self.second_domain_price_text = self.get_text(self._second_domain_price_field)

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

    def add_rental_transaction(self, login):
        self.click(self._add_rental_transaction_button)
        self.click(self._add_rental_transaction_domain_name_field)
        self._rental_domain_name_text = self.get_text(self._add_rental_transaction_domain_name_first_checkbox)
        self.click(self._add_rental_transaction_domain_name_first_checkbox)
        self.clear_field_and_send_keys(login, self._add_rental_transaction_login_field)
        self.clear_field_and_send_keys(self._add_rental_transaction_monthly_rent_value, self._add_rental_transaction_monthly_rent_field)
        self.select_index_from_dropdown(self._add_rental_transaction_currency_index, self._add_rental_transaction_currency_dropdown)
        self.click(self._add_rental_transaction_rent_for_certain_time_radio)
        self.clear_field_and_send_keys(self._add_rental_transaction_rent_duration_value, self._add_rental_transaction_rent_duration_field)
        self.click(self._add_rental_transaction_renter_can_terminate_agreement_checkbox)
        self.click(self._add_rental_transaction_lessee_can_terminate_agreement_checkbox)
        self.clear_field_and_send_keys(self._add_rental_transaction_notice_period_value, self._add_rental_transaction_notice_period_field)
        self.click(self._add_rental_transaction_lessee_has_preemptive_right_checkbox)
        self.clear_field_and_send_keys(self._add_rental_transaction_preemption_price_value, self._add_rental_transaction_preemption_price_field)
        self.click(self._submit_button)

    def add_rental_transaction_submit(self):
        self.click(self._submit_button)
        self.accept_alert()
        sleep(10)

    def cancel_first_rental_transaction(self):
        self.click(self._cancel_first_rental_transaction_button)

    def cancel_first_rental_transaction_submit(self):
        self.click(self._submit_button)
        self.accept_alert()
        sleep(10)