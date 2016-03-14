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

class DomainCatalogList(BasePage):
    _title = "Domain Catalog List"

    _add_new_catalog_button = (By.XPATH, "//button")
    _add_new_catalog_name_field = (By.XPATH, "//div/input")
    _catalog_description_field = (By.XPATH, "/html/body/div[7]/div/div/form/div[3]/div[3]/div[1]/div/div")
    _catalog_description_value = get_random_string(6)+" "+get_random_string(7)+" "+get_random_string(8)
    _submit_button = (By.XPATH, "//button[2]")
    _domain_name_dropdown = (By.XPATH, "//div[3]/div/div/input")
    _domain_name_index = randint(1, 13)
    _domain_name_option = (By.XPATH, "//div[%s]/label" %_domain_name_index)
    _back_to_domains_in_catalog_button = (By.XPATH, "//button")
    _first_domain_in_catalog_field = (By.XPATH, "//td[3]/div/span/label/span")
    _second_domain_in_catalog_field = (By.XPATH, "//tr[6]/td[3]/div/span/label/span")
    _remove_first_domain_in_catalog_button = (By.XPATH, "//div/span/img")
    _remove_first_catalog_button = (By.XPATH, "//span/img")
    _first_catalog_field = (By.XPATH, "//td[2]/div/span")
    _first_catalog_domains_list = (By.XPATH, "//button[2]")
    _add_domains_to_catalog_button = (By.XPATH, "//button")
    _search_field = (By.XPATH, "//form[2]/div/div/div/input")
    _search_button = (By.XPATH, "//div[2]/button")
    _result_text_field = (By.XPATH, "/html/body/div[7]/div/div/form/div[2]/table/tbody/tr[1]/td[3]")
    _result_domain_name_field = (By.XPATH, "/html/body/div[7]/div/div/form/div[2]/table/tbody/tr[1]/td[2]/span")

    def __init__(self, driver):
        super(DomainCatalogList, self).__init__(driver, self._title)

    def add_catalog_stage1(self, catalog_name):
        self.click(self._add_new_catalog_button)
        self.clear_field_and_send_keys(catalog_name, self._add_new_catalog_name_field)
        sleep(2)
        self.click(self._catalog_description_field)
        self.send_keys(self._catalog_description_value, self._catalog_description_field)
        self.click(self._submit_button)

    def add_catalog_stage2(self):
        self.click(self._domain_name_dropdown)
        sleep(2)
        self.click(self._domain_name_dropdown)
        self.domain_name = self.get_text(self._domain_name_option)
        self.click(self._domain_name_option)
        self.click(self._submit_button)

    def result_text(self):
        return self.get_text(self._result_text_field)

    def result_domain_text(self):
        return self.get_text(self._result_domain_name_field)

    def back_to_domains_in_catalog(self):
        self.click(self._back_to_domains_in_catalog_button)

    def remove_first_domain_in_catalog(self):
        self.click(self._remove_first_domain_in_catalog_button)
        self.accept_alert()

    def remove_first_catalog(self):
        self.click(self._remove_first_catalog_button)
        self.click(self._submit_button)
        self.accept_alert()

    def add_already_existing_domain_to_catalog(self):
        self.click(self._first_catalog_field)
        self.click(self._first_catalog_domains_list)
        self.first_domain_value = self.get_text(self._first_domain_in_catalog_field)
        self.click(self._add_domains_to_catalog_button)
        self.clear_field_and_send_keys(self.first_domain_value, self._domain_name_dropdown)
        self.click(self._submit_button)

    def search_second_domain_in_catalog(self):
        self.click(self._first_catalog_field)
        self.click(self._first_catalog_domains_list)
        self.second_domain_value = self.get_text(self._second_domain_in_catalog_field)
        self.clear_field_and_send_keys(self.second_domain_value, self._search_field)
        self.click(self._search_button)
