from selenium.webdriver.common.by import By
from pages.settings import SettingsPage
from pages.register_domain import RegisterDomainPage
from pages.page import Page

class HeaderRegion(Page):
    _login_menu = (By.XPATH, "//button[2]")
    _login_field = (By.NAME, "login")
    _password_field = (By.NAME, "password")
    _login_button = (By.XPATH, "//div[4]/button")
    _base_url = "http://testy.aftermarket2.pl/"

    _domain_menu = (By.XPATH, "//a[contains(@onclick,'domains')]")
    _domain_search_field = (By.NAME, "q")
    _domain_search_button = (By.XPATH, "//div[@id='menu_domains']//input[contains(@src, 'search.png')]")

    def login(self, login, password):
        self.click(self._login_menu)
        self.send_keys(login, self._login_field)
        self.send_keys(password, self._password_field)
        self.click(self._login_button)
        from pages.account import AccountPage
        return AccountPage(self.get_driver())

    def open_settings_page(self):
        self.get(self._base_url + "User/Settings/")
        return SettingsPage(self.get_driver())

    def open_register_domain_page(self):
        self.get(self._base_url + "Domain/Check/")
        return RegisterDomainPage(self.get_driver())