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

class TaskList(BasePage):
    _title = "Task List"

    _option_index = randint(1, 15)
    _more_filters_button = (By.XPATH, "//button")
    _operation_type_dropdown = (By.XPATH, "//select")
    _option_xpath = (By.XPATH, "//option[%s]" % _option_index)
    _filter_list_submit = (By.XPATH, "//form/div[3]/button")
    _first_result = (By.XPATH, "//td[3]/div/span")

    def __init__(self, driver):
        super(TaskList, self).__init__(driver, self._title)

    def get_text_selected_option(self):
        self.click(self._more_filters_button)
        self.click(self._operation_type_dropdown)
        self.option_text = self.get_text(self._option_xpath)

    def select_operation_type(self):
        self.select_index_from_dropdown((self._option_index)-1, self._operation_type_dropdown)
        self.click(self._filter_list_submit)
        sleep(3)

    def first_result_text(self):
        return self.get_text(self._first_result)