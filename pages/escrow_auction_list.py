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

class EscrowAuctionListPage(BasePage):
    _title = "Escrow Auction List"

    _first_auction_domain_name_field = (By.XPATH, "//label/span")
    _first_auction_buyer_login_field = (By.XPATH, "//span/span/a")
    _first_auction_delete_button = (By.XPATH, "//div/span/img")
    _delete_auction_domain_name_field = (By.XPATH, "//div[3]/div/span")
    _delete_auction_buyer_login_field = (By.XPATH, "//div[3]/div[3]/div/span")
    _submit_button = (By.XPATH, "//button[2]")
    _back_from_results_page_button = (By.XPATH, "//div[3]/div/button")

    def __init__(self, driver):
        super(EscrowAuctionListPage, self).__init__(driver, self._title)

    def first_auction_domain_name_text(self):
        return self.get_text(self._first_auction_domain_name_field)

    def first_auction_buyer_login_text(self):
        return self.get_text(self._first_auction_buyer_login_field)

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