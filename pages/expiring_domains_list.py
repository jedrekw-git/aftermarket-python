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

class ExpiringDomainsList(BasePage):
    _title = "Expiring Domains List"

    _first_domain_checkbox = (By.XPATH, "//td[4]/div/span/label/span")
    _sixth_domain_checkbox = (By.XPATH, "//tr[23]/td[4]/div/span/label/span")
    _catch_first_domain_button = (By.XPATH, "//button[2]")
    _result_domain_name_field = (By.XPATH, "/html/body/div[7]/div/div/form/div[2]/table/tbody/tr[1]/td[2]/span")
    _result_text_field = (By.XPATH, "/html/body/div[7]/div/div/form/div[2]/table/tbody/tr[1]/td[3]")
    _search_field = (By.XPATH, "//input")
    _search_button = (By.XPATH, "//div[3]/button")
    _filter_button = (By.XPATH, "//form/div/div/div/button")
    _filter_length_from = (By.XPATH, "//div[3]/div/div[2]/input")
    _filter_length_from_value = randint(1, 7)
    _filter_length_to = (By.XPATH, "//input[2]")
    _filter_length_to_value = randint(8, 15)
    _filter_extension_dropdown = (By.XPATH, "//span[2]/input")
    _filter_extension_com_pl = (By.XPATH, "//span[2]/div/div/div[2]/label")
    _filter_extension_pl = (By.XPATH, "//span[2]/div/div/div/label")
    _filter_submit = (By.XPATH, "//form/div[3]/button")
    _subscribe_results_button = (By.XPATH, "//p/button")
    _subscription_name_field = (By.XPATH, "//div/input")
    _subscription_name_value = get_random_string(10)
    _subscription_submit = (By.XPATH, "//button[2]")
    _subscription_delete_first_button = (By.XPATH, "//div/span/img")

    def __init__(self, driver):
        super(ExpiringDomainsList, self).__init__(driver, self._title)

    def catch_first_domain(self):
        self.click(self._first_domain_checkbox)
        self.click(self._catch_first_domain_button)

    def first_domain_text(self):
        self._first_domain_text_value = self.get_text(self._first_domain_checkbox)
        return self.get_text(self._first_domain_checkbox)

    def result_domain_text(self):
        return self.get_text(self._result_domain_name_field)

    def sixth_domain_text(self):
        self._sixth_domain_text_value = self.get_text(self._sixth_domain_checkbox)

    def search_for_domain_to_catch(self, domain):
        self.clear_field_and_send_keys(domain, self._search_field)
        self.click(self._search_button)

    def filter_results_4_characters_com_pl(self):
        self.click(self._filter_button)
        self.clear_field_and_send_keys(4, self._filter_length_from)
        self.clear_field_and_send_keys(4, self._filter_length_to)
        sleep(2)
        self.click(self._filter_extension_dropdown)
        sleep(2)
        self.click(self._filter_extension_com_pl)
        sleep(2)
        self.click(self._filter_submit)
        sleep(3)

    def filter_results_length_and_pl(self):
        self.click(self._filter_button)
        self.clear_field_and_send_keys(self._filter_length_from_value, self._filter_length_from)
        self.clear_field_and_send_keys(self._filter_length_to_value, self._filter_length_to)
        sleep(2)
        self.click(self._filter_extension_dropdown)
        sleep(2)
        self.click(self._filter_extension_pl)
        sleep(2)
        self.click(self._filter_submit)

    def subscribe_results(self):
        self.click(self._subscribe_results_button)

    def enter_subscription_name_and_submit(self):
        self.clear_field_and_send_keys(self._subscription_name_value, self._subscription_name_field)
        self.click(self._subscription_submit)

    def delete_added_subscription_1_stage(self):
        self.click(self._subscription_delete_first_button)

    def delete_added_subscription_2_stage(self):
        self.click(self._subscription_submit)
