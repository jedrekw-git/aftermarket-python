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

class TransferDomainFromAccountList(BasePage):
    _title = "Transfer domain from account"

    _submit_button = (By.XPATH, "//button[2]")

    _stage2_result_field = (By.XPATH, "/html/body/div[7]/div/div/form/div[1]/table/tbody/tr[1]/td[3]/label/span")
    _stage2_domain_name_field = (By.XPATH, "/html/body/div[7]/div/div/form/div[1]/table/tbody/tr[1]/td[2]/label/span")
    _delete_first_transfer_domain_name_field = (By.XPATH, "//td[3]/div/span/label/span")
    _delete_first_transfer_delete_button = (By.XPATH, "//td/div/button")

    def __init__(self, driver):
        super(TransferDomainFromAccountList, self).__init__(driver, self._title)

    def stage2_domain_text(self):
        return self.get_text(self._stage2_domain_name_field)

    def submit_and_accept_alert(self):
        self.click(self._submit_button)
        self.accept_alert()

    def cancel_first_domain_transfer(self):
        self.click(self._delete_first_transfer_domain_name_field)
        self.click(self._delete_first_transfer_delete_button)