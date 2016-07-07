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

    _first_domain_checkbox = (By.XPATH, "//span/label/span")
    _first_domain_price_field = (By.XPATH, "//div/span/b")
    _second_domain_checkbox = (By.XPATH, "//tr[9]/td[2]/div/span/label/span")
    _fourth_domain_checkbox = (By.XPATH, "//tr[15]/td[2]/div/span/label/span")
    _fourth_domain_price_field = (By.XPATH, "//tr[15]/td[5]/div/span/b")
    _offers_tab = (By.XPATH, "/html/body/div[7]/div/div/ul/li[3]")
    _add_offer_to_second_domain_button = (By.XPATH, "//tr[11]/td/div/button")
    _submit_offer_domain_name_value = (By.XPATH, "//div[3]/div/span")
    _submit_offer_price_value = (By.XPATH, "//div[3]/div[3]/div/span")
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
    _search_field = (By.NAME, "domain")
    _search_button = (By.XPATH, "//div[3]/button")
    _more_filters_button = (By.XPATH, "//form/div/div/div/button")
    _filter_length_from_field = (By.XPATH, "//div[3]/div[2]/input")
    _filter_length_from_value = randint(1, 7)
    _filter_length_to_field = (By.XPATH, "//div[3]/div[2]/input[2]")
    _filter_length_to_value = randint(8, 15)
    _filter_extension_dropdown = (By.XPATH, "//span[2]/input")
    _filter_extension_com_pl_option = (By.XPATH, "//span[2]/div/div/div[2]/label")
    _filter_submit = (By.XPATH, "//form/div[3]/button")
    _subscribe_results_button = (By.XPATH, "//p/button")
    _subscribe_results_subuscription_name_field = (By.XPATH, "//div/input")
    _subscribe_results_subuscription_name_value = get_random_string(12)
    _delete_first_subscription_button = (By.XPATH, "//div/span/img")


    def __init__(self, driver):
        super(DomainsOnMarketplaceList, self).__init__(driver, self._title)

    def open_offers_tab(self):
        self.click(self._offers_tab)

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

    def get_text_fourth_domain_and_price(self):
        self._fourth_domain_text = self.get_text(self._fourth_domain_checkbox)
        self._fourth_domain_price_text = self.get_text(self._fourth_domain_price_field)

    def search_for_domain(self, domain_name):
        self.clear_field_and_send_keys(domain_name, self._search_field)
        self.click(self._search_button)

    def filter_results_12_characters_com_pl(self):
        self.click(self._more_filters_button)
        self.clear_field_and_send_keys("12", self._filter_length_from_field)
        self.clear_field_and_send_keys("12", self._filter_length_to_field)
        self.click(self._filter_extension_dropdown)
        sleep(2)
        self.click(self._filter_extension_com_pl_option)
        sleep(2)
        self.click(self._filter_submit)

    def first_domain_text(self):
        return self.get_text(self._first_domain_checkbox)

    def filter_results_length_com_pl(self):
        self.click(self._more_filters_button)
        self.clear_field_and_send_keys(self._filter_length_from_value, self._filter_length_from_field)
        self.clear_field_and_send_keys(self._filter_length_to_value, self._filter_length_to_field)
        self.click(self._filter_extension_dropdown)
        sleep(2)
        self.click(self._filter_extension_com_pl_option)
        sleep(2)
        self.click(self._filter_submit)

    def subscribe_results(self):
        self.click(self._subscribe_results_button)

    def subscribe_results_stage2(self):
        self.clear_field_and_send_keys(self._subscribe_results_subuscription_name_value, self._subscribe_results_subuscription_name_field)
        self.click(self._submit_button_stage2)

    def delete_first_subscription(self):
        self.click(self._delete_first_subscription_button)

    def delete_subscription_stage2(self):
        self.click(self._submit_button_stage2)