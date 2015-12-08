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

class ExpiringDomainsList(BasePage):
    _title = "Expiring Domains List"

    _first_domain_checkbox = (By.XPATH, "//td[4]/div/span/label/span")
    _catch_first_domain_button = (By.XPATH, "//button[2]")
    _result_domain_name_field = (By.XPATH, "/html/body/div[7]/div/div/form/div[2]/table/tbody/tr[1]/td[2]/span")
    _result_text_field = (By.XPATH, "/html/body/div[7]/div/div/form/div[2]/table/tbody/tr[1]/td[3]")

    def __init__(self, driver):
        super(ExpiringDomainsList, self).__init__(driver, self._title)

    def catch_first_domain(self):
        self.click(self._first_domain_checkbox)
        self.click(self._catch_first_domain_button)

    def first_domain_text(self):
        self._first_domain_text_value = self.get_text(self._first_domain_checkbox)

    def result_domain_text(self):
        return self.get_text(self._result_domain_name_field)

