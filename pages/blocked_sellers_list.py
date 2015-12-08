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

class BlockedSellersListPage(BasePage):
    _title = "Blocked sellers"

    _block_seller_button = (By.XPATH, "//button")
    _block_seller_submit = (By.XPATH, "//button[2]")
    _seller_name_field = (By.NAME, "login")
    _note_field = (By.XPATH, "//div[3]/div/div/div")
    _note_value = get_random_string(10)+" "+get_random_string(7)
    _delete_first_seller_button = (By.XPATH, "//td[5]/div/span/img")

    def __init__(self, driver):
        super(BlockedSellersListPage, self).__init__(driver, self._title)

    def block_seller(self, seller_name):
        self.click(self._block_seller_button)
        self.clear_field_and_send_keys(seller_name, self._seller_name_field)
        self.clear_field_and_send_keys(self._note_value, self._note_field)
        self.click(self._block_seller_submit)

    def delete_first_seller(self):
        self.click(self._delete_first_seller_button)

    def delete_first_seller_submit(self):
        self.click(self._block_seller_submit)