# coding=utf-8
import unittest
from selenium import webdriver
from htmltestrunner import HTMLTestRunner
from unittestzero import Assert
from pages.home import HomePage
from utils.config import *
from utils.utils import *
from datetime import timedelta, date
from time import sleep
import os
from datetime import datetime
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from time import gmtime, strftime

SCREEN_DUMP_LOCATION = os.path.join(
    os.path.dirname(os.path.abspath(__file__)), 'screendumps'
)
run_locally = True

# @on_platforms(browsers)


class SmokeTest(unittest.TestCase):
    _internal_non_grouped_domain_text = 1

    def test_change_contact_data_should_succeed(self):

        home_page = HomePage(self.driver).open_home_page()
        account_page = home_page.header.login(USER, PASSWORD)
        settings_page = account_page.header.open_settings_page()
        change_contact_data_page = settings_page.open_change_contact_data_page()
        settings_page.fill_change_contact_data_form()
        settings_page.save_change_contact_data()

        Assert.contains(u"Poniższe dane wskazują osobę, z którą będziemy mogli skontaktować się w sprawach dotyczących twojego konta.", settings_page.get_page_source())
        Assert.contains("Operacja wykonana poprawnie", settings_page.get_page_source())
        Assert.contains(settings_page._change_contact_data_name_value, settings_page.change_contact_data_name_field_text())
        Assert.contains(settings_page._change_contact_data_address_value, settings_page.change_contact_data_address_field_text())
        Assert.contains(settings_page.change_contact_data_postalcode_field_text(), settings_page._change_contact_data_postalcode_value)
        Assert.contains(settings_page._change_contact_data_city_value, settings_page.change_contact_data_city_field_text())

    def test_change_notification_settings_should_succeed(self):
        home_page = HomePage(self.driver).open_home_page()
        account_page = home_page.header.login(USER, PASSWORD)
        settings_page = account_page.header.open_settings_page()
        change_notification_settings_page = settings_page.open_change_notification_settings_page()
        settings_page.change_notification_settings()
        settings_page.save_change_notification_settings()

#Brak informacji potwierdzającej

    def test_change_newsletter_settings_should_succeed(self):
        home_page = HomePage(self.driver).open_home_page()
        account_page = home_page.header.login(USER, PASSWORD)
        settings_page = account_page.header.open_settings_page()
        change_newsletter_settings_page = settings_page.open_change_newsletter_settings_page()
        settings_page.change_newsletter_settings()
        settings_page.save_change_notification_settings()

#Brak informacji potwierdzającej

    def test_add_email_address_should_succeed(self):
        home_page = HomePage(self.driver).open_home_page()
        account_page = home_page.header.login(USER, PASSWORD)
        settings_page = account_page.header.open_settings_page()
        add_email_page = settings_page.open_add_email_address_page()
        settings_page.add_email_address()

        Assert.equal(settings_page._add_email_address_value, settings_page.added_email_address_text())
        Assert.equal("Niepotwierdzony", settings_page.added_email_status_text())

        settings_page.remove_added_email_address()

        self.not_contains(settings_page._add_email_address_value, settings_page.get_page_source())
        self.not_contains("Niepotwierdzony", settings_page.get_page_source())

    def test_add_other_users_to_account_should_succeed(self):
        home_page = HomePage(self.driver).open_home_page()
        account_page = home_page.header.login(USER, PASSWORD)
        settings_page = account_page.header.open_settings_page()
        add_other_users_page = settings_page.open_add_other_users_page()
        settings_page.add_other_user()

        Assert.equal(settings_page._add_other_user_login_value, settings_page.added_user_login_text())
        Assert.equal(settings_page._add_other_user_description_value, settings_page.added_user_description_text())

        settings_page.add_other_user_change_priviledges()
#nie ma potwierdzenia

        settings_page.remove_added_user()

        self.not_contains(settings_page._add_other_user_login_value, settings_page.get_page_source())
        self.not_contains(settings_page._add_other_user_description_value, settings_page.get_page_source())

    def test_change_company_address_should_succeed(self):
        home_page = HomePage(self.driver).open_home_page()
        account_page = home_page.header.login(USER, PASSWORD)
        settings_page = account_page.header.open_settings_page()
        change_company_address_page = settings_page.open_change_company_data_page()
        settings_page.edit_company_address()

        Assert.contains("Operacja wykonana poprawnie", settings_page.edit_company_data_operation_successful_text())
        Assert.contains(settings_page.edit_company_data_zip_text(), settings_page._change_company_data_zip_value)
        Assert.equal(settings_page._change_company_data_street_value, settings_page.edit_company_data_street_text())
        Assert.equal(settings_page._change_company_data_city_value, settings_page.edit_company_data_city_text())

    def test_change_company_data_should_succeed(self):
        home_page = HomePage(self.driver).open_home_page()
        account_page = home_page.header.login(USER, PASSWORD)
        settings_page = account_page.header.open_settings_page()
        change_company_data_page = settings_page.open_change_company_data_page()
        settings_page.edit_company_data()

        Assert.contains(settings_page.edit_company_data_zip_text(), settings_page._change_company_data_zip_value)
        Assert.equal(settings_page._change_company_data_street_value, settings_page.edit_company_data_street_text())
        Assert.equal(settings_page._change_company_data_city_value, settings_page.edit_company_data_city_text())
        Assert.equal(settings_page._change_company_data_company_name_value, settings_page.edit_company_data_company_name_text())
        Assert.equal(settings_page._change_company_data_nip_value, settings_page.edit_company_data_nip_text())

    def test_add_new_bank_account_should_succeed(self):
        home_page = HomePage(self.driver).open_home_page()
        account_page = home_page.header.login(USER, PASSWORD)
        settings_page = account_page.header.open_settings_page()
        bank_accounts_page = settings_page.open_add_bank_account_page()
        settings_page.add_bank_account()

        Assert.contains("Lista kont bankowych", settings_page.get_page_source())
        Assert.contains(u"Na tej liście znajdują się konta bankowe, na które możesz zlecać wypłaty.", settings_page.get_page_source())
        Assert.contains("Oto lista twoich kont bankowych.", settings_page.get_page_source())
        Assert.equal(settings_page._add_bank_account_account_number_value, settings_page.added_bank_account_number_text())
        Assert.equal(settings_page._add_bank_account_account_name_value, settings_page.added_bank_account_name_text())

        settings_page.remove_added_bank_account()
        account_page.header.open_settings_page()
        settings_page.open_add_bank_account_page()

        Assert.contains("Lista kont bankowych", settings_page.get_page_source())
        Assert.contains(u"Na tej liście znajdują się konta bankowe, na które możesz zlecać wypłaty.", settings_page.get_page_source())
        Assert.contains("Oto lista twoich kont bankowych.", settings_page.get_page_source())
        Assert.contains(u"Brak zdefiniowanych kont bankowych", settings_page.get_page_source())
        self.not_contains(settings_page._add_bank_account_account_number_value, settings_page.get_page_source())
        self.not_contains(settings_page._add_bank_account_account_name_value, settings_page.get_page_source())

    def test_change_DNS_servers_should_succeed(self):
        home_page = HomePage(self.driver).open_home_page()
        account_page = home_page.header.login(USER, PASSWORD)
        settings_page = account_page.header.open_settings_page()
        dns_servers_page = settings_page.open_change_DNS_servers_page()
        settings_page.change_DNS_servers()

        Assert.equal("ns1.aftermarket.pl", settings_page.change_DNS_servers_DNS1_text())
        Assert.equal("ns2.aftermarket.pl", settings_page.change_DNS_servers_DNS2_text())
        Assert.equal(settings_page._change_DNS_servers_DNS3_value, settings_page.change_DNS_servers_DNS3_text())
        Assert.equal(settings_page._change_DNS_servers_DNS4_value, settings_page.change_DNS_servers_DNS4_text())
        Assert.equal("Operacja wykonana poprawnie", settings_page.change_DNS_servers_operation_successful_text())

    def test_new_DNS_profile_should_succeed(self):
        home_page = HomePage(self.driver).open_home_page()
        account_page = home_page.header.login(USER, PASSWORD)
        settings_page = account_page.header.open_settings_page()
        dns_profile_page = settings_page.open_new_DNS_profile_page()
        settings_page.new_DNS_profile()
        settings_page.new_DNS_entry()

        Assert.equal("Operacja wykonana poprawnie", settings_page.new_DNS_profile_successful_operation_text())
        Assert.equal(settings_page._new_DNS_profile_name_value, settings_page.new_DNS_profile_successtul_opertation_profile_text())
        Assert.equal(settings_page._new_DNS_profile_host_value, settings_page.new_DNS_profile_successtul_opertation_host_text())
        Assert.equal(settings_page._new_DNS_profile_address_value, settings_page.new_DNS_profile_successtul_opertation_address_text())

        settings_page = account_page.header.open_settings_page()
        dns_profile_page = settings_page.open_new_DNS_profile_page()

        Assert.contains("Lista profili DNS", settings_page.get_page_source())
        Assert.equal(settings_page._new_DNS_profile_name_value, settings_page.new_DNS_profile_name_text())

        settings_page.delete_added_profile()

        self.not_contains(settings_page._new_DNS_profile_name_value, settings_page.get_page_source())

    def test_notification_about_ending_auctions_should_succeed(self):
        home_page = HomePage(self.driver).open_home_page()
        account_page = home_page.header.login(USER, PASSWORD)
        settings_page = account_page.header.open_settings_page()
        notification_page = settings_page.open_notifications_about_ending_auctions_page()
        settings_page.change_notifications_about_ending_auctions()

        Assert.contains("Operacja wykonana poprawnie", settings_page.get_page_source())

    def test_domain_watching_settings_should_succeed(self):
        home_page = HomePage(self.driver).open_home_page()
        account_page = home_page.header.login(USER, PASSWORD)
        settings_page = account_page.header.open_settings_page()
        domain_watching_settings__page = settings_page.open_domain_watching_settings_page()
        settings_page.change_domain_watching_settings()

        Assert.contains("Operacja wykonana poprawnie", settings_page.get_page_source())

    def test_sellers_watching_settings_should_succeed(self):
        home_page = HomePage(self.driver).open_home_page()
        account_page = home_page.header.login(USER, PASSWORD)
        settings_page = account_page.header.open_settings_page()
        sellers_watching_settings__page = settings_page.open_sellers_watching_settings_page()
        settings_page.change_sellers_watching_settings()

        Assert.contains("Operacja wykonana poprawnie", settings_page.get_page_source())

    def test_change_seller_profile_should_succeed(self):
        home_page = HomePage(self.driver).open_home_page()
        account_page = home_page.header.login(USER, PASSWORD)
        settings_page = account_page.header.open_settings_page()
        change_seller_profile__page = settings_page.open_change_seller_profile_page()
        settings_page.change_seller_profile()

        Assert.contains("Operacja wykonana poprawnie", settings_page.get_page_source())
        Assert.equal(settings_page._change_seller_profile_description_value, settings_page.change_seller_profile_description_text())

    def test_sending_notification_settings_should_succeed(self):
        home_page = HomePage(self.driver).open_home_page()
        account_page = home_page.header.login(USER, PASSWORD)
        settings_page = account_page.header.open_settings_page()
        sending_notification_settings_page = settings_page.open_sending_notification_settings_page()
        settings_page.change_sending_notification_settings()

        Assert.contains("Operacja wykonana poprawnie", settings_page.get_page_source())

    def test_register_domain_should_succeed(self):
        home_page = HomePage(self.driver).open_home_page()
        account_page = home_page.header.login(USER_DELTA, PASSWORD_DELTA)
        register_domain_page = account_page.header.open_register_domain_page()
        register_domain_page.enter_domain_to_register()

        WebDriverWait(self.driver, 30).until(EC.text_to_be_present_in_element(register_domain_page._domain_status_field, u"Dostępna do rejestracji"))

        register_domain_page.register_domain()

        WebDriverWait(self.driver, 20).until(EC.text_to_be_present_in_element(register_domain_page._registration_effect_domain_field, register_domain_page._domain_name_value))
        WebDriverWait(self.driver, 20).until(EC.text_to_be_present_in_element(register_domain_page._registration_effect_text_field, u"Domena zarezerwowana i oczekuje na opłacenie"))

        to_pay_list = account_page.header.open_to_pay_list()

        WebDriverWait(self.driver, 30).until(EC.text_to_be_present_in_element(to_pay_list._first_payment_title, register_domain_page._domain_name_value))
        WebDriverWait(self.driver, 30).until(EC.text_to_be_present_in_element(to_pay_list._first_payment_type, u"Rejestracja domeny"))

        to_pay_list.remove_first_payment()

        self.not_contains(register_domain_page._domain_name_value, to_pay_list.get_page_source())
        self.not_contains(u"Rejestracja domeny", to_pay_list.get_page_source())

    def test_renew_domain_automatically_should_succeed(self):
        home_page = HomePage(self.driver).open_home_page()
        account_page = home_page.header.login(USER_DELTA, PASSWORD_DELTA)
        registered_domains_page = account_page.header.open_registered_domains_list()
        registered_domains_page.first_domain_text()
        registered_domains_page.select_first_domain()
        registered_domains_page.renew_domain_automatically()

        WebDriverWait(self.driver, 30).until(EC.text_to_be_present_in_element(registered_domains_page._result_text_field, u"Operacja wykonana poprawnie"))
        Assert.equal(registered_domains_page._first_domain_text_value, registered_domains_page.result_domain_text())

    def test_renew_domain_manually_should_succeed(self):
        home_page = HomePage(self.driver).open_home_page()
        account_page = home_page.header.login(USER_DELTA, PASSWORD_DELTA)
        registered_domains_page = account_page.header.open_registered_domains_list()
        registered_domains_page.first_domain_text()
        registered_domains_page.select_first_domain()
        registered_domains_page.renew_domain_manually()

        WebDriverWait(self.driver, 30).until(EC.text_to_be_present_in_element(registered_domains_page._second_stage_text_field, u"Domena zostanie odnowiona"))
        Assert.equal(registered_domains_page._first_domain_text_value, registered_domains_page.second_stage_domain_text())

        registered_domains_page.second_stage_checkboxes_and_submit()

        if (WebDriverWait(self.driver, 30).until(EC.text_to_be_present_in_element(registered_domains_page._result_text_field, u"Operacja zawieszona, oczekuje na aktywowanie")))==True:
            Assert.equal(registered_domains_page._first_domain_text_value, registered_domains_page.result_domain_text())
        else:
            WebDriverWait(self.driver, 30).until(EC.text_to_be_present_in_element(registered_domains_page._result_text_field, u"Domena już była odnowiona w ostatnim okresie: "))
            Assert.equal(registered_domains_page._first_domain_text_value, registered_domains_page.result_domain_text())

        to_pay_list = account_page.header.open_to_pay_list()

        WebDriverWait(self.driver, 30).until(EC.text_to_be_present_in_element(to_pay_list._first_payment_title, registered_domains_page._first_domain_text_value))
        WebDriverWait(self.driver, 30).until(EC.text_to_be_present_in_element(to_pay_list._first_payment_type, u"Odnowienie domeny"))

        to_pay_list.remove_first_payment()

        self.not_contains(registered_domains_page._first_domain_text_value, to_pay_list.get_page_source())
        self.not_contains(u"Odnowienie domeny", to_pay_list.get_page_source())

    def test_change_profile_data_should_succeed(self):
        home_page = HomePage(self.driver).open_home_page()
        account_page = home_page.header.login(USER_DELTA, PASSWORD_DELTA)
        registered_domains_page = account_page.header.open_registered_domains_list()
        registered_domains_page.fourth_domain_text()
        registered_domains_page.select_fourth_domain()
        registered_domains_page.change_profile_data()

        if (WebDriverWait(self.driver, 30).until(EC.text_to_be_present_in_element(registered_domains_page._result_text_field, u"Operacja wykonana poprawnie")))==True:
            Assert.equal(registered_domains_page._fourth_domain_text_value, registered_domains_page.result_domain_text())
        else:
            WebDriverWait(self.driver, 30).until(EC.text_to_be_present_in_element(registered_domains_page._result_text_field, u"Domena jest zablokowana:"))
            Assert.equal(registered_domains_page._fourth_domain_text_value, registered_domains_page.result_domain_text())

    def test_privacy_settings_should_succeed(self):
        home_page = HomePage(self.driver).open_home_page()
        account_page = home_page.header.login(USER_DELTA, PASSWORD_DELTA)
        registered_domains_page = account_page.header.open_registered_domains_list()
        registered_domains_page.first_domain_text()
        registered_domains_page.select_first_domain()
        registered_domains_page.privacy_settings_first_stage()

        WebDriverWait(self.driver, 30).until(EC.text_to_be_present_in_element(registered_domains_page._second_stage_text_field, u"Dane abonenta będą widoczne"))
        Assert.equal(registered_domains_page._first_domain_text_value, registered_domains_page.second_stage_domain_text())

        registered_domains_page.second_stage_checkboxes_and_submit()

        WebDriverWait(self.driver, 30).until(EC.text_to_be_present_in_element(registered_domains_page._result_text_field, u"Operacja wykonana poprawnie"))
        Assert.equal(registered_domains_page._first_domain_text_value, registered_domains_page.result_domain_text())

    def test_get_authinfo_should_succeed(self):
        home_page = HomePage(self.driver).open_home_page()
        account_page = home_page.header.login(USER_DELTA, PASSWORD_DELTA)
        registered_domains_page = account_page.header.open_registered_domains_list()
        registered_domains_page.fourth_domain_text()
        registered_domains_page.select_fourth_domain()
        registered_domains_page.get_authinfo()

        WebDriverWait(self.driver, 30).until(EC.text_to_be_present_in_element(registered_domains_page._result_text_field, u"Kod AuthInfo:"))
        Assert.equal(registered_domains_page._fourth_domain_text_value, registered_domains_page.result_domain_text())

    def test_move_domain_from_account_should_succeed(self):

        login = "alfa"

        home_page = HomePage(self.driver).open_home_page()
        account_page = home_page.header.login(USER_DELTA, PASSWORD_DELTA)
        registered_domains_page = account_page.header.open_registered_domains_list()
        registered_domains_page.second_domain_text()
        registered_domains_page.select_second_domain()
        registered_domains_page.move_domain_from_account(login)

        WebDriverWait(self.driver, 30).until(EC.text_to_be_present_in_element(registered_domains_page._result_text_field, u"Transfer został zainicjowany"))
        Assert.equal(registered_domains_page._second_domain_text_value, registered_domains_page.result_domain_text())

        transfer_domain_page = account_page.header.open_transfer_domain_from_account_list()
        transfer_domain_page.cancel_first_domain_transfer()

        WebDriverWait(self.driver, 30).until(EC.text_to_be_present_in_element(transfer_domain_page._stage2_result_field, u"Transfer zostanie anulowany"))
        Assert.equal(registered_domains_page._second_domain_text_value, transfer_domain_page.stage2_domain_text())

        transfer_domain_page.submit_and_accept_alert()

        WebDriverWait(self.driver, 30).until(EC.text_to_be_present_in_element(registered_domains_page._result_text_field, u"Transfer został anulowany"))
        Assert.equal(registered_domains_page._second_domain_text_value, registered_domains_page.result_domain_text())

        transfer_domain_page = account_page.header.open_transfer_domain_from_account_list()

        self.not_contains(registered_domains_page._second_domain_text_value, transfer_domain_page.get_page_source())


#SPRAWDZIC BO BYL BLAD BAZY DANYCH, A JUŻ CHYBA NIE MA

    def test_change_DNS_servers_for_selected_domain_should_succeed(self):
        home_page = HomePage(self.driver).open_home_page()
        account_page = home_page.header.login(USER_DELTA, PASSWORD_DELTA)
        registered_domains_page = account_page.header.open_registered_domains_list()
        registered_domains_page.fourth_domain_text()
        registered_domains_page.select_fourth_domain()
        registered_domains_page.change_dns_servers_for_selected_domain()

        WebDriverWait(self.driver, 30).until(EC.text_to_be_present_in_element(registered_domains_page._result_text_field, u"Operacja wykonana poprawnie"))
        Assert.equal(registered_domains_page._fourth_domain_text_value, registered_domains_page.result_domain_text())

    def test_change_redirection_direct_should_succeed(self):
        home_page = HomePage(self.driver).open_home_page()
        account_page = home_page.header.login(USER_DELTA, PASSWORD_DELTA)
        registered_domains_page = account_page.header.open_registered_domains_list()
        registered_domains_page.first_domain_text()
        registered_domains_page.select_first_domain()
        registered_domains_page.change_redirection_direct()

        WebDriverWait(self.driver, 30).until(EC.text_to_be_present_in_element(registered_domains_page._result_text_field, u"Operacja wykonana poprawnie"))
        Assert.equal(registered_domains_page._first_domain_text_value, registered_domains_page.result_domain_text())

    def test_change_redirection_hidden_should_succeed(self):
        home_page = HomePage(self.driver).open_home_page()
        account_page = home_page.header.login(USER_DELTA, PASSWORD_DELTA)
        registered_domains_page = account_page.header.open_registered_domains_list()
        registered_domains_page.first_domain_text()
        registered_domains_page.select_first_domain()
        registered_domains_page.change_redirection_hidden()

        WebDriverWait(self.driver, 30).until(EC.text_to_be_present_in_element(registered_domains_page._result_text_field, u"Operacja wykonana poprawnie"))
        Assert.equal(registered_domains_page._first_domain_text_value, registered_domains_page.result_domain_text())

    def test_change_redirection_ip_should_succeed(self):
        home_page = HomePage(self.driver).open_home_page()
        account_page = home_page.header.login(USER_DELTA, PASSWORD_DELTA)
        registered_domains_page = account_page.header.open_registered_domains_list()
        registered_domains_page.first_domain_text()
        registered_domains_page.select_first_domain()
        registered_domains_page.change_redirection_ip()

        WebDriverWait(self.driver, 30).until(EC.text_to_be_present_in_element(registered_domains_page._result_text_field, u"Operacja wykonana poprawnie"))
        Assert.equal(registered_domains_page._first_domain_text_value, registered_domains_page.result_domain_text())

    def test_change_dns_profile_should_succeed(self):

        home_page = HomePage(self.driver).open_home_page()
        account_page = home_page.header.login(USER_DELTA, PASSWORD_DELTA)
        registered_domains_page = account_page.header.open_registered_domains_list()
        registered_domains_page.first_domain_text()
        registered_domains_page.select_first_domain()
        registered_domains_page.change_dns_profile()

        WebDriverWait(self.driver, 30).until(EC.text_to_be_present_in_element(registered_domains_page._result_text_field, u"Operacja wykonana poprawnie"))
        Assert.equal(registered_domains_page._first_domain_text_value, registered_domains_page.result_domain_text())

    def test_new_dns_entry_for_selected_domain_should_succeed(self):

        home_page = HomePage(self.driver).open_home_page()
        account_page = home_page.header.login(USER_DELTA, PASSWORD_DELTA)
        registered_domains_page = account_page.header.open_registered_domains_list()
        registered_domains_page.first_domain_text()
        registered_domains_page.select_first_domain()
        registered_domains_page.new_dns_entry_for_senected_domain()

        self.not_contains(registered_domains_page._add_dns_entry_host_name_value, registered_domains_page.get_page_source())
        self.not_contains(registered_domains_page._add_dns_entry_address_value, registered_domains_page.get_page_source())

        registered_domains_page.new_dns_entry_for_senected_domain_details()

        Assert.contains("Operacja wykonana poprawnie", registered_domains_page.get_page_source())

        registered_domains_page = account_page.header.open_registered_domains_list()
        registered_domains_page.select_first_domain()
        registered_domains_page.new_dns_entry_for_senected_domain()

        Assert.contains(registered_domains_page._add_dns_entry_host_name_value, registered_domains_page.get_page_source())
        Assert.contains(registered_domains_page._add_dns_entry_priority_value, registered_domains_page.get_page_source())
        Assert.contains(registered_domains_page._add_dns_entry_address_value, registered_domains_page.get_page_source())

        registered_domains_page.delete_new_dns_entry_for_senected_domain()

        self.not_contains(registered_domains_page._add_dns_entry_host_name_value, registered_domains_page.get_page_source())
        self.not_contains(registered_domains_page._add_dns_entry_address_value, registered_domains_page.get_page_source())

    def test_new_dns_server_in_domain_should_succeed(self):

        home_page = HomePage(self.driver).open_home_page()
        account_page = home_page.header.login(USER_DELTA, PASSWORD_DELTA)
        registered_domains_page = account_page.header.open_registered_domains_list()
        registered_domains_page.first_domain_text()
        registered_domains_page.select_first_domain()
        registered_domains_page.dns_servers_in_domain()

        self.not_contains(registered_domains_page._new_dns_server_in_domain_name_value+"."+registered_domains_page._first_domain_text_value, registered_domains_page.get_page_source())
        self.not_contains(registered_domains_page._new_dns_server_in_domain_ip_value, registered_domains_page.get_page_source())

        registered_domains_page.new_dns_server_in_domain_details()

        Assert.contains(registered_domains_page._new_dns_server_in_domain_name_value+"."+registered_domains_page._first_domain_text_value, registered_domains_page.get_page_source())
        Assert.contains(registered_domains_page._new_dns_server_in_domain_ip_value, registered_domains_page.get_page_source())

        registered_domains_page.delete_new_dns_server_in_domain()

        self.not_contains(registered_domains_page._new_dns_server_in_domain_name_value+"."+registered_domains_page._first_domain_text_value, registered_domains_page.get_page_source())
        self.not_contains(registered_domains_page._new_dns_server_in_domain_ip_value, registered_domains_page.get_page_source())

    def test_change_parking_service_should_succeed(self):

        home_page = HomePage(self.driver).open_home_page()
        account_page = home_page.header.login(USER_DELTA, PASSWORD_DELTA)
        registered_domains_page = account_page.header.open_registered_domains_list()
        registered_domains_page.first_domain_text()
        registered_domains_page.select_first_domain()
        registered_domains_page.change_parking_service()

        WebDriverWait(self.driver, 30).until(EC.text_to_be_present_in_element(registered_domains_page._result_text_field, u"Operacja wykonana poprawnie"))
        Assert.equal(registered_domains_page._first_domain_text_value, registered_domains_page.result_domain_text())

    def test_change_keyword_should_succeed(self):

        home_page = HomePage(self.driver).open_home_page()
        account_page = home_page.header.login(USER_DELTA, PASSWORD_DELTA)
        registered_domains_page = account_page.header.open_registered_domains_list()
        registered_domains_page.first_domain_text()
        registered_domains_page.select_first_domain()
        registered_domains_page.change_keyword()

        sleep(10)
        if "Domena odnowiona poprawnie" in registered_domains_page.result_text():
            Assert.equal(registered_domains_page._first_domain_text_value, registered_domains_page._result_domain_text())
        else:
            WebDriverWait(self.driver, 30).until(EC.text_to_be_present_in_element(registered_domains_page._result_text_field, u"Domena nie jest zaparkowana"))
            Assert.equal(registered_domains_page._first_domain_text_value, registered_domains_page.result_domain_text())

    def test_sell_on_auction_should_succeed(self):

        home_page = HomePage(self.driver).open_home_page()
        account_page = home_page.header.login(USER_DELTA, PASSWORD_DELTA)
        registered_domains_page = account_page.header.open_registered_domains_list()
        registered_domains_page.second_domain_text()
        registered_domains_page.select_second_domain()
        registered_domains_page.sell_on_auction()

        Assert.equal(registered_domains_page._second_domain_text_value, registered_domains_page.sell_on_auction_stage2_domain_text())
        Assert.equal(u"Technologia » Komputery", registered_domains_page.sell_on_auction_stage2_category_text())

        registered_domains_page.sell_on_auction_submit()

        WebDriverWait(self.driver, 30).until(EC.text_to_be_present_in_element(registered_domains_page._result_text_field, u"Aukcja została wystawiona"))
        Assert.equal(registered_domains_page._second_domain_text_value, registered_domains_page.result_domain_text())

        selling_auction_page = account_page.header.open_selling_auction_list()
        selling_auction_page.delete_first_auction()

        WebDriverWait(self.driver, 30).until(EC.text_to_be_present_in_element(registered_domains_page._second_stage_text_field, u"Aukcja zostanie anulowana"))
        Assert.equal(registered_domains_page._second_domain_text_value, registered_domains_page.second_stage_domain_text())

        selling_auction_page.delete_auction_submit()

        WebDriverWait(self.driver, 30).until(EC.text_to_be_present_in_element(registered_domains_page._result_text_field, u"Aukcja została anulowana"))
        Assert.equal(registered_domains_page._second_domain_text_value, registered_domains_page.result_domain_text())

        selling_auction_page.back_from_results_page()

        self.not_contains(registered_domains_page._second_domain_text_value, selling_auction_page.get_page_source())

    def test_sell_on_escrow_auction_should_succeed(self):

        login_value = "alfa"
        price = get_random_integer(2)

        home_page = HomePage(self.driver).open_home_page()
        account_page = home_page.header.login(USER_DELTA, PASSWORD_DELTA)
        registered_domains_page = account_page.header.open_registered_domains_list()
        registered_domains_page.first_domain_text()
        registered_domains_page.select_first_domain()
        registered_domains_page.sell_on_escrow_auction(login_value, price)

        Assert.equal(registered_domains_page._first_domain_text_value, registered_domains_page.sell_on_auction_stage2_domain_text())
        Assert.contains(price, registered_domains_page.get_page_source())
        Assert.equal(login_value, registered_domains_page.sell_on_escrow_auction_stage2_buyer_login_text())

        registered_domains_page.sell_on_auction_submit()

        WebDriverWait(self.driver, 30).until(EC.text_to_be_present_in_element(registered_domains_page._result_text_field, u"Transakcja Escrow została zainicjowana"))
        Assert.equal(registered_domains_page._first_domain_text_value, registered_domains_page.result_domain_text())

        escrow_auction_page = account_page.header.open_escrow_transactions_list()

        Assert.equal(registered_domains_page._first_domain_text_value, escrow_auction_page.first_auction_domain_name_text())
        Assert.contains(price, escrow_auction_page.get_page_source())
        Assert.equal(login_value, escrow_auction_page.first_auction_buyer_login_text())

        escrow_auction_page.delete_first_escrow_auction()

        Assert.equal(registered_domains_page._first_domain_text_value, escrow_auction_page.delete_auction_domain_name_text())
        Assert.contains(price, escrow_auction_page.get_page_source())
        Assert.equal(login_value, escrow_auction_page.delete_auction_buyer_login_text())

        escrow_auction_page.delete_auction_submit()

        WebDriverWait(self.driver, 30).until(EC.text_to_be_present_in_element(registered_domains_page._result_text_field, u"Transakcja została anulowana"))
        Assert.equal(registered_domains_page._first_domain_text_value, registered_domains_page.result_domain_text())

    def test_add_on_marketplace_should_succeed(self):

        home_page = HomePage(self.driver).open_home_page()
        account_page = home_page.header.login(USER_DELTA, PASSWORD_DELTA)
        registered_domains_page = account_page.header.open_registered_domains_list()
        registered_domains_page.fourth_domain_text()
        registered_domains_page.select_fourth_domain()
        registered_domains_page.add_on_marketplace()

        WebDriverWait(self.driver, 30).until(EC.text_to_be_present_in_element(registered_domains_page._result_text_field, u"Dostępna na sprzedaż, cena Kup Teraz: "+registered_domains_page._add_on_marketplace_buynow_value))
        WebDriverWait(self.driver, 30).until(EC.text_to_be_present_in_element(registered_domains_page._result_text_field, u"cena minimalna: "+registered_domains_page._add_on_marketplace_minimum_price_value))
        Assert.equal(registered_domains_page._fourth_domain_text_value, registered_domains_page.result_domain_text())

    def test_delete_domain_should_succeed(self):
        home_page = HomePage(self.driver).open_home_page()
        account_page = home_page.header.login(USER_DELTA, PASSWORD_DELTA)
        registered_domains_page = account_page.header.open_registered_domains_list()
        registered_domains_page.fourth_domain_text()
        registered_domains_page.select_fourth_domain()
        registered_domains_page.delete_fourth_auction()

        WebDriverWait(self.driver, 30).until(EC.text_to_be_present_in_element(registered_domains_page._result_text_field, u"Operacja wykonana poprawnie"))
        Assert.equal(registered_domains_page._fourth_domain_text_value, registered_domains_page.result_domain_text())

    def test_transfer_domain_to_the_same_account_should_succeed(self):
        home_page = HomePage(self.driver).open_home_page()
        account_page = home_page.header.login(USER_DELTA, PASSWORD_DELTA)
        registered_domains_page = account_page.header.open_registered_domains_list()
        registered_domains_page.fourth_domain_text()
        registered_domains_page.select_fourth_domain()
        registered_domains_page.get_authinfo()

        WebDriverWait(self.driver, 30).until(EC.text_to_be_present_in_element(registered_domains_page._result_text_field, u"Kod AuthInfo:"))

        registered_domains_page.store_authinfo()
        transfer_domain_page = account_page.header.open_transfer_domain_to_account_list()
        transfer_domain_page.transfer_domain(registered_domains_page._fourth_domain_text_value, registered_domains_page._authinfo)

        WebDriverWait(self.driver, 30).until(EC.text_to_be_present_in_element(transfer_domain_page._stage2_result_field, u"Domena już znajduje się na twoim koncie"))
        Assert.equal(registered_domains_page._fourth_domain_text_value, transfer_domain_page.stage2_domain_text())

    def test_transfer_domain_to_the_other_account_should_succeed(self):
        home_page = HomePage(self.driver).open_home_page()
        account_page = home_page.header.login(USER_DELTA, PASSWORD_DELTA)
        registered_domains_page = account_page.header.open_registered_domains_list()
        registered_domains_page.fourth_domain_text()
        registered_domains_page.select_fourth_domain()
        registered_domains_page.get_authinfo()

        WebDriverWait(self.driver, 30).until(EC.text_to_be_present_in_element(registered_domains_page._result_text_field, u"Kod AuthInfo:"))

        registered_domains_page.store_authinfo()
        account_page = home_page.header.logout()
        account_page = home_page.header.login(USER, PASSWORD)
        transfer_domain_page = account_page.header.open_transfer_domain_to_account_list()
        transfer_domain_page.transfer_domain(registered_domains_page._fourth_domain_text_value, registered_domains_page._authinfo)

        WebDriverWait(self.driver, 30).until(EC.text_to_be_present_in_element(transfer_domain_page._stage2_result_field, u"Domena zostanie przeniesiona z innego konta"))
        Assert.equal(registered_domains_page._fourth_domain_text_value, transfer_domain_page.stage2_domain_text())

        transfer_domain_page.stage2_change_dns_servers()
        transfer_domain_page.submit_and_accept_alert()

        WebDriverWait(self.driver, 30).until(EC.text_to_be_present_in_element(registered_domains_page._result_text_field, u"Transfer domeny został zainicjowany"))
        Assert.equal(registered_domains_page._fourth_domain_text_value, registered_domains_page.result_domain_text())

        transfer_domain_page = account_page.header.open_transfer_domain_to_account_list()
        transfer_domain_page.cancel_first_domain_transfer()

        WebDriverWait(self.driver, 30).until(EC.text_to_be_present_in_element(transfer_domain_page._stage2_result_field, u"Transfer zostanie anulowany"))
        Assert.equal(registered_domains_page._fourth_domain_text_value, transfer_domain_page.stage2_domain_text())

        transfer_domain_page.submit_and_accept_alert()

        WebDriverWait(self.driver, 30).until(EC.text_to_be_present_in_element(registered_domains_page._result_text_field, u"Transfer został anulowany"))
        Assert.equal(registered_domains_page._fourth_domain_text_value, registered_domains_page.result_domain_text())

        transfer_domain_page = account_page.header.open_transfer_domain_to_account_list()

        self.not_contains(registered_domains_page._fourth_domain_text_value, transfer_domain_page.get_page_source())

    def test_add_profile_for_domain_registration_should_succeed(self):
        home_page = HomePage(self.driver).open_home_page()
        account_page = home_page.header.login(USER_DELTA, PASSWORD_DELTA)
        profile_list_page = account_page.header.open_profile_for_domain_registration_list()
        profile_list_page.register_new_profile()

        sleep(2)
        Assert.contains(profile_list_page._profile_name_value, profile_list_page.get_page_source())

        profile_list_page.delete_added_profile()

        WebDriverWait(self.driver, 30).until(EC.text_to_be_present_in_element(profile_list_page._result_text_field, u"Operacja wykonana poprawnie"))

        profile_list_page.back_from_results_page()

        self.not_contains(profile_list_page._profile_name_value, profile_list_page.get_page_source())

    def test_register_option_should_succeed(self):
        home_page = HomePage(self.driver).open_home_page()
        account_page = home_page.header.login(USER_DELTA, PASSWORD_DELTA)
        registered_domains_page = account_page.header.open_registered_domains_list()
        registered_domains_page.second_domain_text()
        register_option_page = account_page.header.open_register_option_page()
        register_option_page.enter_option_to_register(registered_domains_page._second_domain_text_value)

        WebDriverWait(self.driver, 30).until(EC.text_to_be_present_in_element(register_option_page._stage2_result_field, u"Dostępna do rejestracji"))
        Assert.equal(registered_domains_page._second_domain_text_value, register_option_page.stage2_domain_text())

        register_option_page.submit_and_accept_alert()

        WebDriverWait(self.driver, 30).until(EC.text_to_be_present_in_element(registered_domains_page._result_text_field, u"Operacja zawieszona, oczekuje na aktywowanie"))
        Assert.equal(registered_domains_page._second_domain_text_value, registered_domains_page.result_domain_text())

        to_pay_list = account_page.header.open_to_pay_list()

        WebDriverWait(self.driver, 30).until(EC.text_to_be_present_in_element(to_pay_list._first_payment_title, registered_domains_page._second_domain_text_value))
        WebDriverWait(self.driver, 30).until(EC.text_to_be_present_in_element(to_pay_list._first_payment_type, u"Rejestracja opcji"))

        to_pay_list.remove_first_payment()

        self.not_contains(registered_domains_page._second_domain_text_value, to_pay_list.get_page_source())
        self.not_contains(u"Rejestracja opcji", to_pay_list.get_page_source())

    def test_renew_option_should_succeed(self):
        home_page = HomePage(self.driver).open_home_page()
        account_page = home_page.header.login(USER_DELTA, PASSWORD_DELTA)
        registered_options_list = account_page.header.open_registered_options_list()
        registered_options_list.first_option_text()
        transfer_option = registered_options_list.renew_option()

        WebDriverWait(self.driver, 30).until(EC.text_to_be_present_in_element(registered_options_list._stage2_result_field, u"Opcja może być odnowiona"))
        Assert.equal(registered_options_list._first_option_text_value, registered_options_list.stage2_option_text())

        registered_options_list.second_stage_checkboxes_and_submit()

        if (WebDriverWait(self.driver, 30).until(EC.text_to_be_present_in_element(registered_options_list._result_text_field, u"Operacja zawieszona, oczekuje na aktywowanie")))==True:
            Assert.equal(registered_options_list._first_option_text_value, registered_options_list.result_domain_text())
        else:
            WebDriverWait(self.driver, 30).until(EC.text_to_be_present_in_element(registered_options_list._result_text_field, u"Domena już była odnowiona w ostatnim okresie: "))
            Assert.equal(registered_options_list._first_option_text_value, registered_options_list.result_domain_text())

        to_pay_list = account_page.header.open_to_pay_list()

        WebDriverWait(self.driver, 30).until(EC.text_to_be_present_in_element(to_pay_list._first_payment_title, registered_options_list._first_option_text_value))
        WebDriverWait(self.driver, 30).until(EC.text_to_be_present_in_element(to_pay_list._first_payment_type, u"Odnowienie opcji"))

        to_pay_list.remove_first_payment()

        self.not_contains(registered_options_list._first_option_text_value, to_pay_list.get_page_source())
        self.not_contains(u"Odnowienie opcji", to_pay_list.get_page_source())

    def test_transfer_option_from_account_should_succeed(self):
        login = "alfa"

        home_page = HomePage(self.driver).open_home_page()
        account_page = home_page.header.login(USER_GAMMA, PASSWORD_GAMMA)
        registered_options_list = account_page.header.open_registered_options_list()
        registered_options_list.first_option_text()
        transfer_option = registered_options_list.transfer_option_from_account()
        registered_options_list.transfer_option_enter_login(login)
        registered_options_list.submit()

        WebDriverWait(self.driver, 30).until(EC.text_to_be_present_in_element(registered_options_list._result_text_field, u"Transfer został zainicjowany"))
        Assert.equal(registered_options_list._first_option_text_value, registered_options_list.result_domain_text())

        account_page.header.open_internal_option_transfer_list()

        Assert.equal(registered_options_list._first_option_text_value, registered_options_list.transfer_list_first_domain_text())
        Assert.contains(u"Oczekujący", registered_options_list.get_page_source())

        registered_options_list.delete_first_transfer()

        WebDriverWait(self.driver, 30).until(EC.text_to_be_present_in_element(registered_options_list._stage2_result_field, u"Transfer zostanie anulowany"))
        Assert.equal(registered_options_list._first_option_text_value, registered_options_list.stage2_option_text())

        registered_options_list.submit_and_accept_alert()

        WebDriverWait(self.driver, 30).until(EC.text_to_be_present_in_element(registered_options_list._result_text_field, u"Transfer został anulowany"))
        Assert.equal(registered_options_list._first_option_text_value, registered_options_list.result_domain_text())

        account_page.header.open_internal_option_transfer_list()

        self.not_contains(registered_options_list._first_option_text_value, registered_options_list.get_page_source())
        self.not_contains(u"Oczekujący", registered_options_list.get_page_source())

    def test_transfer_option_to_account_should_succeed(self):

        home_page = HomePage(self.driver).open_home_page()
        account_page = home_page.header.login(USER_GAMMA, PASSWORD_GAMMA)
        registered_options_list = account_page.header.open_registered_options_list()
        registered_options_list.first_option_text()
        registered_options_list.get_option_authinfo()

        WebDriverWait(self.driver, 30).until(EC.text_to_be_present_in_element(registered_options_list._result_text_field, u"Kod AuthInfo:"))

        registered_options_list.store_option_authinfo()

        home_page.header.logout()
        account_page = home_page.header.login(USER_DELTA, PASSWORD_DELTA)
        transfer_option_list = account_page.header.open_transfer_option_to_account_list()
        transfer_option_list.new_option_transfer(registered_options_list._first_option_text_value, registered_options_list._option_authinfo)

        WebDriverWait(self.driver, 30).until(EC.text_to_be_present_in_element(registered_options_list._stage2_result_field, u"Opcja zostanie przeniesiona z innego konta"))
        Assert.equal(registered_options_list._first_option_text_value, registered_options_list.stage2_option_text())

        registered_options_list.submit_and_accept_alert()

        WebDriverWait(self.driver, 30).until(EC.text_to_be_present_in_element(registered_options_list._result_text_field, u"Transfer opcji został zainicjowany"))
        Assert.equal(registered_options_list._first_option_text_value, registered_options_list.result_domain_text())

        account_page.header.open_transfer_option_to_account_list()

        Assert.contains(registered_options_list._first_option_text_value, registered_options_list.get_page_source())
        Assert.contains(strftime("%Y-%m-%d", gmtime()), registered_options_list.get_page_source())
        Assert.contains(u"Oczekujący", registered_options_list.get_page_source())

        transfer_option_list.remove_first_transfer()

        WebDriverWait(self.driver, 30).until(EC.text_to_be_present_in_element(registered_options_list._stage2_result_field, u"Transfer zostanie anulowany"))
        Assert.equal(registered_options_list._first_option_text_value, registered_options_list.stage2_option_text())

        registered_options_list.submit_and_accept_alert()

        WebDriverWait(self.driver, 30).until(EC.text_to_be_present_in_element(registered_options_list._result_text_field, u"Transfer został anulowany"))
        Assert.equal(registered_options_list._first_option_text_value, registered_options_list.result_domain_text())

        account_page.header.open_transfer_option_to_account_list()

        self.not_contains(registered_options_list._first_option_text_value, registered_options_list.get_page_source())

    def test_new_hosting_account_should_succeed(self):

        home_page = HomePage(self.driver).open_home_page()
        account_page = home_page.header.login(USER_DELTA, PASSWORD_DELTA)
        hosting_account_list = account_page.header.open_hosting_account_list()
        hosting_account_list.new_hosting_account(PASSWORD_DELTA)

        Assert.equal("Pakiet Starter", hosting_account_list.get_text_packet_type_stage_2())
        Assert.equal(hosting_account_list._new_hosting_account_login_value, hosting_account_list.get_text_login_stage_2())

        hosting_account_list.new_hosting_account_stage_2()

        WebDriverWait(self.driver, 90).until(EC.text_to_be_present_in_element(hosting_account_list._new_hosting_account_result_text_field, u"Konto hostingowe zostało utworzone i aktywowane na okres próbny 14 dni."))

        to_pay_list = account_page.header.open_to_pay_list()

        WebDriverWait(self.driver, 30).until(EC.text_to_be_present_in_element(to_pay_list._first_payment_title, hosting_account_list._new_hosting_account_login_value))
        WebDriverWait(self.driver, 30).until(EC.text_to_be_present_in_element(to_pay_list._first_payment_type, u"Zamówienie serwera"))

        to_pay_list.remove_first_payment()

        self.not_contains(hosting_account_list._new_hosting_account_login_value, to_pay_list.get_page_source())
        self.not_contains(u"Zamówienie serwera", to_pay_list.get_page_source())

    def test_add_domain_to_hosting_account_should_succeed(self):

        home_page = HomePage(self.driver).open_home_page()
        account_page = home_page.header.login(USER_GAMMA, PASSWORD_GAMMA)
        registered_domains_page = account_page.header.open_registered_domains_list()
        registered_domains_page.first_domain_text()
        hosting_account_list = account_page.header.open_hosting_account_list()
        hosting_account_list.add_domains_to_hosting_account()
        hosting_account_list.add_domains_to_hosting_account_stage2(registered_domains_page._first_domain_text_value)

        WebDriverWait(self.driver, 30).until(EC.text_to_be_present_in_element(registered_domains_page._result_text_field, u"Operacja wykonana poprawnie"))
        Assert.equal(registered_domains_page._first_domain_text_value, registered_domains_page.result_domain_text())

        hosting_account_list.back_from_results_page()

        Assert.contains(registered_domains_page._first_domain_text_value, hosting_account_list.get_page_source())
        Assert.contains(strftime("%Y-%m-%d", gmtime()), hosting_account_list.get_page_source())

        hosting_account_list.remove_first_domain()

        WebDriverWait(self.driver, 30).until(EC.text_to_be_present_in_element(registered_domains_page._result_text_field, u"Operacja wykonana poprawnie"))
        Assert.equal(registered_domains_page._first_domain_text_value, registered_domains_page.result_domain_text())

        hosting_account_list.back_from_results_page()

        self.not_contains(registered_domains_page._first_domain_text_value, hosting_account_list.get_page_source())
        self.not_contains(strftime("%Y-%m-%d", gmtime()), hosting_account_list.get_page_source())

    def test_add_offer_on_marketplace(self):
        home_page = HomePage(self.driver).open_home_page()
        account_page = home_page.header.login(USER_DELTA, PASSWORD_DELTA)
        domains_on_marketplace_list = account_page.header.open_domains_on_marketplace_list()
        domains_on_marketplace_list.get_text_second_domain()
        domains_on_marketplace_list.add_offer_to_second_domain()

        WebDriverWait(self.driver, 30).until(EC.text_to_be_present_in_element(domains_on_marketplace_list._domain_field_stage1, domains_on_marketplace_list._second_domain_text))

        domains_on_marketplace_list.get_text_price_buynow()
        domains_on_marketplace_list.submit_offer_stage1()

        WebDriverWait(self.driver, 30).until(EC.text_to_be_present_in_element(domains_on_marketplace_list._domain_field_stage1, domains_on_marketplace_list._second_domain_text))
        Assert.contains(domains_on_marketplace_list.price_buynow, domains_on_marketplace_list.get_page_source())
        Assert.contains(domains_on_marketplace_list._price_value, domains_on_marketplace_list.get_page_source())

        domains_on_marketplace_list.submit_offer_stage2()

#BŁĄD BAZY DANYCH

    def test_watch_new_domain_should_succeed(self):

        home_page = HomePage(self.driver).open_home_page()
        account_page = home_page.header.login(USER_DELTA, PASSWORD_DELTA)
        watched_domains_page = account_page.header.open_watched_domains_list()
        watched_domains_page.watch_new_domain()

        WebDriverWait(self.driver, 30).until(EC.text_to_be_present_in_element(watched_domains_page._result_text_field, u"Operacja wykonana poprawnie"))
        Assert.equal(watched_domains_page._domain_name_value, watched_domains_page.result_domain_text())

        account_page.header.open_watched_domains_list()

        Assert.contains(watched_domains_page._domain_name_value, watched_domains_page.get_page_source())
        Assert.contains(strftime("%Y-%m-%d", gmtime()), watched_domains_page.get_page_source())

        watched_domains_page.delete_first_domain()

        WebDriverWait(self.driver, 30).until(EC.text_to_be_present_in_element(watched_domains_page._result_text_field, u"Operacja wykonana poprawnie"))
        Assert.equal(watched_domains_page._domain_name_value, watched_domains_page.result_domain_text())

        watched_domains_page.back_from_results_page()

        self.not_contains(watched_domains_page._domain_name_value, watched_domains_page.get_page_source())
        self.not_contains(strftime("%Y-%m-%d", gmtime()), watched_domains_page.get_page_source())

    def test_watch_new_seller_should_succeed(self):

        seller_name = "alfa"

        home_page = HomePage(self.driver).open_home_page()
        account_page = home_page.header.login(USER_DELTA, PASSWORD_DELTA)
        watched_sellers_page = account_page.header.open_watched_sellers_list()
        watched_sellers_page.watch_new_seller(seller_name)

        Assert.contains(seller_name, watched_sellers_page.get_page_source())
        Assert.contains(strftime("%Y-%m-%d", gmtime()), watched_sellers_page.get_page_source())

        watched_sellers_page.delete_first_seller()

        WebDriverWait(self.driver, 30).until(EC.text_to_be_present_in_element(watched_sellers_page._result_text_field, u"Operacja wykonana poprawnie"))

        watched_sellers_page.back_from_results_page()

        self.not_contains(seller_name, watched_sellers_page.get_page_source())
        self.not_contains(strftime("%Y-%m-%d", gmtime()), watched_sellers_page.get_page_source())

    def test_new_escrow_option_transaction_should_succeed(self):

        login = "alfa"

        home_page = HomePage(self.driver).open_home_page()
        account_page = home_page.header.login(USER_GAMMA, PASSWORD_GAMMA)
        registered_options_list = account_page.header.open_registered_options_list()
        registered_options_list.first_option_text()
        escrow_option_transaction_page = account_page.header.open_escrow_option_transaction_list()
        escrow_option_transaction_page.add_escrow_option_transaction(login, registered_options_list._first_option_text_value)

        Assert.equal(registered_options_list._first_option_text_value, escrow_option_transaction_page.stage2_option_text())
        Assert.equal(login, escrow_option_transaction_page.stage2_login_text())
        Assert.contains(escrow_option_transaction_page._price_value, escrow_option_transaction_page.get_page_source())

        escrow_option_transaction_page.stage2_submit_and_accept_alert()

        WebDriverWait(self.driver, 30).until(EC.text_to_be_present_in_element(registered_options_list._result_text_field, u"Transakcja Escrow została zainicjowana"))
        Assert.equal(registered_options_list._first_option_text_value, registered_options_list.result_domain_text())

        account_page.header.open_escrow_option_transaction_list()

        Assert.contains(registered_options_list._first_option_text_value, escrow_option_transaction_page.get_page_source())
        Assert.contains(login, escrow_option_transaction_page.get_page_source())
        Assert.contains("Nowa", escrow_option_transaction_page.get_page_source())
        Assert.contains(escrow_option_transaction_page._price_value, escrow_option_transaction_page.get_page_source())

        escrow_option_transaction_page.delete_first_auction()

        Assert.equal(registered_options_list._first_option_text_value, escrow_option_transaction_page.stage2_option_text())
        Assert.equal(login, escrow_option_transaction_page.stage2_login_text())
        Assert.contains(escrow_option_transaction_page._price_value, escrow_option_transaction_page.get_page_source())

        escrow_option_transaction_page.stage2_submit_and_accept_alert()

        WebDriverWait(self.driver, 30).until(EC.text_to_be_present_in_element(registered_options_list._result_text_field, u"Transakcja została anulowana"))
        Assert.equal(registered_options_list._first_option_text_value, registered_options_list.result_domain_text())

        account_page.header.open_escrow_option_transaction_list()
        escrow_option_transaction_page.filter_new()

        self.not_contains(registered_options_list._first_option_text_value, escrow_option_transaction_page.get_page_source())
        self.not_contains(login, escrow_option_transaction_page.get_page_source())
        self.not_contains(strftime("%Y-%m-%d", gmtime()), escrow_option_transaction_page.get_page_source())

    def test_block_seller_should_succeed(self):

        seller_name = "alfa"

        home_page = HomePage(self.driver).open_home_page()
        account_page = home_page.header.login(USER_DELTA, PASSWORD_DELTA)
        blocked_sellers_page = account_page.header.open_blocked_sellers_list()
        blocked_sellers_page.block_seller(seller_name)

        Assert.contains(seller_name, blocked_sellers_page.get_page_source())
        Assert.contains(strftime("%Y-%m-%d", gmtime()), blocked_sellers_page.get_page_source())

        blocked_sellers_page.delete_first_seller()

        Assert.contains(seller_name, blocked_sellers_page.get_page_source())
        Assert.contains(blocked_sellers_page._note_value, blocked_sellers_page.get_page_source())

        blocked_sellers_page.delete_first_seller_submit()

        self.not_contains(seller_name, blocked_sellers_page.get_page_source())
        self.not_contains(strftime("%Y-%m-%d", gmtime()), blocked_sellers_page.get_page_source())

    def test_catch_domain_should_succeed(self):

        home_page = HomePage(self.driver).open_home_page()
        account_page = home_page.header.login(USER_DELTA, PASSWORD_DELTA)
        expiring_domains_list = account_page.header.open_expiring_domains_list()
        expiring_domains_list.first_domain_text()
        expiring_domains_list.catch_first_domain()

        WebDriverWait(self.driver, 30).until(EC.text_to_be_present_in_element(expiring_domains_list._result_text_field, u"Domena dodana do przechwycenia"))
        Assert.equal(expiring_domains_list._first_domain_text_value, expiring_domains_list.result_domain_text())

        domains_to_catch = account_page.header.open_domains_to_catch_list()

        Assert.contains(expiring_domains_list._first_domain_text_value, domains_to_catch.get_page_source())
        Assert.contains(strftime("%Y-%m-%d", gmtime()), domains_to_catch.get_page_source())

        domains_to_catch.delete_first_domain()

        WebDriverWait(self.driver, 30).until(EC.text_to_be_present_in_element(expiring_domains_list._result_text_field, u"Operacja wykonana poprawnie"))
        Assert.equal(expiring_domains_list._first_domain_text_value, expiring_domains_list.result_domain_text())

        account_page.header.open_domains_to_catch_list()

        self.not_contains(expiring_domains_list._first_domain_text_value, domains_to_catch.get_page_source())
        self.not_contains(strftime("%Y-%m-%d", gmtime()), domains_to_catch.get_page_source())

    def test_zz_generate_plot_and_send_email(self):
        self._save_plot()
        self._send_email()

    def tally(self):
        return len(self._resultForDoCleanups.errors) + len(self._resultForDoCleanups.failures)

    def setUp(self):
        self.timeout = 30
        if run_locally:
            self.driver = webdriver.Firefox()
            self.driver.set_window_size(1024,768)
            self.driver.implicitly_wait(self.timeout)
            self.errors_and_failures = self.tally()
        else:
            self.desired_capabilities['name'] = self.id()
            sauce_url = "http://%s:%s@ondemand.saucelabs.com:80/wd/hub"

            self.driver = webdriver.Remote(
                desired_capabilities=self.desired_capabilities,
                command_executor=sauce_url % (USERNAME, ACCESS_KEY)
            )

            self.driver.implicitly_wait(self.timeout)

    def tearDown(self):
        if run_locally:
                if self.tally() > self.errors_and_failures:
                    if not os.path.exists(SCREEN_DUMP_LOCATION):
                        os.makedirs(SCREEN_DUMP_LOCATION)
                    for ix, handle in enumerate(self.driver.window_handles):
                        self._windowid = ix
                        self.driver.switch_to.window(handle)
                        self.take_screenshot()
                        self.dump_html()
                self.driver.quit()

    def _get_filename(self):
        timestamp = datetime.now().isoformat().replace(':', '.')[:19]
        self._saved_filename = "{classname}.{method}-window{windowid}-{timestamp}".format(
            classname=self.__class__.__name__,
            method=self._testMethodName,
            windowid=self._windowid,
            timestamp=timestamp
        )
        return "{folder}/{classname}.{method}-window{windowid}-{timestamp}".format(
            folder=SCREEN_DUMP_LOCATION,
            classname=self.__class__.__name__,
            method=self._testMethodName,
            windowid=self._windowid,
            timestamp=timestamp
        )

    def _get_filename_for_plot(self):
        timestamp = datetime.now().isoformat().replace(':', '.')[:19]
        self._saved_filename_plot = "{classname}.plot-{timestamp}".format(
            classname=self.__class__.__name__,
            timestamp=timestamp
        )
        return "{folder}/{classname}.plot-{timestamp}".format(
            folder=SCREEN_DUMP_LOCATION,
            classname=self.__class__.__name__,
            timestamp=timestamp
            )

    def _save_plot(self):
        import matplotlib.pyplot as plt
        filename = self._get_filename_for_plot() + ".png"
        err = len(self._resultForDoCleanups.errors) + len(self._resultForDoCleanups.failures)

        # The slices will be ordered and plotted counter-clockwise.
        labels = 'Errors', 'Passes'
        sizes = [err, 50-err]
        colors = ['red', 'gold']
        explode = (0, 0.1)

        plt.pie(sizes, explode=explode, labels=labels, colors=colors,
                autopct='%1.1f%%', shadow=True, startangle=90)
        plt.axis('equal')
        print "\n WYKRES:\n", filename
        plt.savefig(filename)
        text_file = open("Aftermarket2RaportScreeny.txt", "a")
        text_file.write("<br><br>Wykres statystyczny: <a href=""http://ci.testuj.pl/job/Aftermarket2/ws/screendumps/"+self._saved_filename_plot+".png>Wykres</a>")
        text_file.close()

    def take_screenshot(self):
        filename = self._get_filename() + ".png"
        print "\n{method} Screenshot and HTML:\n".format(
            method=self._testMethodName)
        print 'screenshot:', filename
        self.driver.get_screenshot_as_file(filename)
        text_file = open("Aftermarket2RaportScreeny.txt", "a")
        text_file.write("<br><br>{method} Screenshot and HTML:<br>".format(
            method=self._testMethodName)+"<br>Screenshot: <a href=""http://ci.testuj.pl/job/Aftermarket2/ws/screendumps/"+self._saved_filename+".png>"+self._saved_filename+"</a>")
        text_file.close()

    def dump_html(self):
        filename = self._get_filename() + '.html'
        print 'page HTML:', filename
        with open(filename, 'w') as f:
            f.write(self.driver.page_source.encode('utf-8'))
        text_file = open("Aftermarket2RaportScreeny.txt", "a")
        text_file.write("<br>Html: <a href=""http://ci.testuj.pl/job/Aftermarket2/ws/screendumps/"+self._saved_filename+".html>"+self._saved_filename+"</a>")
        text_file.close()

    def _send_email(self):
        from mailer import Mailer
        from mailer import Message

        message = Message(From="jedrzej.wojcieszczyk@testuj.pl",
                          To=["kontakt@michau.name", "info@testuj.pl"])
        message.Subject = "Raport Jenkins Aftermarket2 Testy Automatyczne"
        message.Html = """<head><meta http-equiv="Content-Type" content="text/html;charset=UTF-8"></head><p>Cześć!<br>
           Oto wygenerowany automatycznie raport z testów Aftermarket2.pl<br><br>
           Tabela raportowa z logami wykonanych testów, a pod nią linki do screenshotów i kodu html testów które nie przeszły oraz wykres statystyczny: <a href="http://ci.testuj.pl/job/Aftermarket2/ws/Aftermarket2ReportLogi.html">Tabela z logami, screenshoty i wykres</a></p>"""

        sender = Mailer('smtp.gmail.com', use_tls=True, usr='jedrzej.wojcieszczyk@testuj.pl', pwd='paluch88')
        sender.send(message)

    def not_contains(self, needle, haystack, msg=''):
        try:
            assert not needle in haystack
        except AssertionError:
            raise AssertionError('%s is found in %s. %s' % (needle, haystack, msg))

open("Aftermarket2RaportScreeny.txt", 'w').close()
suite = unittest.TestLoader().loadTestsFromTestCase(SmokeTest)
outfile = open("Aftermarket2ReportLogi.html", "wb")
runner = HTMLTestRunner(stream=outfile, title='Test Report', description='Aftermarket2', verbosity=2)
runner.run(suite)

     # htmltestrunner.main()
# if __name__ == '__main__':
#      unittest.main()

     # import xmlrunner
     # unittest.main(testRunner=xmlrunner.XMLTestRunner(output='test-reports'))