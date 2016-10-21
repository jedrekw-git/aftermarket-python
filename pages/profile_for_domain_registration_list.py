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

class ProfileForDomainRegistrationList(BasePage):
    _title = "Profile For Domain Registration"

    _submit_button = (By.XPATH, "//button[2]")
    _register_new_profile_button = (By.XPATH, "//button")
    _profile_name_field = (By.NAME, "title")
    _profile_name_value = "z"+get_random_string(7)
    _company_name_field = (By.NAME, "name")
    _company_name_value = get_random_string(5)+" "+get_random_string(6)
    _address_field = (By.NAME, "address")
    _address_value = get_random_string(9)+" "+get_random_integer(2)
    _zip_field = (By.NAME, "zip")
    _zip_value = get_random_integer(2)+"-"+get_random_integer(3)
    _city_field = (By.NAME, "city")
    _city_value = get_random_string(7)
    _country_dropdown = (By.NAME, "country")
    _country_index = randint(1, 245)
    _phone_directional_dropdown = (By.NAME, "country3")
    _phone_directional_index = randint(1, 215)
    _phone_number_field = (By.NAME, "phone")
    _phone_number_value = get_random_integer(9)
    _delete_button = (By.XPATH, "//div[3]/div/button")
    _delete_submit = (By.XPATH, "//button[2]")
    _result_text_field = (By.XPATH, "/html/body/div[7]/div/div/form/div[2]/table/tbody/tr[1]/td[3]")
    _back_from_results_page_button = (By.XPATH, "//button")
    _added_profile_name_field = (By.XPATH, "//tr[7]/td[3]/div/span/label")
    _profiles_header = (By.XPATH, "//h1")

    def __init__(self, driver):
        super(ProfileForDomainRegistrationList, self).__init__(driver, self._title)

    def register_new_profile(self):
        self.click(self._register_new_profile_button)
        self.clear_field_and_send_keys(self._profile_name_value, self._profile_name_field)
        self.clear_field_and_send_keys(self._company_name_value, self._company_name_field)
        self.clear_field_and_send_keys(self._address_value, self._address_field)
        self.clear_field_and_send_keys(self._zip_value, self._zip_field)
        self.clear_field_and_send_keys(self._city_value, self._city_field)
        self.select_index_from_dropdown(self._country_index, self._country_dropdown)
        self.select_index_from_dropdown(self._phone_directional_index, self._phone_directional_dropdown)
        self.clear_field_and_send_keys(self._phone_number_value, self._phone_number_field)
        self.click(self._submit_button)

    def delete_added_profile(self):
        self.click(self._added_profile_name_field)
        self.click(self._delete_button)
        self.click(self._delete_submit)

    def delete_all_profiles(self):
        while True:
            if "/assets/img/table/row/delete.png" in self.get_page_source():
                self.click(self._added_profile_name_field)
                self.click(self._delete_button)
                self.click(self._delete_submit)
                self.click(self._back_from_results_page_button)
            else:
                break

    def back_from_results_page(self):
        self.click(self._back_from_results_page_button)