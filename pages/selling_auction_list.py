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

    _first_auction_delete_button = (By.XPATH, "//td[11]/div/span/img")
    _submit_button = (By.XPATH, "//button[2]")
    _back_from_results_page_button = (By.XPATH, "//button")

    def __init__(self, driver):
        super(SellingAuctionListPage, self).__init__(driver, self._title)

    def delete_first_auction(self):
        self.click(self._first_auction_delete_button)

    def delete_auction_submit(self):
        self.click(self._submit_button)
        self.accept_alert()

    def back_from_results_page(self):
        self.click(self._back_from_results_page_button)