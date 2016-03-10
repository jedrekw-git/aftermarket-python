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

class AppraisalListPage(BasePage):
    _title = "Appraisal List"

    _fourth_appraisal_domain_field = (By.XPATH, "//tr[12]/td[3]/div/span/label/span")
    _fourth_appraisal_time_field = (By.XPATH, "//tr[12]/td[4]/div/span/span")
    _fourth_appraisal_type_field = (By.XPATH, "//tr[12]/td[5]/div/span")
    _fourth_appraisal_status_field = (By.XPATH, "//tr[12]/td[6]/div/span")
    _first_appraisal_domain_field = (By.XPATH, "//td[3]/div/span/label/span")
    _first_appraisal_time_field = (By.XPATH, "//td[4]/div/span/span")
    _first_appraisal_type_field = (By.XPATH, "//td[5]/div/span")
    _first_appraisal_status_field = (By.XPATH, "//td[6]/div/span")
    _search_field = (By.NAME, "domain")
    _search_button = (By.XPATH, "//div[3]/button")

    def __init__(self, driver):
        super(AppraisalListPage, self).__init__(driver, self._title)

    def search_for_appraisal(self, domain_name):
        self.clear_field_and_send_keys(domain_name, self._search_field)
        self.click(self._search_button)

    def get_fourth_appraisal_domain_time_type_and_status(self):
        self.fourth_appraisal_domain = self.get_text(self._fourth_appraisal_domain_field)
        self.fourth_appraisal_time = self.get_text(self._fourth_appraisal_time_field)
        self.fourth_appraisal_type = self.get_text(self._fourth_appraisal_type_field)
        self.fourth_appraisal_status = self.get_text(self._fourth_appraisal_status_field)