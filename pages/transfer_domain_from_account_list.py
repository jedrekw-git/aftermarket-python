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

    _submit_button = (By.XPATH, "//div[2]/button")
    _submit_confirm_button = (By.XPATH, "//div[3]/button")
    _result_field = (By.XPATH, "//td[3]")
    _stage2_result_field = (By.XPATH, "//label/div")
    _delete_first_transfer_domain_name_field = (By.XPATH, "//td[3]/div/span/label/span")
    _delete_first_transfer_delete_button = (By.XPATH, "//td[6]/div/a/img")
    _back_from_results_page = (By.XPATH, "//button")

    def __init__(self, driver):
        super(TransferDomainFromAccountList, self).__init__(driver, self._title)

    def stage2_domain_text(self):
        return self.get_text(self._stage2_domain_name_field)

    def cancel_all_domain_transfers_from_account(self):
        while True:
            if "https://assets-testy.aftermarket2.pl//img/table/icon/delete.svg" in self.get_page_source():
                self.click(self._delete_first_transfer_delete_button)
                WebDriverWait(self.get_driver(), 30).until(EC.text_to_be_present_in_element(self._stage2_result_field, u"Transfer zostanie anulowany"))
                self.click(self._submit_button)
                self.click(self._submit_confirm_button)
                WebDriverWait(self.get_driver(), 30).until(EC.text_to_be_present_in_element(self._result_field, u"Transfer domeny został anulowany"))
                self.click(self._back_from_results_page)
            else:
                break
