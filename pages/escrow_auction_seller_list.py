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

class EscrowAuctionSellerListPage(BasePage):
    _title = "Escrow Auction Seller List"

    _first_auction_domain_name_field = (By.XPATH, "//label/span")
    _first_auction_buyer_login_field = (By.XPATH, "//td[3]/div/span/a")
    _first_auction_price_field = (By.XPATH, "//td[5]/div/b")
    _first_auction_delete_button = (By.XPATH, "//td[8]/div/a/img")
    _delete_auction_domain_name_field = (By.XPATH, "//div[3]/div/span")
    _delete_auction_buyer_login_field = (By.XPATH, "//div[3]/div[3]/div/span")
    _delete_auction_result_field = (By.XPATH, "//p")
    _submit_button = (By.XPATH, "//div[2]/button")
    _submit_confirm_button = (By.XPATH, "//div[3]/button")
    _back_from_results_page_button = (By.XPATH, "//button")
    _second_domain_field = (By.XPATH, "//tbody[2]/tr/td[2]/div/label/span")
    _second_domain_login_field = (By.XPATH, "//tbody[2]/tr/td[3]/div/span/a")
    _second_domain_price_field = (By.XPATH, "//tbody[2]/tr/td[5]/div/b")
    _search_field = (By.NAME, "domain")
    _search_button = (By.XPATH, "//span/div/button")

    def __init__(self, driver):
        super(EscrowAuctionSellerListPage, self).__init__(driver, self._title)

    def first_auction_domain_name_text(self):
        return self.get_text(self._first_auction_domain_name_field)

    def first_auction_buyer_login_text(self):
        return self.get_text(self._first_auction_buyer_login_field)

    def first_auction_price_text(self):
        return self.get_text(self._first_auction_price_field)

    def delete_all_escrow_auctions(self):
        while True:
            if "/assets/img/table/delete.svg" in self.get_page_source():
                self.click(self._first_auction_delete_button)
                self.click(self._submit_button)
                self.click(self._submit_confirm_button)
                WebDriverWait(self.get_driver(), 30).until(EC.text_to_be_present_in_element(self._delete_auction_result_field, u"Transakcja Escrow została anulowana."))
                self.click(self._back_from_results_page_button)
            else:
                break

    def back_from_results_page(self):
        self.click(self._back_from_results_page_button)

    def get_text_second_domain_login_and_price(self):
        self.second_domain_text = self.get_text(self._second_domain_field)
        self.second_domain_login_text = self.get_text(self._second_domain_login_field)
        self.second_domain_price_text = self.get_text(self._second_domain_price_field)

    def search_for_auction(self, domain_name):
        self.clear_field_and_send_keys(domain_name, self._search_field)
        self.click(self._search_button)
