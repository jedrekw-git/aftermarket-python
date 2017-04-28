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

class NewOptionAuctionPage(BasePage):
    _title = "New Option Auction"

    _option_name_field = (By.NAME, "domain")
    _choose_option_dropdown = (By.XPATH, "//div[2]/div/a")
    _option_name_field_first_option = (By.XPATH, "//label")
    _price_start_field = (By.NAME, "price_start")
    _price_start_value = randint(1, 20)
    _currency_dropdown = (By.NAME, "currency")
    _currency_value = randint(0, 3)
    _end_date_field = (By.NAME, "end_date")
    _end_date_index = randint(1, 29)
    _end_time_field = (By.NAME, "end_time")
    _end_time_index = randint(1, 22)
    _minimal_price_checkbox = (By.XPATH, "//div[5]/div/div[2]/div/label")
    _buy_now_price_checkbox = (By.XPATH, "//div[2]/div[2]/label")
    _auction_description_checkbox = (
        By.XPATH, "/html/body/div[7]/div/div/form/div[5]/div[3]/div[3]/label")
    _price_minimum_field = (By.NAME, "price_minimum")
    _price_minimum_value = randint(21, 40)
    _price_buynow_field = (By.NAME, "price_buynow")
    _price_buynow_value = randint(41, 60)
    _description_field = (By.XPATH, "//div[2]/div/div/div/p")
    _description_value = get_random_string(10) + " " + get_random_string(7) + " " + get_random_string(8)
    _submit_button = (By.XPATH, "//button[@type='submit']")
    _submit_confirm_button = (By.XPATH, "//div[3]/button")
    _realize_immediately_radio = (By.XPATH, "//label/span[2]")
    _result_domain_name_field = (By.XPATH, "//div/span")
    _result_text_field = (By.XPATH, "//td[3]/div")
    _stage2_result_domain_name_field = (By.XPATH, "//div/span")
    _stage2_result_text_field = (By.XPATH, "//td[3]/div")

    def __init__(self, driver):
        super(NewOptionAuctionPage, self).__init__(driver, self._title)

    def new_option_auction_enter_details(self):
        # self.click(self._option_name_field)
        # sleep(2)
        # self.click(self._option_name_field)
        self.click(self._choose_option_dropdown)
        sleep(2)
        self._option_name = self.get_text(self._option_name_field_first_option)
        self.click(self._option_name_field_first_option)
        self.clear_field_and_send_keys(self._price_start_value, self._price_start_field)
        self.select_index_from_dropdown(self._currency_value, self._currency_dropdown)
        self.select_index_from_dropdown(self._end_date_index, self._end_date_field)
        self.select_index_from_dropdown(self._end_time_index, self._end_time_field)
        self.click(self._minimal_price_checkbox)
        self.click(self._buy_now_price_checkbox)
        # self.click(self._auction_description_checkbox)
        self.clear_field_and_send_keys(self._price_minimum_value,
                                       self._price_minimum_field)
        self.clear_field_and_send_keys(self._price_buynow_value,
                                       self._price_buynow_field)
        # self.clear_field_and_send_keys(self._description_value, self._description_field)
        self.click(self._submit_button)

    def new_option_auction_stage_2_submit(self):
        self.get_driver().execute_script("window.scrollTo(1100, 800);")
        # self.click(self._realize_immediately_radio)
        self.click(self._submit_button)
        self.click(self._submit_confirm_button)

    def result_domain_text(self):
        return self.get_text(self._result_domain_name_field)

    def stage2_result_domain_text(self):
        return self.get_text(self._stage2_result_domain_name_field)