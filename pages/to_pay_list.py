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

class ToPayList(BasePage):
    _title = "To Pay List"

    _remove_first_payment_button = (By.XPATH, "//td[9]/div/a/img")
    _first_payment_title = (By.XPATH, "//td[4]/div/label/span")
    _first_payment_type = (By.XPATH, "//td[5]/div")
    _sumbit_first_payment_button = (By.XPATH, "//td[8]/div/img")

    def __init__(self, driver):
        super(ToPayList, self).__init__(driver, self._title)

    def remove_first_payment(self):
        self.click(self._remove_first_payment_button)

    def remove_all_payments(self):
        while True:
            if "/assets/img/table/delete.svg" in self.get_page_source():
                self.click(self._remove_first_payment_button)
            else:
                break

    def submit_first_payment(self):
        self.click(self._sumbit_first_payment_button)