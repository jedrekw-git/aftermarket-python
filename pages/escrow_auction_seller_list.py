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
    _first_auction_buyer_login_field = (By.XPATH, "//span/span/a")
    _first_auction_price_field = (By.XPATH, "//div/span/b")
    _first_auction_delete_button = (By.XPATH, "//div/span/img")
    _delete_auction_domain_name_field = (By.XPATH, "//div[3]/div/span")
    _delete_auction_buyer_login_field = (By.XPATH, "//div[3]/div[3]/div/span")
    _submit_button = (By.XPATH, "//button[2]")
    _back_from_results_page_button = (By.XPATH, "//div[3]/div/button")
    _eighteen_domain_field = (By.XPATH, "//tr[52]/td[2]/div/span/label/span")
    _eighteen_domain_login_field = (By.XPATH, "//tr[52]/td[3]/div/span/span/a")
    _eighteen_domain_price_field = (By.XPATH, "//tr[52]/td[5]/div/span/b")
    _search_field = (By.NAME, "domain")
    _search_button = (By.XPATH, "//div[3]/button")

    def __init__(self, driver):
        super(EscrowAuctionSellerListPage, self).__init__(driver, self._title)

    def first_auction_domain_name_text(self):
        return self.get_text(self._first_auction_domain_name_field)

    def first_auction_buyer_login_text(self):
        return self.get_text(self._first_auction_buyer_login_field)

    def first_auction_price_text(self):
        return self.get_text(self._first_auction_price_field)

    def delete_first_escrow_auction(self):
        self.click(self._first_auction_delete_button)

    def delete_auction_domain_name_text(self):
        return self.get_text(self._delete_auction_domain_name_field)

    def delete_auction_buyer_login_text(self):
        return self.get_text(self._delete_auction_buyer_login_field)

    def delete_auction_submit(self):
        self.click(self._submit_button)
        self.accept_alert()

    def back_from_results_page(self):
        self.click(self._back_from_results_page_button)

    def get_text_eighteenth_domain_login_and_price(self):
        self.eighteenth_domain_text = self.get_text(self._eighteen_domain_field)
        self.eighteenth_domain_login_text = self.get_text(self._eighteen_domain_login_field)
        self.eighteenth_domain_price_text = self.get_text(self._eighteen_domain_price_field)

    def search_for_auction(self, domain_name):
        self.clear_field_and_send_keys(domain_name, self._search_field)
        self.click(self._search_button)