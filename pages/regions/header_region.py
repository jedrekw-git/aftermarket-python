from selenium.webdriver.common.by import By
from pages.settings import SettingsPage
from pages.register_domain import RegisterDomainPage
from pages.registered_domains_list import RegisteredDomainsListPage
from pages.selling_auction_list import SellingAuctionListPage
from pages.page import Page
from pages.escrow_auction_list import EscrowAuctionListPage
from pages.transfer_domain_to_account_list import TransferDomainToAccountList
from pages.transfer_domain_from_account_list import TransferDomainFromAccountList
from pages.profile_for_domain_registration_list import ProfileForDomainRegistrationList
from pages.register_option import RegisterOptionPage
from pages.registered_options_list import RegisteredOptionsListPage
from pages.watched_domains_list import WatchedDomainsListPage
from pages.watched_sellers_list import WatchedSellersListPage
from pages.escrow_option_transaction import OptionEscrowTransactionList
from pages.blocked_sellers_list import BlockedSellersListPage
from pages.expiring_domains_list import ExpiringDomainsList
from pages.domains_to_catch_list import DomainsToCatchList
from pages.hosting_account_list import HostingAccountList
from pages.to_pay_list import ToPayList
from pages.transfer_option_to_account_list import TransferOptionToAccountList

class HeaderRegion(Page):
    _login_menu = (By.XPATH, "//button[2]")
    _login_field = (By.NAME, "login")
    _password_field = (By.NAME, "password")
    _login_button = (By.XPATH, "//div[4]/button")
    _base_url = "http://www.testy.aftermarket2.pl/"
    _logout_button = (By.PARTIAL_LINK_TEXT, "Wyloguj")

    _domain_menu = (By.XPATH, "//a[contains(@onclick,'domains')]")
    _domain_search_button = (By.XPATH, "//div[@id='menu_domains']//input[contains(@src, 'search.png')]")

    def login(self, login, password):
        self.click(self._login_menu)
        self.send_keys(login, self._login_field)
        self.send_keys(password, self._password_field)
        self.click(self._login_button)
        from pages.account import AccountPage
        return AccountPage(self.get_driver())

    def logout(self):
        self.click(self._logout_button)

    def open_settings_page(self):
        self.get(self._base_url + "User/Settings/")
        return SettingsPage(self.get_driver())

    def open_register_domain_page(self):
        self.get(self._base_url + "Domain/Check/")
        return RegisterDomainPage(self.get_driver())

    def open_registered_domains_list(self):
        self.get(self._base_url + "Domain/List/")
        return RegisteredDomainsListPage(self.get_driver())

    def open_selling_auction_list(self):
        self.get(self._base_url + "Auction/Seller/List/")
        return SellingAuctionListPage(self.get_driver())

    def open_escrow_transactions_list(self):
        self.get(self._base_url + "Escrow/Seller/List/")
        return EscrowAuctionListPage(self.get_driver())

    def open_transfer_domain_to_account_list(self):
        self.get(self._base_url + "Transfer/List/")
        return TransferDomainToAccountList(self.get_driver())

    def open_transfer_domain_from_account_list(self):
        self.get(self._base_url + "Intransfer/List/")
        return TransferDomainFromAccountList(self.get_driver())

    def open_profile_for_domain_registration_list(self):
        self.get(self._base_url + "Profile/List/")
        return ProfileForDomainRegistrationList(self.get_driver())

    def open_register_option_page(self):
        self.get(self._base_url + "Future/Check/")
        return RegisterOptionPage(self.get_driver())

    def open_registered_options_list(self):
        self.get(self._base_url + "Future/List/")
        return RegisteredOptionsListPage(self.get_driver())

    def open_internal_option_transfer_list(self):
        self.get(self._base_url + "Intransferfuture/List/")
        return RegisteredOptionsListPage(self.get_driver())

    def open_watched_domains_list(self):
        self.get(self._base_url + "Watch/Domain/List/")
        return WatchedDomainsListPage(self.get_driver())

    def open_watched_sellers_list(self):
        self.get(self._base_url + "Watch/User/List/")
        return WatchedSellersListPage(self.get_driver())

    def open_escrow_option_transaction_list(self):
        self.get(self._base_url + "Escrowfuture/Seller/List/")
        return OptionEscrowTransactionList(self.get_driver())

    def open_blocked_sellers_list(self):
        self.get(self._base_url + "Selling/Banned/List/")
        return BlockedSellersListPage(self.get_driver())

    def open_expiring_domains_list(self):
        self.get(self._base_url + "Deleted/List/")
        return ExpiringDomainsList(self.get_driver())

    def open_domains_to_catch_list(self):
        self.get(self._base_url + "Catch/List/")
        return DomainsToCatchList(self.get_driver())

    def open_hosting_account_list(self):
        self.get(self._base_url + "Hosting/List/")
        return HostingAccountList(self.get_driver())

    def open_to_pay_list(self):
        self.get(self._base_url + "Topay/List/")
        return ToPayList(self.get_driver())

    def open_transfer_option_to_account_list(self):
        self.get(self._base_url + "Transferfuture/List/")
        return TransferOptionToAccountList(self.get_driver())

