# coding=utf-8
from selenium.webdriver.common.by import By
from pages.base import BasePage


class AccountPage(BasePage):
    _title = "Your account snapshot"

    # temporary solution, since it's a workaround
    _not_change_lang_radio = (By.XPATH, "//input[@name = 'lang' and @value='2']")
    _change_lang_button = (By.XPATH, "//input[@value = 'Set language »']")

    def __init__(self, driver):
        # temporary solution, since it's a workaround
        if driver.title == "Account data change":
            driver.find_element(*self._not_change_lang_radio).click()
            driver.find_element(*self._change_lang_button).click()

        super(AccountPage, self).__init__(driver, self._title)