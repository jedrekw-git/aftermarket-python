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

class TransferDomainToAccountList(BasePage):
    _title = "Transfer domain to account"

    _add_new_domain_transfer_button = (By.XPATH, "//button")
    _submit_button = (By.XPATH, "//div[2]/button")
    _submit_confirm_button = (By.XPATH, "/html/body/div[10]/div/div[3]/button[1]")
    _transfer_submit_button = (By.XPATH, "//div[12]/div/div[2]/div[2]/button")
    _domain_name_field = (By.NAME, "domain")
    _authinfo_code_field = (By.NAME, "authinfo")
    _renew_1_year_radio = (By.XPATH, "//div[5]/div/div[2]/div/label[2]")
    _renew_without_renewal_radio = (By.XPATH, "//div[5]/div/div[2]/div/label")
    _stage2_result_field = (By.XPATH, "//label/div")
    _stage3_result_field = (By.XPATH, "//td[3]")
    _stage2_domain_name_field = (By.XPATH, "//td[2]/div/label/span")
    _stage2_change_DNS_servers_radio = (By.XPATH, "//label[2]/span[2]")
    _stage2_change_DNS_servers_dropdown = (By.NAME, "dns")
    _stage2_change_DNS_servers_index = randint(1, 5)
    _delete_first_transfer_domain_name_field = (By.XPATH, "//td[3]/div/span/label/span")
    _delete_first_transfer_delete_button = (By.XPATH, "//td[6]/div/a/img")
    _back_from_results_page_button = (By.XPATH, "//button")

    def __init__(self, driver):
        super(TransferDomainToAccountList, self).__init__(driver, self._title)

    def transfer_domain(self, domain, authinfo):
        self.click(self._add_new_domain_transfer_button)
        self.clear_field_and_send_keys(domain, self._domain_name_field)
        self.clear_field_and_send_keys(authinfo, self._authinfo_code_field)
        self.click(self._renew_without_renewal_radio)
        self.click(self._submit_button)

    def transfer_domain_and_renew(self, domain, authinfo):
        self.click(self._add_new_domain_transfer_button)
        self.clear_field_and_send_keys(domain, self._domain_name_field)
        self.clear_field_and_send_keys(authinfo, self._authinfo_code_field)
        self.click(self._renew_1_year_radio)
        self.click(self._submit_button)

    def stage2_domain_text(self):
        return self.get_text(self._stage2_domain_name_field)

    def stage2_result_text(self):
        return self.get_text(self._stage2_result_field)

    def stage2_change_dns_servers_and_submit(self):
        self.click(self._stage2_change_DNS_servers_radio)
        self.select_index_from_dropdown(self._stage2_change_DNS_servers_index, self._stage2_change_DNS_servers_dropdown)
        self.click(self._transfer_submit_button)
        sleep(1)
        self.click(self._submit_confirm_button)

    def cancel_all_domain_transfers(self):
        while True:
            if "https://assets-testy.aftermarket2.pl//img/table/icon/delete.svg" in self.get_page_source():
                self.click(self._delete_first_transfer_delete_button)
                WebDriverWait(self.get_driver(), 30).until(EC.text_to_be_present_in_element(self._stage2_result_field, u"Transfer zostanie anulowany"))
                self.click(self._submit_button)
                sleep(1)
                self.click(self._submit_confirm_button)
                WebDriverWait(self.get_driver(), 30).until(EC.text_to_be_present_in_element(self._stage3_result_field, u"Transfer domeny został anulowany"))
                self.click(self._back_from_results_page_button)
            else:
                break
