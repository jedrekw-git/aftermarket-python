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

class WatchedDomainsListPage(BasePage):
    _title = "Watched domains"

    _watch_new_domain_button = (By.XPATH, "//button")
    _domain_name_field = (By.NAME, "domains")
    _domain_name_value = get_random_string(8)+".waw.pl"
    _watch_new_domain_submit = (By.XPATH, "//div[2]/button")
    _result_domain_name_field = (By.XPATH, "//div/span")
    _result_text_field = (By.XPATH, "//td[3]/div")
    _delete_first_domain_button = (By.XPATH, "//td[5]/div/a/img")
    _delete_first_domain_confirm_button = (By.XPATH, "//div[3]/button")
    _back_from_results_page_button = (By.XPATH, "//button")
    _first_domain_checkbox = (By.XPATH, "//div/label/span")
    _first_domain_change_settings_button = (By.XPATH, "//tr[3]/td/div/a")
    _change_watching_settings_choose_type_of_sending_notifications_radio = (By.XPATH, "//label[2]")
    _change_watching_settings_domain_issued_on_auction_checkbox = (By.XPATH, "//div[2]/div/div/label[2]")
    _change_watching_settings_domain_issued_on_last_minute_auction_checkbox = (By.XPATH, "//label[3]")
    _change_watching_settings_domain_set_on_sale_checkbox = (By.XPATH, "//label[4]")
    _change_watching_settings_set_buynow_price_checkbox = (By.XPATH, "//label[5]")
    _change_watching_settings_lowered_buynow_price_checkbox = (By.XPATH, "//label[6]")
    _change_watching_settings_raised_buynow_price_checkbox = (By.XPATH, "//label[7]")
    _change_watching_settings_domain_deleted_from_marketplace_checkbox = (By.XPATH, "//label[8]")
    _change_watching_settings_domain_available_to_buy_on_installments_checkbox = (By.XPATH, "//label[9]")
    _change_watching_settings_domain_available_to_lease_checkbox = (By.XPATH, "//label[10]")
    _change_watching_settings_domain_available_to_catch_checkbox = (By.XPATH, "//label[11]")

    def __init__(self, driver):
        super(WatchedDomainsListPage, self).__init__(driver, self._title)

    def watch_new_domain(self):
        self.click(self._watch_new_domain_button)
        self.clear_field_and_send_keys(self._domain_name_value, self._domain_name_field)
        self.click(self._watch_new_domain_submit)

    def result_domain_text(self):
        return self.get_text(self._result_domain_name_field)

    def delete_all_domains(self):
        while True:
            if "https://assets-testy.aftermarket2.pl//img/table/delete.svg" in self.get_page_source():
                self.click(self._delete_first_domain_button)
                self.click(self._delete_first_domain_confirm_button)
                WebDriverWait(self.get_driver(), 40).until(EC.text_to_be_present_in_element(self._result_text_field, u"Domena została usunięta z obserwacji"))
                self.click(self._back_from_results_page_button)
            else:
                break

    def back_from_results_page(self):
        self.click(self._back_from_results_page_button)

    def first_domain_change_watch_settings(self):
        self.click(self._first_domain_checkbox)
        self.click(self._first_domain_change_settings_button)
        self.click(self._change_watching_settings_choose_type_of_sending_notifications_radio)
        self.click(self._change_watching_settings_domain_issued_on_auction_checkbox)
        self.click(self._change_watching_settings_domain_issued_on_last_minute_auction_checkbox)
        self.click(self._change_watching_settings_domain_set_on_sale_checkbox)
        self.click(self._change_watching_settings_set_buynow_price_checkbox)
        self.click(self._change_watching_settings_lowered_buynow_price_checkbox)
        self.click(self._change_watching_settings_raised_buynow_price_checkbox)
        self.click(self._change_watching_settings_domain_deleted_from_marketplace_checkbox)
        self.click(self._change_watching_settings_domain_available_to_buy_on_installments_checkbox)
        self.click(self._change_watching_settings_domain_available_to_lease_checkbox)
        # self.click(self._change_watching_settings_domain_available_to_catch_checkbox)
        self.click(self._watch_new_domain_submit)