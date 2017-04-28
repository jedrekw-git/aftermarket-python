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

class SellingAuctionListPage(BasePage):
    _title = "Selling Auction"

    _first_auction_delete_button = (By.XPATH, "//td[11]/div/a/img")
    _submit_button = (By.XPATH, "//div[2]/button")
    _submit_confirm_button = (By.XPATH, "//div[3]/button")
    _back_from_results_page_button = (By.XPATH, "//button")
    _first_auction_checkbox = (By.XPATH, "//td[4]/div/label/span")
    _first_auction_change_button = (By.XPATH, "//div/span/span")
    _first_auction_change_prices_button = (By.XPATH, "//td/div/span/div/a[3]")
    _first_auction_change_description_button = (By.XPATH, "//td/div/span/div/a[4]")
    _edit_auction_details_change_minimal_price_radio = (By.XPATH, "//label[2]")
    _edit_auction_details_change_buynow_price_radio = (By.XPATH, "//div[6]/div/div[2]/div/label[2]")
    _edit_auction_details_price_start_field = (By.NAME, "price_start")
    _edit_auction_details_price_start_value = randint(1, 20)
    _edit_auction_details_price_minimum_field = (By.NAME, "price_minimum")
    _edit_auction_details_price_minimum_value = randint(21, 40)
    _edit_auction_details_price_buynow_field = (By.NAME, "price_buynow")
    _edit_auction_details_price_buynow_value = randint(41, 60)
    _edit_auction_details_description_field = (By.XPATH, "//div/div[2]/div/div/div")
    _edit_auction_details_description_value = get_random_string(10) + " " + get_random_string(7) + " " + get_random_string(8)
    _finish_auction_button = (By.XPATH, "//div[7]/div/button")
    _result_text_field = (By.XPATH, "//td[3]")
    _selling_auctions_header = (By.XPATH, "//h1")

    def __init__(self, driver):
        super(SellingAuctionListPage, self).__init__(driver, self._title)

    def delete_all_domain_selling_auctions(self):
        while True:
            if u"Brak aukcji" in self.get_page_source():
                break
            else:
                self.click(self._first_auction_delete_button)
                sleep(1)
                self.click(self._submit_button)
                self.click(self._submit_confirm_button)
                WebDriverWait(self.get_driver(), 30).until(EC.text_to_be_present_in_element(self._result_text_field, u"Aukcja została anulowana"))
                self.click(self._back_from_results_page_button)

    def back_from_results_page(self):
        self.click(self._back_from_results_page_button)

    def first_auction_enter_edit_prices(self):
        self.click(self._first_auction_checkbox)
        self.click(self._first_auction_change_button)
        self.click(self._first_auction_change_prices_button)

    def edit_auction_prices(self):
        self.click(self._edit_auction_details_change_minimal_price_radio)
        self.get_driver().execute_script("window.scrollTo(2700, 500);")
        self.click(self._edit_auction_details_change_buynow_price_radio)
        self.clear_field_and_send_keys(self._edit_auction_details_price_start_value, self._edit_auction_details_price_start_field)
        self.clear_field_and_send_keys(self._edit_auction_details_price_minimum_value,
                                       self._edit_auction_details_price_minimum_field)
        self.clear_field_and_send_keys(self._edit_auction_details_price_buynow_value,
                                       self._edit_auction_details_price_buynow_field)
        self.click(self._submit_button)
        self.click(self._submit_confirm_button)

    def first_auction_enter_edit_description(self):
        self.click(self._first_auction_checkbox)
        self.click(self._first_auction_change_button)
        self.click(self._first_auction_change_description_button)

    def edit_auction_description(self):
        self.clear_field_and_send_keys(self._edit_auction_details_description_value, self._edit_auction_details_description_field)
        self.click(self._submit_button)
        self.click(self._submit_confirm_button)