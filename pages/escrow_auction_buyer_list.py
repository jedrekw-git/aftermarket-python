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

class EscrowAuctionBuyerListPage(BasePage):
    _title = "Escrow Auction Buyer List"

    _first_auction_domain_name_field = (By.XPATH, "//label/span")
    _first_auction_buyer_status_field = (By.XPATH, "//td[3]/div")
    _first_auction_price_field = (By.XPATH, "//td[4]/div/b")
    _submit_button = (By.XPATH, "//button[2]")
    _back_from_results_page_button = (By.XPATH, "//div[3]/div/button")
    _second_domain_field = (By.XPATH, "//tbody[2]/tr/td[2]/div/label/span")
    _second_domain_status_field = (By.XPATH, "//tbody[2]/tr/td[3]/div")
    _second_domain_price_field = (By.XPATH, "//tbody[2]/tr/td[4]/div/b")
    _search_field = (By.NAME, "domain")
    _search_button = (By.XPATH, "//button")

    def __init__(self, driver):
        super(EscrowAuctionBuyerListPage, self).__init__(driver, self._title)

    def first_auction_domain_name_text(self):
        return self.get_text(self._first_auction_domain_name_field)

    def first_auction_buyer_status_text(self):
        return self.get_text(self._first_auction_buyer_status_field)

    def first_auction_price_text(self):
        return self.get_text(self._first_auction_price_field)

    def search_for_auction(self, domain_name):
        self.clear_field_and_send_keys(domain_name, self._search_field)
        self.click(self._search_button)

    def get_text_second_domain_status_and_price(self):
        self.second_domain_text = self.get_text(self._second_domain_field)
        self.second_domain_status_text = self.get_text(self._second_domain_status_field)
        self.second_domain_price_text = self.get_text(self._second_domain_price_field)