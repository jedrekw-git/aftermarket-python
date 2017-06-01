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

class ControlsTestPage(BasePage):
    _title = "Controls Test Page"

    _submit_values_button = (By.XPATH, "//button[@type='submit']")
    _1_text_field = (By.NAME, "text1")
    _2_text_field = (By.NAME, "text2")
    _1_number_field = (By.NAME, "number1")
    _2_number_field = (By.NAME, "number2")
    _1_amount_field = (By.NAME, "amount1")
    _2_amount_field = (By.NAME, "amount1")
    _1_email_field = (By.NAME, "email1")
    _2_email_field = (By.NAME, "email2")
    _1_url_field = (By.NAME, "url1")
    _2_url_field = (By.NAME, "url2")
    _1_text_error_field =
    _1_random_value = get_random_string(7)


    def __init__(self, driver):
        super(ControlsTestPage, self).__init__(driver, self._title)


    def submit_values(self):
        self.click(self._submit_values_button)

    def send_random_value_to_text2(self):
        self.clear_field_and_send_keys(self._1_random_value, self._2_text_field)
