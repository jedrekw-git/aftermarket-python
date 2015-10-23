# coding=utf-8
from selenium.webdriver.common.by import By
from pages.base import BasePage
from utils.utils import *
from random import randint
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


class RegisterDomainPage(BasePage):
    _title = "Register domain"

    _domain_name_field = (By.NAME, "domains")
    _domain_name_value = get_random_uuid(10)+".waw.pl"
    _check_domain_availability_button = (By.XPATH, "//button")
    _first_domain_checkbox = (By.XPATH, "/html/body/div[7]/div/div/form/div[1]/table/tbody/tr[1]/td[1]/div/label/input")
    _realization_method_immediately_radio = (By.XPATH, "/html/body/div[7]/div/div/form/div[10]/div[3]/div/label[1]/span[2]")
    _register_domain_button = (By.XPATH, "/html/body/div[7]/div/div/form/div[11]/div[3]/button[2]")
    _registration_effect_text_field = (By.XPATH, "/html/body/div[7]/div/div/form/div[1]/table/tbody/tr[1]/td[3]")
    _first_domain = (By.XPATH, "//input[@value='%s']" %_domain_name_value)
    _domain_status_field = (By.XPATH, "/html/body/div[7]/div/div/form/div[1]/table/tbody/tr[1]/td[3]/label/span")

    def __init__(self, driver):
        super(RegisterDomainPage, self).__init__(driver, self._title)

    def enter_domain_to_register(self):
        self.clear_field_and_send_keys(self._domain_name_value, self._domain_name_field)
        self.click(self._check_domain_availability_button)

    def register_domain(self):
        # self.check(self._first_domain_checkbox)
        self.click(self._realization_method_immediately_radio)
        sleep(3)
        self.click(self._register_domain_button)
        sleep(3)
        self.accept_alert()





