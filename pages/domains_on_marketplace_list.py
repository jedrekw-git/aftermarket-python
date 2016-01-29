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

class DomainsOnMarketplaceList(BasePage):
    _title = "Domains on marketplace"

    _second_domain_checkbox = (By.XPATH, "//tr[9]/td[2]/div/span/label/span")
    _add_offer_to_second_domain_button = (By.XPATH, "//tr[11]/td/div/button")
    _price_field = (By.NAME, "amount")
    _price_value = get_random_integer(2)
    _submit_button = (By.XPATH, "//button")
    _buynow_price_text = (By.XPATH, "//div[3]/div[3]/div/span")
    _domain_field_stage1 = (By.XPATH, "//div[3]/div/span")
    _days_dropdown = (By.NAME, "days")
    _days_index = randint(0, 6)
    _send_additional_message_chackbox = (By.XPATH, "//label")
    _additional_message_value = get_random_string(10)+" "+get_random_string(12)+" "+get_random_string(14)
    _additional_message_field = (By.XPATH, "//div[3]/div/div/div")
    _submit_button_stage2 = (By.XPATH, "//button[2]")
    _remove_first_offer_button = (By.XPATH, "//td[8]/div/span/img")
    _remove_first_offer_additional_message_field = (By.XPATH, "//div[3]/div/div/div/p")
    _remove_first_offer_additional_message_value = get_random_string(10)+" "+get_random_string(12)+" "+get_random_string(14)
    _hide_offer_on_list_radio = (By.XPATH, "//label[2]")

    def __init__(self, driver):
        super(DomainsOnMarketplaceList, self).__init__(driver, self._title)

    def get_text_second_domain(self):
        self._second_domain_text = self.get_text(self._second_domain_checkbox)

    def add_offer_to_second_domain(self):
        self.click(self._second_domain_checkbox)
        self.click(self._add_offer_to_second_domain_button)

    def get_text_price_buynow(self):
        self.price_buynow = self.get_text(self._buynow_price_text)

    def submit_offer_stage1(self):
        self.clear_field_and_send_keys(self._price_value, self._price_field)
        self.click(self._submit_button)

    def submit_offer_stage2(self):
        self.select_index_from_dropdown(self._days_index, self._days_dropdown)
        self.click(self._send_additional_message_chackbox)
        self.clear_field_and_send_keys(self._additional_message_value, self._additional_message_field)
        self.click(self._submit_button_stage2)
        self.accept_alert()

    def delete_offer_stage1(self):
        self.click(self._submit_button_stage2)
        self.click(self._remove_first_offer_button)

    def delete_offer_stage2(self):
        self.click(self._send_additional_message_chackbox)
        self.clear_field_and_send_keys(self._remove_first_offer_additional_message_value, self._remove_first_offer_additional_message_field)
        self.click(self._hide_offer_on_list_radio)
        self.click(self._submit_button_stage2)
        self.accept_alert()

