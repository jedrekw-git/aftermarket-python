# coding=utf-8
from selenium.webdriver.common.by import By
from pages.base import BasePage
from utils.utils import *
from random import randint
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


class RegisteredDomainsListPage(BasePage):
    _title = "Registered domains"

    _first_domain_checkbox = (By.XPATH, "//td[3]/span/label/span")
    _renew_button = (By.XPATH, "//div[7]/div/button")
    _renew_automatically_button = (By.XPATH, "//div[7]/div/div/div/div[2]")
    _renew_automatically_when_money_on_account_radio = (By.XPATH, "//div[3]/div/label")
    _renew_automatically_send_email_after_operation_radio = (By.XPATH, "/html/body/div[7]/div/div/form/div[4]/div[3]/div/label[1]/span[2]")
    _renew_automatically_change_renewal_submit_button = (By.XPATH, "//button[2]")
    _renew_automatically_result_text_field = (By.XPATH, "/html/body/div[7]/div/div/form/div[2]/table/tbody/tr[1]/td[3]")
    _renew_automatically_result_domain_name_field = (By.XPATH, "/html/body/div[7]/div/div/form/div[2]/table/tbody/tr[1]/td[2]/span")
    _renew_manually_button = (By.XPATH, "//div[7]/div/div/div/div")
    _renew_manually_second_stage_domain_name_field = (By.XPATH, "/html/body/div[7]/div/div/form/div[1]/table/tbody/tr[1]/td[2]/label/span")
    _renew_manually_second_stage_text_field = (By.XPATH, "/html/body/div[7]/div/div/form/div[1]/table/tbody/tr[1]/td[3]/label/span")
    _renew_manually_send_email_after_oparation_radio = (By.XPATH, "/html/body/div[7]/div/div/form/div[2]/div[3]/div/label[1]/span[2]")
    _renew_manually_realize_immediately_radio = (By.XPATH, "/html/body/div[7]/div/div/form/div[3]/div[3]/div/label[1]/span[2]")
    _renew_manually_submit_button = (By.XPATH, "//button[2]")
    _renew_manually_result_domain_name_field = (By.XPATH, "/html/body/div[7]/div/div/form/div[2]/table/tbody/tr[1]/td[2]/span")
    _renew_manually_result_text_field = (By.XPATH, "/html/body/div[7]/div/div/form/div[2]/table/tbody/tr[1]/td[3]")

    def __init__(self, driver):
        super(RegisteredDomainsListPage, self).__init__(driver, self._title)

    def renew_domain_automatically(self):
        self.click(self._first_domain_checkbox)
        self.click(self._renew_button)
        self.click(self._renew_automatically_button)
        self.click(self._renew_automatically_when_money_on_account_radio)
        self.click(self._renew_automatically_send_email_after_operation_radio)
        self.click(self._renew_automatically_change_renewal_submit_button)

    def renew_automatically_result_domain_text(self):
        return self.get_text(self._renew_automatically_result_domain_name_field)

    def first_domain_text(self):
        self._first_domain_text_value = self.get_text(self._first_domain_checkbox)

    def select_first_domain_renew_manually(self):
        self.click(self._first_domain_checkbox)
        self.click(self._renew_button)
        self.click(self._renew_manually_button)

    def renew_manually_second_stage_domain_text(self):
        return self.get_text(self._renew_manually_second_stage_domain_name_field)

    def renew_manually_checkboxes_and_submit(self):
        self.click(self._renew_manually_send_email_after_oparation_radio)
        self.click(self._renew_manually_realize_immediately_radio)
        self.click(self._renew_manually_submit_button)
        self.accept_alert()

    def renew_manually_result_domain_text(self):
        return self.get_text(self._renew_manually_result_domain_name_field)

    def renew_manually_result_text(self):
        return self.get_text(self._renew_manually_result_text_field)



