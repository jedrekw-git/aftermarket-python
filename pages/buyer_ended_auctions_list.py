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

class BuyerEndedAuctionsList(BasePage):
    _title = "Buyer ended auctions list"

    _second_domain_checkbox = (By.XPATH, "//tr[9]/td[3]/div/span/label/span")
    _second_domain_price_field = (By.XPATH, "//tr[9]/td[6]/div/span/b/span")
    _first_domain_checkbox = (By.XPATH, "//td[3]/div/span/label/span")
    _first_domain_price_field = (By.XPATH, "//span/b/span")
    _search_field = (By.NAME, "domain")
    _search_button = (By.XPATH, "//div[3]/button")

    def __init__(self, driver):
        super(BuyerEndedAuctionsList, self).__init__(driver, self._title)

    def get_second_domain_and_price_text(self):
        self._second_domain_text = self.get_text(self._second_domain_checkbox)
        self._second_domain_price_text = self.get_text(self._second_domain_price_field)

    def search_for_domain(self, domain_name):
        self.clear_field_and_send_keys(domain_name, self._search_field)
        self.click(self._search_button)