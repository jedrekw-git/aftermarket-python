from selenium.webdriver.common.by import By
from pages.settings import SettingsPage
from pages.register_domain import RegisterDomainPage
from pages.registered_domains_list import RegisteredDomainsListPage
from pages.selling_auction_list import SellingAuctionListPage
from pages.page import Page
from pages.escrow_auction_seller_list import EscrowAuctionSellerListPage
from pages.escrow_auction_buyer_list import EscrowAuctionBuyerListPage
from pages.transfer_domain_to_account_list import TransferDomainToAccountList
from pages.transfer_domain_from_account_list import TransferDomainFromAccountList
from pages.profile_for_domain_registration_list import ProfileForDomainRegistrationList
from pages.register_option import RegisterOptionPage
from pages.registered_options_list import RegisteredOptionsListPage
from pages.watched_domains_list import WatchedDomainsListPage
from pages.watched_sellers_list import WatchedSellersListPage
from pages.escrow_option_selling_transaction import OptionEscrowSellingTransactionList
from pages.escrow_option_buying_transaction import OptionEscrowBuyingTransactionList
from pages.blocked_sellers_list import BlockedSellersListPage
from pages.expiring_domains_list import ExpiringDomainsList
from pages.domains_to_catch_list import DomainsToCatchList
from pages.hosting_account_list import HostingAccountList
from pages.to_pay_list import ToPayList
from pages.transfer_option_to_account_list import TransferOptionToAccountList
from pages.domains_on_marketplace_list import DomainsOnMarketplaceList
from pages.expired_options_list import ExpiredOptionsList
from pages.task_list import TaskList
from pages.selling_history_list import SellingHistoryPage
from pages.new_option_auction import NewOptionAuctionPage
from pages.seller_ended_auctions_list import SellerEndedAuctionsList
from pages.buyer_ended_auctions_list import BuyerEndedAuctionsList
from pages.rental_buyer_list import RentalBuyerList
from pages.rental_seller_list import RentalSellerList
from pages.hire_buyer_list import HireBuyerList
from pages.hire_seller_list import HireSellerList
from pages.monitor_domains_list import MonitorDomainsList
from pages.domain_catalog_list import DomainCatalogList
from pages.appraisal_list import AppraisalListPage
from pages.active_appraisals_list import ActiveAppraisalsListPage
from pages.home import HomePage
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class HeaderRegion(Page):
    _login_menu = (By.XPATH, "//button[3]")
    _login_field = (By.NAME, "login")
    _password_field = (By.NAME, "password")
    _login_button = (By.XPATH, "//div[4]/button")
    _base_url = HomePage._url
    _settings_button = (By.XPATH, "//a[2]/div/img")
    _logout_button = (By.PARTIAL_LINK_TEXT, "Wyloguj")
    _remind_password_button = (By.XPATH, "//div[4]/div/a")
    _remind_password_login_field = (By.XPATH, "//div[2]/div/input")
    _remind_password_submit = (By.XPATH, "//div[2]/div/button")

    _domain_menu = (By.XPATH, "//a[contains(@onclick,'domains')]")
    _domain_search_button = (By.XPATH, "//div[@id='menu_domains']//input[contains(@src, 'search.png')]")

    def login(self, login, password):
        self.click(self._login_menu)
        WebDriverWait(self.get_driver(), 10).until(EC.visibility_of_element_located(self._login_field))
        self.send_keys(login, self._login_field)
        self.send_keys(password, self._password_field)
        self.click(self._login_button)
        from pages.account import AccountPage
        return AccountPage(self.get_driver())

    def logout(self):
        self.click(self._settings_button)
        self.click(self._logout_button)

    def remind_password(self, login):
        self.click(self._login_menu)
        self.click(self._remind_password_button)
        self.send_keys(login, self._remind_password_login_field)
        self.click(self._remind_password_submit)
        from pages.account import AccountPage
        return AccountPage(self.get_driver())

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

    def open_escrow_transactions_seller_list(self):
        self.get(self._base_url + "Escrow/Seller/List/")
        return EscrowAuctionSellerListPage(self.get_driver())

    def open_escrow_transactions_buyer_list(self):
        self.get(self._base_url + "Escrow/Buyer/List/")
        return EscrowAuctionBuyerListPage(self.get_driver())

    def open_transfer_domain_to_account_list(self):
        self.get(self._base_url + "Transfer/List/")
        return TransferDomainToAccountList(self.get_driver())

    def open_transfer_domain_from_account_list(self):
        self.get(self._base_url + "Intransfer/List/")
        return TransferDomainFromAccountList(self.get_driver())

    def open_profile_for_domain_registration_list(self):
        self.get(self._base_url + "Profile/List/")
        return ProfileForDomainRegistrationList(self.get_driver())

    def open_expired_options_list(self):
        self.get(self._base_url + "Future/OldList/")
        return ExpiredOptionsList(self.get_driver())

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

    def open_new_option_auction_page(self):
        self.get(self._base_url + "Auction/Seller/AddFuture/")
        return NewOptionAuctionPage(self.get_driver())

    def open_escrow_option_selling_transaction_list(self):
        self.get(self._base_url + "Escrowfuture/Seller/List/")
        return OptionEscrowSellingTransactionList(self.get_driver())

    def open_escrow_option_buying_transaction_list(self):
        self.get(self._base_url + "Escrowfuture/Buyer/List/")
        return OptionEscrowBuyingTransactionList(self.get_driver())

    def open_blocked_sellers_list(self):
        self.get(self._base_url + "Selling/Banned/List/")
        return BlockedSellersListPage(self.get_driver())

    def open_selling_history_list(self):
        self.get(self._base_url + "Selling/Sold/")
        return SellingHistoryPage(self.get_driver())

    def open_seller_ended_auctions_list(self):
        self.get(self._base_url + "Auction/Seller/Past/")
        return SellerEndedAuctionsList(self.get_driver())

    def open_buyer_ended_auctions_list(self):
        self.get(self._base_url + "Auction/Buyer/Past/")
        return BuyerEndedAuctionsList(self.get_driver())

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

    def open_domains_on_marketplace_list(self):
        self.get(self._base_url + "Market/List/")
        return DomainsOnMarketplaceList(self.get_driver())

    def open_subscriptions_on_marketplace_list(self):
        self.get(self._base_url + "Market/Subscriptions/")
        return DomainsOnMarketplaceList(self.get_driver())

    def open_task_list(self):
        self.get(self._base_url + "Task/List/")
        return TaskList(self.get_driver())

    def open_expiring_domains_subscriptions_list(self):
        self.get(self._base_url + "Deleted/Subscriptions/")
        return ExpiringDomainsList(self.get_driver())

    def open_rental_buyer_list(self):
        self.get(self._base_url + "Rental/Buyer/List/")
        return RentalBuyerList(self.get_driver())

    def open_rental_seller_list(self):
        self.get(self._base_url + "Rental/Seller/List/")
        return RentalSellerList(self.get_driver())

    def open_hire_buyer_list(self):
        self.get(self._base_url + "Hire/Buyer/List/")
        return HireBuyerList(self.get_driver())

    def open_hire_seller_list(self):
        self.get(self._base_url + "Hire/Seller/List/")
        return HireSellerList(self.get_driver())

    def open_monitor_domains_list(self):
        self.get(self._base_url + "Monitor/List/")
        return MonitorDomainsList(self.get_driver())

    def open_domain_catalog_list(self):
        self.get(self._base_url + "Catalog/List/")
        return DomainCatalogList(self.get_driver())

    def open_appraisal_list(self):
        self.get(self._base_url + "Appraisal/List/")
        return AppraisalListPage(self.get_driver())

    def open_active_appraisals_list(self):
        self.get(self._base_url + "Appraisal/Active/")
        return ActiveAppraisalsListPage(self.get_driver())