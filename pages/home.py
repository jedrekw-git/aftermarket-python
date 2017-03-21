# coding=utf-8
from pages.base import BasePage
from time import sleep
from selenium.webdriver.common.by import By

class HomePage(BasePage):
    _title = "Strona główna"
    _url = "https://devel:miodzio@testy.aftermarket2.pl/"
    _language_dropdown = (By.XPATH, "//li[5]/a")
    _language_polish = (By.XPATH, "//li[5]/div/div/div/a")

    def __init__(self, driver):
        super(HomePage, self).__init__(driver, self._title, self._url)

    def open_home_page(self):
        self.get(self._url)
        self.is_the_current_page()
        self.click(self._language_dropdown)
        self.click(self._language_polish)
        return self