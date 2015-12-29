# coding=utf-8
from selenium.webdriver.common.by import By
from pages.base import BasePage
from utils.utils import *
from random import randint
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


class RegisterOptionPage(BasePage):
    _title = "Register option"

    _submit_button = (By.XPATH, "//button[2]")
    _option_name_field = (By.NAME, "domains")
    _check_option_availability_button = (By.XPATH, "//button")
    _stage2_result_field = (By.XPATH, "/html/body/div[7]/div/div/form/div[1]/table/tbody/tr[1]/td[3]/label/span")
    _stage2_domain_name_field = (By.XPATH, "/html/body/div[7]/div/div/form/div[1]/table/tbody/tr[1]/td[2]/label/span")
    _stop_realization_until_manual_activation_radio = (By.XPATH, "//label[2]/span[2]")
    _cancel_domain_registration_button = (By.XPATH, "//td[5]/img")

    def __init__(self, driver):
        super(RegisterOptionPage, self).__init__(driver, self._title)

    def enter_option_to_register(self, option_name):
        self.clear_field_and_send_keys(option_name, self._option_name_field)
        self.click(self._check_option_availability_button)

    def stage2_domain_text(self):
        return self.get_text(self._stage2_domain_name_field)

    def submit_and_accept_alert(self):
        self.click(self._stop_realization_until_manual_activation_radio)
        self.click(self._submit_button)
        self.accept_alert()






