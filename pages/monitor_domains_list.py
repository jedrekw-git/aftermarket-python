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

class MonitorDomainsList(BasePage):
    _title = "Monitor Domains List"

    _second_domain_field = (By.XPATH, "//tr[7]/td[3]/div/span/label/span")
    _second_domain_status_field = (By.XPATH, "//tr[7]/td[6]/div/span")
    _first_domain_field = (By.XPATH, "//td[3]/div/span/label/span")
    _first_domain_status_field = (By.XPATH, "//td[6]/div/span")
    _search_field = (By.NAME, "domain")
    _search_button = (By.XPATH, "//div[3]/button")
    _first_domain_change_settings_button = (By.XPATH, "//button[3]")
    _change_settings_random = randint(1, 3)
    _change_settings_checkbox = (By.XPATH, "//div[%s]/label" %_change_settings_random)
    _change_settings_random2 = randint(1, 3)
    _change_settings_checkbox2 = (By.XPATH, "//div[%s]/label" %_change_settings_random2)
    _submit_button = (By.XPATH, "//button[2]")
    _result_domain_name_field = (By.XPATH, "/html/body/div[7]/div/div/form/div[2]/table/tbody/tr[1]/td[2]/span")
    _result_text_field = (By.XPATH, "/html/body/div[7]/div/div/form/div[2]/table/tbody/tr[1]/td[3]")
    _monitor_new_domain_button = (By.XPATH, "//button")
    _monitor_new_domain_domain_field = (By.XPATH, "//textarea")
    _remove_first_monitored_domain_button = (By.XPATH, "//div/span/img")
    _more_filters_button = (By.XPATH, "//div/div/button")
    _filters_dropdown = (By.XPATH, "//select")
    _filter_submit = (By.XPATH, "//form[2]/div[3]/button")

    def __init__(self, driver):
        super(MonitorDomainsList, self).__init__(driver, self._title)

    def get_text_second_domain_and_status(self):
        self.second_domain_text = self.get_text(self._second_domain_field)
        self.second_domain_status_text = self.get_text(self._second_domain_status_field)

    def search_for_domain(self, domain_name):
        self.clear_field_and_send_keys(domain_name, self._search_field)
        self.click(self._search_button)

    def change_first_domain_settings(self):
        self.click(self._first_domain_field)
        self.click(self._first_domain_change_settings_button)
        self.click(self._change_settings_checkbox)
        self.click(self._change_settings_checkbox2)
        self.click(self._submit_button)

    def get_text_first_domain(self):
        self.first_domain_text = self.get_text(self._first_domain_field)

    def result_domain_text(self):
        return self.get_text(self._result_domain_name_field)

    def monitor_new_domain(self, domain):
        self.click(self._monitor_new_domain_button)
        self.clear_field_and_send_keys(domain, self._monitor_new_domain_domain_field)
        self.click(self._change_settings_checkbox)
        self.click(self._change_settings_checkbox2)
        self.click(self._monitor_new_domain_button)

    def remove_first_monitored_domain(self):
        self.click(self._remove_first_monitored_domain_button)

    def filter_available(self):
        self.click(self._more_filters_button)
        self.select_index_from_dropdown(1, self._filters_dropdown)
        self.click(self._filter_submit)

    def filter_registered(self):
        self.click(self._more_filters_button)
        self.select_index_from_dropdown(2, self._filters_dropdown)
        self.click(self._filter_submit)


