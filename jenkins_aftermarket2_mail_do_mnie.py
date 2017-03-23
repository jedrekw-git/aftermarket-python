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
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
import re

SCREEN_DUMP_LOCATION = os.path.join(
    os.path.dirname(os.path.abspath(__file__)), 'screendumps'
)
run_locally = True

# @on_platforms(browsers)


class SmokeTest(unittest.TestCase):
    _internal_non_grouped_domain_text = 1

    def test_login_wrong_credentials_should_succeed(self):

        home_page = HomePage(self.driver).open_home_page()
        account_page = home_page.header.login(get_random_string(7), get_random_uuid(6))

        Assert.contains(u"Nieprawidłowy login lub hasło", account_page.get_page_source())

    def test_remind_password_wrong_login_should_succeed(self):

        login = get_random_string(7)

        home_page = HomePage(self.driver).open_home_page()
        remind_page = home_page.header.remind_password(login)

        Assert.contains(u"Podany login nie istnieje", remind_page.get_page_source())

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
        change_notification_settings_page = settings_page.open_change_email_notification_settings_page()
        settings_page.change_email_notification_settings()
        settings_page.save_change_email_notification_settings()

        WebDriverWait(self.driver, 15).until(EC.text_to_be_present_in_element(settings_page._confirmation_result_field, u"Operacja wykonana poprawnie."))

    def test_change_newsletter_settings_should_succeed(self):
        home_page = HomePage(self.driver).open_home_page()
        account_page = home_page.header.login(USER, PASSWORD)
        settings_page = account_page.header.open_settings_page()
        change_newsletter_settings_page = settings_page.open_change_newsletter_settings_page()
        settings_page.change_newsletter_settings()
        settings_page.save_change_newsletter_settings()

        Assert.contains(u"Operacja wykonana poprawnie.", settings_page.get_page_source())

    def test_add_email_address_should_succeed(self):
        home_page = HomePage(self.driver).open_home_page()
        account_page = home_page.header.login(USER, PASSWORD)
        settings_page = account_page.header.open_settings_page()
        add_email_page = settings_page.open_add_email_address_page()
        settings_page.remove_all_email_addresses()
        settings_page.add_email_address()

        Assert.contains(u"Potwierdź adres e-mail", settings_page.get_page_source())

        settings_page.back_to_email_addresses_list()

        Assert.equal(settings_page._add_email_address_value, settings_page.added_email_address_text())
        Assert.equal("Niepotwierdzony", settings_page.added_email_status_text())

        settings_page.remove_all_email_addresses()

        self.not_contains(settings_page._add_email_address_value, settings_page.get_page_source())
        self.not_contains("Niepotwierdzony", settings_page.get_page_source())

    def test_change_SMS_notification_should_succeed(self):
        home_page = HomePage(self.driver).open_home_page()
        account_page = home_page.header.login(USER, PASSWORD)
        settings_page = account_page.header.open_settings_page()
        change_sms_notification_page = settings_page.open_sms_notification_settings_page()
        # settings_page.open_first_number_notifications()
        settings_page.change_sms_notification_settings()

        WebDriverWait(self.driver, 15).until(EC.text_to_be_present_in_element(settings_page._confirmation_result_field, u"Operacja wykonana poprawnie."))

    def test_add_other_users_to_account_should_succeed(self):
        home_page = HomePage(self.driver).open_home_page()
        account_page = home_page.header.login(USER, PASSWORD)
        settings_page = account_page.header.open_settings_page()
        add_other_users_page = settings_page.open_add_other_users_page()
        settings_page.remove_all_users()
        settings_page.add_other_user()
        settings_page.add_other_user_change_priviledges()

        WebDriverWait(self.driver, 15).until(EC.text_to_be_present_in_element(settings_page._confirmation_result_field, u"Operacja wykonana poprawnie."))
        WebDriverWait(self.driver, 15).until(EC.text_to_be_present_in_element(settings_page._add_other_user_header, u"Lista loginów"))

        Assert.equal(settings_page._add_other_user_login_value, settings_page.added_user_login_text())
        Assert.equal(settings_page._add_other_user_description_value, settings_page.added_user_description_text())

        settings_page.remove_all_users()

        self.not_contains(settings_page._add_other_user_login_value, settings_page.get_page_source())
        self.not_contains(settings_page._add_other_user_description_value, settings_page.get_page_source())

    def test_change_company_address_should_succeed(self):
        home_page = HomePage(self.driver).open_home_page()
        account_page = home_page.header.login(USER, PASSWORD)
        settings_page = account_page.header.open_settings_page()
        change_company_address_page = settings_page.open_change_company_data_page()
        settings_page.edit_company_address()
        sleep(30)
        Assert.contains("Operacja wykonana poprawnie", settings_page.edit_company_data_operation_successful_text())
        Assert.contains(settings_page.edit_company_data_zip_text(), settings_page._change_company_data_zip_value)
        Assert.equal(settings_page._change_company_data_street_value, settings_page.edit_company_data_street_text())
        Assert.equal(settings_page._change_company_data_city_value, settings_page.edit_company_data_city_text())

    def test_change_company_data_should_succeed(self):
        home_page = HomePage(self.driver).open_home_page()
        account_page = home_page.header.login(USER_BETA, PASSWORD_BETA)
        settings_page = account_page.header.open_settings_page()
        change_company_data_page = settings_page.open_change_company_data_page()
        settings_page.edit_company_data()

        Assert.contains(settings_page.edit_company_data_zip_text(), settings_page._change_company_data_zip_value)
        Assert.equal(settings_page._change_company_data_street_value, settings_page.edit_company_data_street_text())
        Assert.equal(settings_page._change_company_data_city_value, settings_page.edit_company_data_city_text())
        Assert.equal(settings_page._change_company_data_company_name_value, settings_page.edit_company_data_company_name_text())
        Assert.equal(settings_page._change_company_data_nip_value, settings_page.edit_company_data_nip_text())

    def test_add_new_bank_account_should_succeed(self):

        number = "26105014451000002276470461"

        home_page = HomePage(self.driver).open_home_page()
        account_page = home_page.header.login(USER, PASSWORD)
        settings_page = account_page.header.open_settings_page()
        bank_accounts_page = settings_page.open_add_bank_account_page()
        settings_page.remove_all_bank_accounts()
        settings_page.add_bank_account(number)

        Assert.contains(u"Operacja wykonana poprawnie.", settings_page.get_page_source())
        WebDriverWait(self.driver, 30).until(EC.text_to_be_present_in_element(settings_page._added_bank_account_number, number))
        Assert.contains("Lista kont bankowych", settings_page.get_page_source())
        Assert.contains(u"Na tej liście znajdują się konta bankowe, na które możesz zlecać wypłaty.", settings_page.get_page_source())
        Assert.contains("Oto lista twoich kont bankowych.", settings_page.get_page_source())
        Assert.equal(settings_page._add_bank_account_account_name_value, settings_page.added_bank_account_name_text())

        settings_page.remove_all_bank_accounts()

        Assert.contains("Lista kont bankowych", settings_page.get_page_source())
        Assert.contains(u"Na tej liście znajdują się konta bankowe, na które możesz zlecać wypłaty.", settings_page.get_page_source())
        Assert.contains("Oto lista twoich kont bankowych.", settings_page.get_page_source())
        Assert.contains(u"Brak zdefiniowanych kont bankowych", settings_page.get_page_source())
        self.not_contains(number, settings_page.get_page_source())
        self.not_contains(settings_page._add_bank_account_account_name_value, settings_page.get_page_source())

    def test_change_DNS_servers_should_succeed(self):
        home_page = HomePage(self.driver).open_home_page()
        account_page = home_page.header.login(USER, PASSWORD)
        settings_page = account_page.header.open_settings_page()
        dns_servers_page = settings_page.open_change_DNS_servers_page()
        settings_page.change_DNS_servers()

        Assert.contains("ns1.aftermarket.pl", settings_page.get_page_source())
        Assert.contains("ns2.aftermarket.pl", settings_page.get_page_source())
        Assert.contains(settings_page._change_DNS_servers_DNS3_value, settings_page.get_page_source())
        Assert.contains(settings_page._change_DNS_servers_DNS4_value, settings_page.get_page_source())
        Assert.equal("Operacja wykonana poprawnie", settings_page.change_DNS_servers_operation_successful_text())

    def test_new_DNS_profile_should_succeed(self):
        home_page = HomePage(self.driver).open_home_page()
        account_page = home_page.header.login(USER, PASSWORD)
        settings_page = account_page.header.open_settings_page()
        dns_profile_page = settings_page.open_new_DNS_template_page()
        settings_page.delete_all_profiles()
        settings_page.new_DNS_template()

        settings_page.new_DNS_entry()
        Assert.equal("Operacja wykonana poprawnie", settings_page.new_DNS_profile_successful_operation_text())
        Assert.equal(settings_page._new_DNS_profile_name_value, settings_page.new_DNS_profile_successtul_opertation_profile_text())
        Assert.equal(settings_page._new_DNS_profile_host_value, settings_page.new_DNS_profile_successtul_opertation_host_text())
        Assert.equal(settings_page._new_DNS_profile_address_value, settings_page.new_DNS_profile_successtul_opertation_address_text())

        settings_page = account_page.header.open_settings_page()
        dns_profile_page = settings_page.open_new_DNS_template_page()

        Assert.contains(u"Lista szablonów DNS", settings_page.get_page_source())
        Assert.equal(settings_page._new_DNS_profile_name_value, settings_page.new_DNS_profile_name_text())

        settings_page.delete_all_profiles()

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

    def test_sending_notification_settings_t55should_succeed(self):
        home_page = HomePage(self.driver).open_home_page()
        account_page = home_page.header.login(USER, PASSWORD)
        settings_page = account_page.header.open_settings_page()
        sending_notification_settings_page = settings_page.open_sending_notification_settings_page()
        settings_page.change_sending_notification_settings()

        Assert.contains("Operacja wykonana poprawnie", settings_page.get_page_source())

    def test_task_list_filtering_should_succeed(self):
        home_page = HomePage(self.driver).open_home_page()
        account_page = home_page.header.login(USER_DELTA, PASSWORD_DELTA)
        task_list = account_page.header.open_task_list()
        task_list.get_text_selected_option()
        task_list.select_operation_type()
        try:
            WebDriverWait(self.driver, 10).until(EC.text_to_be_present_in_element(task_list._first_result, task_list.option_text))
            Assert.contains(u"Rodzaj operacji: <b>%s" % task_list.option_text, task_list.get_page_source())
        except WebDriverException:
            Assert.contains(u"Brak zleconych operacji.", task_list.get_page_source())

    def test_register_domain_should_succeed(self):
        home_page = HomePage(self.driver).open_home_page()
        account_page = home_page.header.login(USER_BETA, PASSWORD_BETA)
        to_pay_list = account_page.header.open_to_pay_list()
        to_pay_list.remove_all_payments()
        register_domain_page = account_page.header.open_register_domain_page()
        register_domain_page.enter_domain_to_register(register_domain_page._domain_name_value_co_pl)

        WebDriverWait(self.driver, 30).until(EC.text_to_be_present_in_element(register_domain_page._domain_status_field, u"Dostępna do rejestracji"))

        register_domain_page.register_domain()

        WebDriverWait(self.driver, 20).until(EC.text_to_be_present_in_element(register_domain_page._registration_effect_domain_field, register_domain_page._domain_name_value_co_pl))
        WebDriverWait(self.driver, 20).until(EC.text_to_be_present_in_element(register_domain_page._registration_effect_text_field, u"Operacja zawieszona, oczekuje na aktywowanie"))
        to_pay_list = account_page.header.open_to_pay_list()

        WebDriverWait(self.driver, 30).until(EC.text_to_be_present_in_element(to_pay_list._first_payment_title, register_domain_page._domain_name_value_co_pl))
        WebDriverWait(self.driver, 30).until(EC.text_to_be_present_in_element(to_pay_list._first_payment_type, u"Rejestracja domeny"))

        to_pay_list.submit_first_payment()
        # to_pay_list.remove_all_payments()
        #
        # self.not_contains(register_domain_page._domain_name_value_co_pl, to_pay_list.get_page_source())
        # self.not_contains(u"Rejestracja domeny", to_pay_list.get_page_source())

    def test_renew_domain_automatically_should_succeed(self):
        home_page = HomePage(self.driver).open_home_page()
        account_page = home_page.header.login(USER_DELTA, PASSWORD_DELTA)
        registered_domains_page = account_page.header.open_registered_domains_list()
        registered_domains_page.first_domain_text()
        registered_domains_page.select_first_domain()
        registered_domains_page.renew_domain_automatically()

        WebDriverWait(self.driver, 10).until(EC.text_to_be_present_in_element(registered_domains_page._result_text_field, u"Domena będzie automatycznie odnawiana od"))
        Assert.equal(registered_domains_page._first_domain_text_value, registered_domains_page.result_domain_text())

    def test_renew_domain_manually_should_succeed(self):
        home_page = HomePage(self.driver).open_home_page()
        account_page = home_page.header.login(USER_BETA, PASSWORD_BETA)
        to_pay_list = account_page.header.open_to_pay_list()
        to_pay_list.remove_all_payments()
        registered_domains_page = account_page.header.open_registered_domains_list()
        registered_domains_page.first_domain_text()
        registered_domains_page.select_first_domain()
        registered_domains_page.renew_domain_manually()

        WebDriverWait(self.driver, 30).until(EC.text_to_be_present_in_element(registered_domains_page._second_stage_text_field, u"Domena zostanie odnowiona"))
        Assert.equal(registered_domains_page._first_domain_text_value, registered_domains_page.second_stage_domain_text())

        registered_domains_page.second_stage_checkboxes_and_submit()

        sleep(3)
        if u"Operacja zawieszona, oczekuje na aktywowanie" in registered_domains_page.result_text():
            Assert.equal(registered_domains_page._first_domain_text_value, registered_domains_page.result_domain_text())
        else:
            WebDriverWait(self.driver, 30).until(EC.text_to_be_present_in_element(registered_domains_page._result_text_field, u"Domena już była odnowiona w ostatnim okresie: "))
            Assert.equal(registered_domains_page._first_domain_text_value, registered_domains_page.result_domain_text())

        to_pay_list = account_page.header.open_to_pay_list()
        to_pay_list.change_tab_renew()

        WebDriverWait(self.driver, 30).until(EC.text_to_be_present_in_element(to_pay_list._first_payment_title, registered_domains_page._first_domain_text_value))
        WebDriverWait(self.driver, 30).until(EC.text_to_be_present_in_element(to_pay_list._first_payment_type, u"Odnowienie domeny"))

        to_pay_list.remove_all_payments()
        to_pay_list.refresh()

        self.not_contains(registered_domains_page._first_domain_text_value, to_pay_list.get_page_source())
        self.not_contains(u"Odnowienie domeny", to_pay_list.get_page_source())

    def test_change_profile_data_should_succeed(self):
        home_page = HomePage(self.driver).open_home_page()
        account_page = home_page.header.login(USER_DELTA, PASSWORD_DELTA)
        registered_domains_page = account_page.header.open_registered_domains_list()
        registered_domains_page.second_domain_text()
        registered_domains_page.select_second_domain()
        registered_domains_page.change_profile_data()

        WebDriverWait(self.driver, 30).until(EC.text_to_be_present_in_element(registered_domains_page._second_stage_text_field, u"Profil danych zostanie zmieniony"))
        Assert.equal(registered_domains_page._second_domain_text_value, registered_domains_page.second_stage_domain_text())

        registered_domains_page.change_profile_data_stage_2()

        WebDriverWait(self.driver, 30).until_not(EC.text_to_be_present_in_element(registered_domains_page._result_text_field, u"Operacja w toku"))
        if u"Ustawiono profil danych:" in registered_domains_page.result_text():
            Assert.equal(registered_domains_page._second_domain_text_value, registered_domains_page.result_domain_text())
        else:
            WebDriverWait(self.driver, 30).until(EC.text_to_be_present_in_element(registered_domains_page._result_text_field, u"Domena jest zablokowana"))
            Assert.equal(registered_domains_page._second_domain_text_value, registered_domains_page.result_domain_text())

    def test_privacy_settings_should_succeed(self):
        home_page = HomePage(self.driver).open_home_page()
        account_page = home_page.header.login(USER_DELTA, PASSWORD_DELTA)
        registered_domains_page = account_page.header.open_registered_domains_list()
        registered_domains_page.first_domain_text()
        registered_domains_page.select_first_domain()
        registered_domains_page.privacy_settings_first_stage()

        WebDriverWait(self.driver, 30).until(EC.text_to_be_present_in_element(registered_domains_page._second_stage_text_field, u"Dane abonenta będą widoczne"))
        Assert.equal(registered_domains_page._first_domain_text_value, registered_domains_page.second_stage_domain_text())

        registered_domains_page.second_stage_checkboxes_and_submit2()

        WebDriverWait(self.driver, 30).until(EC.text_to_be_present_in_element(registered_domains_page._result_text_field, u"Dane abonenta zostały ujawnione"))
        Assert.equal(registered_domains_page._first_domain_text_value, registered_domains_page.result_domain_text())

    def test_get_authinfo_should_succeed(self):
        home_page = HomePage(self.driver).open_home_page()
        account_page = home_page.header.login(USER_DELTA, PASSWORD_DELTA)
        registered_domains_page = account_page.header.open_registered_domains_list()
        registered_domains_page.first_domain_text()
        registered_domains_page.select_first_domain()
        registered_domains_page.get_authinfo()

        try:
            WebDriverWait(self.driver, 15).until(EC.text_to_be_present_in_element(registered_domains_page._result_text_field, u"Kod AuthInfo:"))
            Assert.equal(registered_domains_page._first_domain_text_value, registered_domains_page.result_domain_text())
        except WebDriverException:
            WebDriverWait(self.driver, 15).until(EC.text_to_be_present_in_element(registered_domains_page._result_text_field, u"Domeny nie można transferować"))
            Assert.equal(registered_domains_page._first_domain_text_value, registered_domains_page.result_domain_text())

    def test_move_domain_from_account_should_succeed(self):

        login = "alfa"

        home_page = HomePage(self.driver).open_home_page()
        account_page = home_page.header.login(USER_DELTA, PASSWORD_DELTA)
        registered_domains_page = account_page.header.open_registered_domains_list()
        registered_domains_page.first_domain_text()
        registered_domains_page.select_first_domain()
        registered_domains_page.move_domain_from_account(login)

        WebDriverWait(self.driver, 40).until(EC.text_to_be_present_in_element(registered_domains_page._result_text_field, u"Transfer domeny został zainicjowany"))
        Assert.equal(registered_domains_page._first_domain_text_value, registered_domains_page.result_domain_text())

        transfer_domain_page = account_page.header.open_transfer_domain_from_account_list()
        transfer_domain_page.cancel_all_domain_transfers_from_account()

        self.not_contains(registered_domains_page._first_domain_text_value, transfer_domain_page.get_page_source())

    def test_change_DNS_servers_for_selected_domain_should_succeed(self):
        home_page = HomePage(self.driver).open_home_page()
        account_page = home_page.header.login(USER_BETA, PASSWORD_BETA)
        registered_domains_page = account_page.header.open_registered_domains_list()
        registered_domains_page.third_domain_text()
        registered_domains_page.select_third_domain()
        registered_domains_page.change_dns_servers_for_selected_domain()

        WebDriverWait(self.driver, 30).until(EC.text_to_be_present_in_element(registered_domains_page._result_text_field, u"Ustawiono serwery DNS:"))
        Assert.equal(registered_domains_page._third_domain_text_value, registered_domains_page.result_domain_text())

    def test_change_redirection_direct_should_succeed(self):
        home_page = HomePage(self.driver).open_home_page()
        account_page = home_page.header.login(USER_DELTA, PASSWORD_DELTA)
        registered_domains_page = account_page.header.open_registered_domains_list()
        registered_domains_page.first_domain_text()
        registered_domains_page.select_first_domain()
        registered_domains_page.change_redirection_direct()

        WebDriverWait(self.driver, 30).until(EC.text_to_be_present_in_element(registered_domains_page._result_text_field, u"Przekierowano na adres: %s"%registered_domains_page._change_redirection_url_value))
        Assert.equal(registered_domains_page._first_domain_text_value, registered_domains_page.result_domain_text())

    def test_change_redirection_hidden_should_succeed(self):
        home_page = HomePage(self.driver).open_home_page()
        account_page = home_page.header.login(USER_DELTA, PASSWORD_DELTA)
        registered_domains_page = account_page.header.open_registered_domains_list()
        registered_domains_page.first_domain_text()
        registered_domains_page.select_first_domain()
        registered_domains_page.change_redirection_hidden()

        WebDriverWait(self.driver, 30).until(EC.text_to_be_present_in_element(registered_domains_page._result_text_field, u"Przekierowano na adres: %s"%registered_domains_page._change_redirection_url_value))
        Assert.equal(registered_domains_page._first_domain_text_value, registered_domains_page.result_domain_text())

    def test_change_redirection_ip_should_succeed(self):
        home_page = HomePage(self.driver).open_home_page()
        account_page = home_page.header.login(USER_DELTA, PASSWORD_DELTA)
        registered_domains_page = account_page.header.open_registered_domains_list()
        registered_domains_page.first_domain_text()
        registered_domains_page.select_first_domain()
        registered_domains_page.change_redirection_ip()

        WebDriverWait(self.driver, 30).until(EC.text_to_be_present_in_element(registered_domains_page._result_text_field, u"Przekierowano na adres: %s"%registered_domains_page._change_redirection_ip_value))
        Assert.equal(registered_domains_page._first_domain_text_value, registered_domains_page.result_domain_text())

    def test_change_dns_profile_should_succeed(self):

        home_page = HomePage(self.driver).open_home_page()
        account_page = home_page.header.login(USER_DELTA, PASSWORD_DELTA)
        registered_domains_page = account_page.header.open_registered_domains_list()
        registered_domains_page.first_domain_text()
        registered_domains_page.select_first_domain()
        registered_domains_page.change_dns_profile_stage1()
        registered_domains_page.change_DNS_profile_stage2()
        WebDriverWait(self.driver, 15).until(EC.text_to_be_present_in_element(registered_domains_page._result_text_field, u"Zastosowano szablon wpisów DNS:"))
        Assert.equal(registered_domains_page._first_domain_text_value, registered_domains_page.result_domain_text())

    def test_new_dns_entry_for_selected_domain_should_succeed(self):

        home_page = HomePage(self.driver).open_home_page()
        account_page = home_page.header.login(USER_DELTA, PASSWORD_DELTA)
        registered_domains_page = account_page.header.open_registered_domains_list()
        registered_domains_page.first_domain_text()
        registered_domains_page.select_first_domain()
        sleep(1)
        registered_domains_page.new_dns_entry_for_selected_domain()
        registered_domains_page.delete_all_dns_entries_for_selected_domain()
        registered_domains_page.new_dns_entry_for_selected_domain_details()

        Assert.contains("Operacja wykonana poprawnie", registered_domains_page.get_page_source())

        registered_domains_page.back_from_results_page()

        Assert.contains(registered_domains_page._add_dns_entry_host_name_value, registered_domains_page.get_page_source())
        Assert.contains(registered_domains_page._add_dns_entry_priority_value, registered_domains_page.get_page_source())
        Assert.contains(registered_domains_page._add_dns_entry_address_value, registered_domains_page.get_page_source())

        registered_domains_page.delete_all_dns_entries_for_selected_domain()

        self.not_contains(registered_domains_page._add_dns_entry_host_name_value, registered_domains_page.get_page_source())
        self.not_contains(registered_domains_page._add_dns_entry_address_value, registered_domains_page.get_page_source())

# PRZYCISK POWROTU PO DODANIU WPISU NIE PRZEKIEROWUJE NIGDZIE, zgłoszone


    def test_new_dns_server_in_domain_should_succeed(self):

        home_page = HomePage(self.driver).open_home_page()
        account_page = home_page.header.login(USER_DELTA, PASSWORD_DELTA)
        registered_domains_page = account_page.header.open_registered_domains_list()
        registered_domains_page.first_domain_text()
        registered_domains_page.select_first_domain()
        registered_domains_page.dns_servers_in_domain()

        registered_domains_page.delete_all_dns_servers_in_domain()
        registered_domains_page.new_dns_server_in_domain_details()
        Assert.contains(u"Operacja wykonana poprawnie.", registered_domains_page.get_page_source())
        registered_domains_page.back_from_results_page()

        Assert.contains(registered_domains_page._new_dns_server_in_domain_name_value+"."+registered_domains_page._first_domain_text_value, registered_domains_page.get_page_source())
        Assert.contains(registered_domains_page._new_dns_server_in_domain_ip_value, registered_domains_page.get_page_source())

        registered_domains_page.delete_all_dns_servers_in_domain()

        self.not_contains(registered_domains_page._new_dns_server_in_domain_name_value+"."+registered_domains_page._first_domain_text_value, registered_domains_page.get_page_source())
        self.not_contains(registered_domains_page._new_dns_server_in_domain_ip_value, registered_domains_page.get_page_source())

    def test_change_parking_service_should_succeed(self):

        home_page = HomePage(self.driver).open_home_page()
        account_page = home_page.header.login(USER_DELTA, PASSWORD_DELTA)
        registered_domains_page = account_page.header.open_registered_domains_list()
        registered_domains_page.first_domain_text()
        registered_domains_page.select_first_domain()
        registered_domains_page.change_parking_service()

        WebDriverWait(self.driver, 30).until(EC.text_to_be_present_in_element(registered_domains_page._result_text_field, u"Zmieniono serwis parkingu domeny"))
        Assert.equal(registered_domains_page._first_domain_text_value, registered_domains_page.result_domain_text())

    def test_change_keyword_should_succeed(self):

        home_page = HomePage(self.driver).open_home_page()
        account_page = home_page.header.login(USER_DELTA, PASSWORD_DELTA)
        registered_domains_page = account_page.header.open_registered_domains_list()
        registered_domains_page.first_domain_text()
        registered_domains_page.select_first_domain()
        registered_domains_page.change_keyword()

        WebDriverWait(self.driver, 30).until_not(EC.text_to_be_present_in_element(registered_domains_page._result_text_field, u"Operacja w toku"))

        if "Domena odnowiona poprawnie" in registered_domains_page.result_text():
            Assert.equal(registered_domains_page._first_domain_text_value, registered_domains_page._result_domain_text())
        else:
            WebDriverWait(self.driver, 30).until(EC.text_to_be_present_in_element(registered_domains_page._result_text_field, u"Domena nie jest zaparkowana"))
            Assert.equal(registered_domains_page._first_domain_text_value, registered_domains_page.result_domain_text())

    def test_sell_on_auction_should_succeed(self):

        home_page = HomePage(self.driver).open_home_page()
        account_page = home_page.header.login(USER_DELTA, PASSWORD_DELTA)
        selling_auction_page = account_page.header.open_selling_auction_list()
        selling_auction_page.delete_all_domain_selling_auctions()
        registered_domains_page = account_page.header.open_registered_domains_list()
        registered_domains_page.third_domain_text()
        sleep(1)
        registered_domains_page.select_third_domain()
        registered_domains_page.sell_on_auction()

        Assert.equal(registered_domains_page._third_domain_text_value, registered_domains_page.sell_on_auction_stage2_domain_text())
        Assert.equal(registered_domains_page._sell_on_auction_description_value, registered_domains_page.sell_on_auction_stage2_description_text())

        registered_domains_page.sell_on_auction_submit()
        sleep(2)
        # Assert.contains("Operacja wykonana poprawnie", registered_domains_page.get_page_source())
        WebDriverWait(self.driver, 30).until(EC.text_to_be_present_in_element(registered_domains_page._result_text_field, u"Aukcja została wystawiona z ceną początkową %s"%registered_domains_page._sell_on_auction_price_start_value))
        Assert.equal(registered_domains_page._third_domain_text_value, registered_domains_page.result_domain_text())

        selling_auction_page = account_page.header.open_selling_auction_list()
        Times=0
        while Times < 10:
            try:
                Times+=1
                Assert.contains(registered_domains_page._third_domain_text_value, selling_auction_page.get_page_source())
                break
            except AssertionError:
                self.driver.refresh()
        Assert.contains(str(registered_domains_page._sell_on_auction_price_start_value), selling_auction_page.get_page_source())
        selling_auction_page.delete_all_domain_selling_auctions()

        self.not_contains(registered_domains_page._third_domain_text_value, selling_auction_page.get_page_source())

    def test_sell_on_auction_edit_details_should_succeed(self):

        home_page = HomePage(self.driver).open_home_page()
        account_page = home_page.header.login(USER_DELTA, PASSWORD_DELTA)
        selling_auction_page = account_page.header.open_selling_auction_list()
        selling_auction_page.delete_all_domain_selling_auctions()
        registered_domains_page = account_page.header.open_registered_domains_list()
        registered_domains_page.third_domain_text()
        sleep(1)
        registered_domains_page.select_third_domain()
        registered_domains_page.sell_on_auction()

        Assert.equal(registered_domains_page._third_domain_text_value, registered_domains_page.sell_on_auction_stage2_domain_text())
        Assert.equal(registered_domains_page._sell_on_auction_description_value, registered_domains_page.sell_on_auction_stage2_description_text())

        registered_domains_page.sell_on_auction_submit()
        sleep(2)
        # Assert.contains("Operacja wykonana poprawnie", registered_domains_page.get_page_source())
        WebDriverWait(self.driver, 30).until(EC.text_to_be_present_in_element(registered_domains_page._result_text_field, u"Aukcja została wystawiona z ceną początkową %s"%registered_domains_page._sell_on_auction_price_start_value))
        Assert.equal(registered_domains_page._third_domain_text_value, registered_domains_page.result_domain_text())

        selling_auction_page = account_page.header.open_selling_auction_list()
        Times=0
        while Times < 10:
            try:
                Times+=1
                Assert.contains(registered_domains_page._third_domain_text_value, selling_auction_page.get_page_source())
                break
            except AssertionError:
                self.driver.refresh()
        Assert.contains(str(registered_domains_page._sell_on_auction_price_start_value), selling_auction_page.get_page_source())
        selling_auction_page.first_auction_enter_edit_prices()

        Assert.contains(registered_domains_page._third_domain_text_value, selling_auction_page.get_page_source())
        Assert.contains(str(registered_domains_page._sell_on_auction_price_start_value), selling_auction_page.get_page_source())

        selling_auction_page.edit_auction_prices()
        sleep(2)
        Assert.contains(u"Operacja wykonana poprawnie.", selling_auction_page.get_page_source())
        WebDriverWait(self.driver, 30).until(EC.text_to_be_present_in_element(selling_auction_page._selling_auctions_header, u"Lista aukcji (sprzedawca)"))

        Assert.contains(registered_domains_page._third_domain_text_value, selling_auction_page.get_page_source())
        Assert.contains(str(selling_auction_page._edit_auction_details_price_start_value), selling_auction_page.get_page_source())

        selling_auction_page.first_auction_enter_edit_description()

        Assert.contains(registered_domains_page._third_domain_text_value, selling_auction_page.get_page_source())
        Assert.contains(str(selling_auction_page._edit_auction_details_price_start_value), selling_auction_page.get_page_source())

        selling_auction_page.edit_auction_description()

        Assert.contains(u"Operacja wykonana poprawnie.", selling_auction_page.get_page_source())
        WebDriverWait(self.driver, 30).until(EC.text_to_be_present_in_element(selling_auction_page._selling_auctions_header, u"Lista aukcji (sprzedawca)"))
        selling_auction_page.delete_all_domain_selling_auctions()

        self.not_contains(registered_domains_page._third_domain_text_value, selling_auction_page.get_page_source())

    def test_sell_on_escrow_auction_should_succeed(self):

        login_value = "alfa"
        price = get_random_integer(2)

        home_page = HomePage(self.driver).open_home_page()
        account_page = home_page.header.login(USER_DELTA, PASSWORD_DELTA)
        escrow_auction_page = account_page.header.open_escrow_transactions_seller_list()
        escrow_auction_page.delete_all_escrow_auctions()
        registered_domains_page = account_page.header.open_registered_domains_list()
        registered_domains_page.first_domain_text()
        registered_domains_page.select_first_domain()
        registered_domains_page.sell_on_escrow_auction(login_value, price)

        Assert.equal(registered_domains_page._first_domain_text_value, registered_domains_page.sell_on_auction_stage2_domain_text())
        Assert.contains(price, registered_domains_page.get_page_source())
        Assert.equal(login_value, registered_domains_page.sell_on_escrow_auction_stage2_buyer_login_text())

        registered_domains_page.sell_on_escrow_auction_stage2()

        WebDriverWait(self.driver, 30).until(EC.text_to_be_present_in_element(registered_domains_page._add_escrow_transaction_result_text_field, u"Transakcja Escrow została rozpoczęta"))

        escrow_auction_page = account_page.header.open_escrow_transactions_seller_list()

        Assert.equal(registered_domains_page._first_domain_text_value, escrow_auction_page.first_auction_domain_name_text())
        Assert.contains(price, escrow_auction_page.get_page_source())
        Assert.equal(login_value, escrow_auction_page.first_auction_buyer_login_text())

        escrow_auction_page.delete_all_escrow_auctions()

    def test_search_selling_escrow_auctions_should_succeed(self):

        home_page = HomePage(self.driver).open_home_page()
        account_page = home_page.header.login(USER_BETA, PASSWORD_BETA)
        escrow_auction_page = account_page.header.open_escrow_transactions_seller_list()
        escrow_auction_page.get_text_first_domain_login_and_price()
        escrow_auction_page.search_for_auction(escrow_auction_page.first_domain_text)

        WebDriverWait(self.driver, 15).until(EC.text_to_be_present_in_element(escrow_auction_page._first_auction_domain_name_field, escrow_auction_page.first_domain_text))
        Assert.equal(escrow_auction_page.first_domain_login_text, escrow_auction_page.first_auction_buyer_login_text())
        Assert.equal(escrow_auction_page.first_domain_price_text, escrow_auction_page.first_auction_price_text())


# NIE WYŚWIETLA WSZYSTKICH WYNIKÓW, ZGŁOSZONE



    def test_sell_on_escrow_auction_the_same_login_should_succeed(self):

        login_value = USER_DELTA
        price = get_random_integer(2)

        home_page = HomePage(self.driver).open_home_page()
        account_page = home_page.header.login(USER_DELTA, PASSWORD_DELTA)
        registered_domains_page = account_page.header.open_registered_domains_list()
        registered_domains_page.third_domain_text()
        registered_domains_page.select_third_domain()
        registered_domains_page.sell_on_escrow_auction(login_value, price)

        Assert.contains(registered_domains_page._third_domain_text_value, registered_domains_page.get_page_source())
        Assert.contains(price, registered_domains_page.get_page_source())
        Assert.contains(login_value, registered_domains_page.get_page_source())
        Assert.contains(u"Nie możesz przeprowadzić transakcji sam ze sobą", registered_domains_page.get_page_source())

    def test_search_buyer_escrow_auctions_should_succeed(self):

        home_page = HomePage(self.driver).open_home_page()
        account_page = home_page.header.login(USER_DELTA, PASSWORD_DELTA)
        escrow_auction_page = account_page.header.open_escrow_transactions_buyer_list()
        escrow_auction_page.get_text_second_domain_status_and_price()
        escrow_auction_page.search_for_auction(escrow_auction_page.second_domain_text)

        WebDriverWait(self.driver, 30).until(EC.text_to_be_present_in_element(escrow_auction_page._first_auction_domain_name_field, escrow_auction_page.second_domain_text))
        Assert.equal(escrow_auction_page.second_domain_status_text, escrow_auction_page.first_auction_buyer_status_text())
        Assert.equal(escrow_auction_page.second_domain_price_text, escrow_auction_page.first_auction_price_text())

    def test_add_on_marketplace_should_succeed(self):

        home_page = HomePage(self.driver).open_home_page()
        account_page = home_page.header.login(USER_DELTA, PASSWORD_DELTA)
        registered_domains_page = account_page.header.open_registered_domains_list()
        registered_domains_page.fourth_domain_text()
        registered_domains_page.select_fourth_domain()
        registered_domains_page.add_on_marketplace()

        WebDriverWait(self.driver, 30).until(EC.text_to_be_present_in_element(registered_domains_page._result_text_field, u"Cena Kup Teraz: "+registered_domains_page._add_on_marketplace_buynow_value))
        WebDriverWait(self.driver, 30).until(EC.text_to_be_present_in_element(registered_domains_page._result_text_field, u"Cena minimalna: "+registered_domains_page._add_on_marketplace_minimum_price_value))
        WebDriverWait(self.driver, 30).until(EC.text_to_be_present_in_element(registered_domains_page._result_text_field, u"Dzierżawa: "+registered_domains_page._add_on_marketplace_lease_value))
        Assert.equal(registered_domains_page._fourth_domain_text_value, registered_domains_page.result_domain_text())

    # BŁĄD BAZY DANYCH, zgłoszone

    def test_delete_domain_should_succeed(self):
        home_page = HomePage(self.driver).open_home_page()
        account_page = home_page.header.login(USER_BETA, PASSWORD_BETA)
        register_domain_page = account_page.header.open_register_domain_page()
        register_domain_page.enter_domain_to_register(register_domain_page._domain_name_value_co_pl)
        WebDriverWait(self.driver, 15).until(EC.text_to_be_present_in_element(register_domain_page._domain_status_field, u"Dostępna do rejestracji"))
        register_domain_page.register_domain_immediately()
        WebDriverWait(self.driver, 15).until(EC.text_to_be_present_in_element(register_domain_page._result_text_field, u"Domena zarejestrowana poprawnie"))
        registered_domains_page = account_page.header.open_registered_domains_list()
        registered_domains_page.search_for_auction(register_domain_page._domain_name_value_co_pl)
        registered_domains_page.wait_until_domain_is_visible()
        registered_domains_page.select_first_searched_auction()
        registered_domains_page.delete_auction()
        WebDriverWait(self.driver, 15).until(EC.text_to_be_present_in_element(registered_domains_page._result_text_field, u"Domena została usunięta"))
        Assert.equal(register_domain_page._domain_name_value_co_pl, registered_domains_page.result_domain_text())

        registered_domains_page = account_page.header.open_registered_domains_list()
        registered_domains_page.search_for_auction(register_domain_page._domain_name_value_co_pl)

        Assert.contains(u"Brak elementów spełniających warunki wyszukiwania", registered_domains_page.get_page_source())

    def test_transfer_domain_to_the_same_account_should_succeed(self):
        home_page = HomePage(self.driver).open_home_page()
        account_page = home_page.header.login(USER_DELTA, PASSWORD_DELTA)
        register_domain_page = account_page.header.open_register_domain_page()
        register_domain_page.enter_domain_to_register(register_domain_page._domain_name_value_co_pl)
        WebDriverWait(self.driver, 15).until(EC.text_to_be_present_in_element(register_domain_page._domain_status_field, u"Dostępna do rejestracji"))
        register_domain_page.register_domain_immediately()
        WebDriverWait(self.driver, 15).until(EC.text_to_be_present_in_element(register_domain_page._result_text_field, u"Domena zarejestrowana poprawnie"))
        registered_domains_page = account_page.header.open_registered_domains_list()
        registered_domains_page.search_for_auction(register_domain_page._domain_name_value_co_pl)
        registered_domains_page.wait_until_domain_is_visible()
        registered_domains_page.select_first_searched_auction()
        registered_domains_page.get_authinfo()

        WebDriverWait(self.driver, 30).until(EC.text_to_be_present_in_element(registered_domains_page._result_text_field, u"Kod AuthInfo:"))

        registered_domains_page.store_authinfo()
        transfer_domain_page = account_page.header.open_transfer_domain_to_account_list()
        transfer_domain_page.transfer_domain(register_domain_page._domain_name_value_co_pl, registered_domains_page._authinfo)

        WebDriverWait(self.driver, 30).until(EC.text_to_be_present_in_element(transfer_domain_page._stage2_result_field, u"Domena już znajduje się na twoim koncie"))
        Assert.equal(register_domain_page._domain_name_value_co_pl, transfer_domain_page.stage2_domain_text())

        registered_domains_page = account_page.header.open_registered_domains_list()
        registered_domains_page.search_for_auction(register_domain_page._domain_name_value_co_pl)
        registered_domains_page.select_first_searched_auction()
        registered_domains_page.delete_auction()
        WebDriverWait(self.driver, 15).until(EC.text_to_be_present_in_element(registered_domains_page._result_text_field, u"Domena została usunięta"))
        Assert.equal(register_domain_page._domain_name_value_co_pl, registered_domains_page.result_domain_text())

    def test_transfer_domain_to_the_other_account_should_succeed(self):
        home_page = HomePage(self.driver).open_home_page()
        account_page = home_page.header.login(USER_DELTA, PASSWORD_DELTA)
        register_domain_page = account_page.header.open_register_domain_page()
        register_domain_page.enter_domain_to_register(register_domain_page._domain_name_value_co_pl)
        WebDriverWait(self.driver, 15).until(EC.text_to_be_present_in_element(register_domain_page._domain_status_field, u"Dostępna do rejestracji"))
        register_domain_page.register_domain_immediately()
        WebDriverWait(self.driver, 15).until(EC.text_to_be_present_in_element(register_domain_page._result_text_field, u"Domena zarejestrowana poprawnie"))
        registered_domains_page = account_page.header.open_registered_domains_list()
        registered_domains_page.search_for_auction(register_domain_page._domain_name_value_co_pl)
        registered_domains_page.wait_until_domain_is_visible()
        registered_domains_page.select_first_searched_auction()
        registered_domains_page.get_authinfo()
        print register_domain_page._domain_name_value_co_pl
        WebDriverWait(self.driver, 30).until(EC.text_to_be_present_in_element(registered_domains_page._result_text_field, u"Kod AuthInfo:"))

        registered_domains_page.store_authinfo()
        print registered_domains_page._authinfo
        account_page = home_page.header.logout()
        account_page = home_page.header.login(USER, PASSWORD)
        transfer_domain_page = account_page.header.open_transfer_domain_to_account_list()
        transfer_domain_page.transfer_domain(register_domain_page._domain_name_value_co_pl, registered_domains_page._authinfo)

        WebDriverWait(self.driver, 30).until(EC.text_to_be_present_in_element(transfer_domain_page._stage2_result_field, u"Domena zostanie przeniesiona z innego konta"))
        Assert.equal(register_domain_page._domain_name_value_co_pl, transfer_domain_page.stage2_domain_text())

        transfer_domain_page.stage2_change_dns_servers_and_submit()

        WebDriverWait(self.driver, 30).until(EC.text_to_be_present_in_element(registered_domains_page._result_text_field, u"Transfer domeny został zainicjowany"))
        Assert.equal(register_domain_page._domain_name_value_co_pl, registered_domains_page.result_domain_text())

        transfer_domain_page = account_page.header.open_transfer_domain_to_account_list()
        Assert.contains(register_domain_page._domain_name_value_co_pl, registered_domains_page.get_page_source())

        transfer_domain_page.cancel_all_domain_transfers()
        self.not_contains(register_domain_page._domain_name_value_co_pl, transfer_domain_page.get_page_source())

        account_page = home_page.header.logout()
        account_page = home_page.header.login(USER_DELTA, PASSWORD_DELTA)
        transfer_domains_page = account_page.header.open_transfer_domain_from_account_list()
        self.not_contains(register_domain_page._domain_name_value_co_pl, transfer_domains_page.get_page_source())

        registered_domains_page = account_page.header.open_registered_domains_list()
        registered_domains_page.search_for_auction(register_domain_page._domain_name_value_co_pl)
        registered_domains_page.select_first_searched_auction()
        registered_domains_page.delete_auction()
        WebDriverWait(self.driver, 15).until(EC.text_to_be_present_in_element(registered_domains_page._result_text_field, u"Domena została usunięta"))
        Assert.equal(register_domain_page._domain_name_value_co_pl, registered_domains_page.result_domain_text())

    def test_transfer_domain_to_the_other_account_and_renew_should_succeed(self):
        home_page = HomePage(self.driver).open_home_page()
        account_page = home_page.header.login(USER_DELTA, PASSWORD_DELTA)
        register_domain_page = account_page.header.open_register_domain_page()
        register_domain_page.enter_domain_to_register(register_domain_page._domain_name_value_co_pl)
        WebDriverWait(self.driver, 15).until(EC.text_to_be_present_in_element(register_domain_page._domain_status_field, u"Dostępna do rejestracji"))
        register_domain_page.register_domain_immediately()
        WebDriverWait(self.driver, 15).until(EC.text_to_be_present_in_element(register_domain_page._result_text_field, u"Domena zarejestrowana poprawnie"))
        registered_domains_page = account_page.header.open_registered_domains_list()
        registered_domains_page.search_for_auction(register_domain_page._domain_name_value_co_pl)
        registered_domains_page.wait_until_domain_is_visible()
        registered_domains_page.select_first_searched_auction()
        registered_domains_page.get_authinfo()
        print register_domain_page._domain_name_value_co_pl
        WebDriverWait(self.driver, 30).until(EC.text_to_be_present_in_element(registered_domains_page._result_text_field, u"Kod AuthInfo:"))

        registered_domains_page.store_authinfo()
        print registered_domains_page._authinfo
        account_page = home_page.header.logout()
        account_page = home_page.header.login(USER, PASSWORD)
        transfer_domain_page = account_page.header.open_transfer_domain_to_account_list()
        transfer_domain_page.transfer_domain_and_renew(register_domain_page._domain_name_value_co_pl, registered_domains_page._authinfo)

        WebDriverWait(self.driver, 30).until(EC.text_to_be_present_in_element(transfer_domain_page._stage2_result_field, u"Domena zostanie przeniesiona z innego konta"))
        Assert.equal(register_domain_page._domain_name_value_co_pl, transfer_domain_page.stage2_domain_text())

        transfer_domain_page.stage2_change_dns_servers_and_submit()

        WebDriverWait(self.driver, 30).until(EC.text_to_be_present_in_element(registered_domains_page._result_text_field, u"Transfer domeny został zainicjowany"))
        Assert.equal(register_domain_page._domain_name_value_co_pl, registered_domains_page.result_domain_text())

        transfer_domain_page = account_page.header.open_transfer_domain_to_account_list()
        Assert.contains(register_domain_page._domain_name_value_co_pl, registered_domains_page.get_page_source())

        transfer_domain_page.cancel_all_domain_transfers()
        self.not_contains(register_domain_page._domain_name_value_co_pl, transfer_domain_page.get_page_source())

        account_page = home_page.header.logout()
        account_page = home_page.header.login(USER_DELTA, PASSWORD_DELTA)
        transfer_domains_page = account_page.header.open_transfer_domain_from_account_list()
        self.not_contains(register_domain_page._domain_name_value_co_pl, transfer_domains_page.get_page_source())

        registered_domains_page = account_page.header.open_registered_domains_list()
        registered_domains_page.search_for_auction(register_domain_page._domain_name_value_co_pl)
        registered_domains_page.select_first_searched_auction()
        registered_domains_page.delete_auction()
        WebDriverWait(self.driver, 15).until(EC.text_to_be_present_in_element(registered_domains_page._result_text_field, u"Domena została usunięta"))
        Assert.equal(register_domain_page._domain_name_value_co_pl, registered_domains_page.result_domain_text())

    def test_transfer_domain_to_the_other_account_wrong_data_should_succeed(self):

        _wrong_domain = get_random_uuid(10)+".co.pl"
        _wrong_authinfo = get_random_uuid(10)

        home_page = HomePage(self.driver).open_home_page()
        account_page = home_page.header.login(USER_DELTA, PASSWORD_DELTA)
        transfer_domain_page = account_page.header.open_transfer_domain_to_account_list()
        transfer_domain_page.transfer_domain(_wrong_domain, _wrong_authinfo)

        WebDriverWait(self.driver, 30).until_not(EC.text_to_be_present_in_element(transfer_domain_page._stage2_result_field, u"Trwa sprawdzanie domeny"))

        if u"Niepoprawny kod AuthInfo: %s" % _wrong_domain in transfer_domain_page.stage2_result_text():
            Assert.equal(_wrong_domain, transfer_domain_page.stage2_domain_text())
        else:
            WebDriverWait(self.driver, 20).until(EC.text_to_be_present_in_element(transfer_domain_page._stage2_result_field, u"Domena nie istnieje"))
            Assert.equal(_wrong_domain, transfer_domain_page.stage2_domain_text())


    def test_search_expired_options_should_succeed(self):
        home_page = HomePage(self.driver).open_home_page()
        account_page = home_page.header.login(USER_DELTA, PASSWORD_DELTA)
        expired_options_page = account_page.header.open_expired_options_list()
        expired_options_page.get_text_sixth_option()
        expired_options_page.search_for_option(expired_options_page.sixth_option_text)

        WebDriverWait(self.driver, 30).until(EC.text_to_be_present_in_element(expired_options_page._first_option_value, expired_options_page.sixth_option_text))

    def test_register_option_should_succeed(self):
        home_page = HomePage(self.driver).open_home_page()
        account_page = home_page.header.login(USER_DELTA, PASSWORD_DELTA)
        register_domain_page = account_page.header.open_register_domain_page()
        register_domain_page.enter_domain_to_register(register_domain_page._domain_name_value_waw_pl)
        WebDriverWait(self.driver, 15).until(EC.text_to_be_present_in_element(register_domain_page._domain_status_field, u"Dostępna do rejestracji"))
        register_domain_page.register_domain_immediately()
        WebDriverWait(self.driver, 15).until(EC.text_to_be_present_in_element(register_domain_page._result_text_field, u"Domena zarejestrowana poprawnie"))
        to_pay_list = account_page.header.open_to_pay_list()
        to_pay_list.remove_all_payments()
        register_option_page = account_page.header.open_register_option_page()
        register_option_page.enter_option_to_register(register_domain_page._domain_name_value_waw_pl)

        WebDriverWait(self.driver, 30).until(EC.text_to_be_present_in_element(register_option_page._stage2_result_field, u"Dostępna."))
        Assert.equal(register_domain_page._domain_name_value_waw_pl, register_option_page.stage2_domain_text())

        register_option_page.submit_and_accept_alert()

        WebDriverWait(self.driver, 30).until(EC.text_to_be_present_in_element(register_option_page._result_text_field, u"Operacja zawieszona, oczekuje na aktywowanie"))
        Assert.equal(register_domain_page._domain_name_value_waw_pl, register_option_page.result_domain_text())

        to_pay_list = account_page.header.open_to_pay_list()
        Assert.contains(register_domain_page._domain_name_value_waw_pl, to_pay_list.get_page_source())
        Assert.contains(u"Rejestracja opcji", to_pay_list.get_page_source())

        to_pay_list.remove_all_payments()
        to_pay_list.refresh()
        self.not_contains(register_domain_page._domain_name_value_waw_pl, to_pay_list.get_page_source())
        self.not_contains(u"Rejestracja opcji", to_pay_list.get_page_source())

    def test_register_option_unavailable_should_succeed(self):

        _unavailable_option = get_random_uuid(8)+".unavailabla.pl"

        home_page = HomePage(self.driver).open_home_page()
        account_page = home_page.header.login(USER_DELTA, PASSWORD_DELTA)
        register_option_page = account_page.header.open_register_option_page()
        register_option_page.enter_option_to_register(_unavailable_option)

        WebDriverWait(self.driver, 30).until(EC.text_to_be_present_in_element(register_option_page._stage2_result_field, u"Niedostępna"))
        Assert.equal(_unavailable_option, register_option_page.stage2_domain_text())

    # W DRUGIM KROKU NAZWA OPCJI WYŚWIETLA SIĘ BEZ PRZEDROSTKA (SAMO UNAVAILABLA.PL), zgłoszone

    def test_change_option_profile_data_should_succeed(self):
        home_page = HomePage(self.driver).open_home_page()
        account_page = home_page.header.login(USER_DELTA, PASSWORD_DELTA)
        registered_options_list = account_page.header.open_registered_options_list()
        registered_options_list.first_option_text()
        registered_options_list.change_option_profile_data()

        WebDriverWait(self.driver, 30).until(EC.text_to_be_present_in_element(registered_options_list._result_text_field, u"Ustawiono profil danych:"))
        Assert.equal(registered_options_list._first_option_text_value, registered_options_list.result_domain_text())

    def test_get_option_authinfo_should_succeed(self):
        home_page = HomePage(self.driver).open_home_page()
        account_page = home_page.header.login(USER_DELTA, PASSWORD_DELTA)
        registered_options_list = account_page.header.open_registered_options_list()
        registered_options_list.third_option_text()
        registered_options_list.get_option_authinfo()

        WebDriverWait(self.driver, 30).until(EC.text_to_be_present_in_element(registered_options_list._result_text_field, u"Kod AuthInfo:"))
        Assert.equal(registered_options_list._third_option_text_value, registered_options_list.result_domain_text())

    def test_renew_option_should_succeed(self):
        home_page = HomePage(self.driver).open_home_page()
        account_page = home_page.header.login(USER_DELTA, PASSWORD_DELTA)
        to_pay_list = account_page.header.open_to_pay_list()
        to_pay_list.remove_all_payments()
        registered_options_list = account_page.header.open_registered_options_list()
        registered_options_list.first_option_text()
        renew_option = registered_options_list.renew_option()

        WebDriverWait(self.driver, 30).until(EC.text_to_be_present_in_element(registered_options_list._stage2_result_field, u"Opcja może być odnowiona"))
        Assert.equal(registered_options_list._first_option_text_value, registered_options_list.stage2_option_text())

        registered_options_list.second_stage_checkboxes_and_submit()

        WebDriverWait(self.driver, 30).until_not(EC.text_to_be_present_in_element(registered_options_list._result_text_field, u"Operacja w toku"))

        if u"Operacja zawieszona, oczekuje na aktywowanie" in registered_options_list.result_text():
            Assert.equal(registered_options_list._first_option_text_value, registered_options_list.result_domain_text())

        to_pay_list = account_page.header.open_to_pay_list()

        Assert.contains(registered_options_list._first_option_text_value, to_pay_list.get_page_source())
        Assert.contains(u"Odnowienie opcji", to_pay_list.get_page_source())

        to_pay_list.remove_all_payments()
        to_pay_list.refresh()

        self.not_contains(registered_options_list._first_option_text_value, to_pay_list.get_page_source())
        self.not_contains(u"Odnowienie opcji", to_pay_list.get_page_source())

#     def test_transfer_option_from_account_should_succeed(self):
#         login = "alfa"
#
#         home_page = HomePage(self.driver).open_home_page()
#         account_page = home_page.header.login(USER_GAMMA, PASSWORD_GAMMA)
#         internal_option_transfer_list = account_page.header.open_internal_option_transfer_list()
#         internal_option_transfer_list.delete_all_option_transfers()
#         registered_options_list = account_page.header.open_registered_options_list()
#         registered_options_list.third_option_text()
#         transfer_option = registered_options_list.transfer_option_from_account()
#         registered_options_list.transfer_option_enter_login(login)
#         registered_options_list.submit()
#
#         WebDriverWait(self.driver, 30).until(EC.text_to_be_present_in_element(registered_options_list._result_text_field, u"Transfer został zainicjowany"))
#         Assert.equal(registered_options_list._third_option_text_value, registered_options_list.result_domain_text())
#
#         account_page.header.open_internal_option_transfer_list()
#
#         Assert.equal(registered_options_list._third_option_text_value, registered_options_list.transfer_list_first_domain_text())
#         Assert.contains(u"Oczekujący", registered_options_list.get_page_source())
#
#         registered_options_list.delete_first_transfer()
#
#         WebDriverWait(self.driver, 30).until(EC.text_to_be_present_in_element(registered_options_list._stage2_result_field, u"Transfer zostanie anulowany"))
#         Assert.equal(registered_options_list._third_option_text_value, registered_options_list.stage2_option_text())
#
#         registered_options_list.submit_and_accept_alert()
#
#         WebDriverWait(self.driver, 30).until(EC.text_to_be_present_in_element(registered_options_list._result_text_field, u"Transfer został anulowany"))
#         Assert.equal(registered_options_list._third_option_text_value, registered_options_list.result_domain_text())
#
#         account_page.header.open_internal_option_transfer_list()
#
#         self.not_contains(registered_options_list._third_option_text_value, registered_options_list.get_page_source())
#         self.not_contains(u"Oczekujący", registered_options_list.get_page_source())


# DOPISAC


    def test_transfer_option_from_account_wrong_login_should_succeed(self):
        wrong_login = get_random_string(10)

        home_page = HomePage(self.driver).open_home_page()
        account_page = home_page.header.login(USER_DELTA, PASSWORD_DELTA)
        registered_options_list = account_page.header.open_registered_options_list()
        transfer_option = registered_options_list.transfer_option_from_account()
        registered_options_list.transfer_option_enter_login(wrong_login)
        registered_options_list.submit()

        Assert.contains(u"Użytkownik o podanym loginie nie istnieje", registered_options_list.get_page_source())
        Assert.contains(wrong_login, registered_options_list.get_page_source())

#     def test_transfer_option_to_account_should_succeed(self):
#
#         home_page = HomePage(self.driver).open_home_page()
#         account_page = home_page.header.login(USER_GAMMA, PASSWORD_GAMMA)
#         registered_options_list = account_page.header.open_registered_options_list()
#         registered_options_list.third_option_text()
#         registered_options_list.get_option_authinfo()
#
#         WebDriverWait(self.driver, 30).until(EC.text_to_be_present_in_element(registered_options_list._result_text_field, u"Kod AuthInfo:"))
#
#         registered_options_list.store_option_authinfo()
#
#         home_page.header.logout()
#         account_page = home_page.header.login(USER_DELTA, PASSWORD_DELTA)
#         transfer_option_list = account_page.header.open_transfer_option_to_account_list()
#         transfer_option_list.new_option_transfer(registered_options_list._third_option_text_value, registered_options_list._option_authinfo)
#
#         WebDriverWait(self.driver, 30).until(EC.text_to_be_present_in_element(registered_options_list._stage2_result_field, u"Opcja zostanie przeniesiona z innego konta"))
#         Assert.equal(registered_options_list._third_option_text_value, registered_options_list.stage2_option_text())
#
#         registered_options_list.submit_and_accept_alert()
#
#         WebDriverWait(self.driver, 30).until(EC.text_to_be_present_in_element(registered_options_list._result_text_field, u"Transfer opcji został zainicjowany"))
#         Assert.equal(registered_options_list._third_option_text_value, registered_options_list.result_domain_text())
#
#         account_page.header.open_transfer_option_to_account_list()
#
#         Assert.contains(registered_options_list._third_option_text_value, registered_options_list.get_page_source())
#         Assert.contains(strftime("%Y-%m-%d", gmtime()), registered_options_list.get_page_source())
#         Assert.contains(u"Oczekujący", registered_options_list.get_page_source())
#
#         transfer_option_list.remove_first_transfer()
#
#         WebDriverWait(self.driver, 30).until(EC.text_to_be_present_in_element(registered_options_list._stage2_result_field, u"Transfer zostanie anulowany"))
#         Assert.equal(registered_options_list._third_option_text_value, registered_options_list.stage2_option_text())
#
#         registered_options_list.submit_and_accept_alert()
#
#         WebDriverWait(self.driver, 30).until(EC.text_to_be_present_in_element(registered_options_list._result_text_field, u"Transfer został anulowany"))
#         Assert.equal(registered_options_list._third_option_text_value, registered_options_list.result_domain_text())
#
#         account_page.header.open_transfer_option_to_account_list()
#
#         self.not_contains(registered_options_list._third_option_text_value, registered_options_list.get_page_source())
#
    def test_transfer_option_to_account_option_unavailable_should_succeed(self):

        _unavailable_option = get_random_uuid(8)+".unavailable.pl"
        _wrong_authinfo = get_random_uuid(8)

        home_page = HomePage(self.driver).open_home_page()
        account_page = home_page.header.login(USER_DELTA, PASSWORD_DELTA)
        transfer_option_list = account_page.header.open_transfer_option_to_account_list()
        transfer_option_list.new_option_transfer(_unavailable_option, _wrong_authinfo)

        WebDriverWait(self.driver, 30).until(EC.text_to_be_present_in_element(transfer_option_list._stage2_result_field, u"Opcja może być przetransferowana"))
        Assert.equal(_unavailable_option, transfer_option_list.stage2_option_text())

    def test_new_hosting_account_should_succeed(self):

        home_page = HomePage(self.driver).open_home_page()
        account_page = home_page.header.login(USER_DELTA, PASSWORD_DELTA)
        to_pay_list = account_page.header.open_to_pay_list()
        to_pay_list.remove_all_payments()
        hosting_account_list = account_page.header.open_hosting_account_list()
        hosting_account_list.new_hosting_account(PASSWORD_DELTA)

        Assert.equal("Pakiet Starter", hosting_account_list.get_text_packet_type_stage_2())
        Assert.equal(hosting_account_list._new_hosting_account_login_value, hosting_account_list.get_text_login_stage_2())

        hosting_account_list.new_hosting_account_stage_2()

        WebDriverWait(self.driver, 90).until(EC.text_to_be_present_in_element(hosting_account_list._new_hosting_account_result_text_field, u"Konto hostingowe zostało utworzone i aktywowane na okres próbny 14 dni."))

        to_pay_list = account_page.header.open_to_pay_list()

        Assert.contains(hosting_account_list._new_hosting_account_login_value, to_pay_list.get_page_source())
        Assert.contains(u"Zamówienie serwera", to_pay_list.get_page_source())

        to_pay_list.remove_all_payments()
        to_pay_list.refresh()

        self.not_contains(hosting_account_list._new_hosting_account_login_value, to_pay_list.get_page_source())
        self.not_contains(u"Zamówienie serwera", to_pay_list.get_page_source())

    def test_add_domain_to_hosting_account_should_succeed(self):

        home_page = HomePage(self.driver).open_home_page()
        account_page = home_page.header.login(USER_DELTA, PASSWORD_DELTA)
        registered_domains_page = account_page.header.open_registered_domains_list()
        registered_domains_page.first_domain_text()
        hosting_account_list = account_page.header.open_hosting_account_list()
        hosting_account_list.add_domains_to_hosting_account()
        hosting_account_list.remove_all_all_domains_from_hosting_account()
        hosting_account_list.add_domains_to_hosting_account_stage2(registered_domains_page._first_domain_text_value)

        WebDriverWait(self.driver, 30).until(EC.text_to_be_present_in_element(registered_domains_page._result_text_field, u"Domena została dodana do konta:"))
        Assert.equal(registered_domains_page._first_domain_text_value, registered_domains_page.result_domain_text())

        hosting_account_list.back_from_results_page()

        Assert.contains(registered_domains_page._first_domain_text_value, hosting_account_list.get_page_source())
        Assert.contains(strftime("%Y-%m-%d", gmtime()), hosting_account_list.get_page_source())

        hosting_account_list.remove_all_all_domains_from_hosting_account()

        self.not_contains(registered_domains_page._first_domain_text_value, hosting_account_list.get_page_source())
        self.not_contains(strftime("%Y-%m-%d", gmtime()), hosting_account_list.get_page_source())

    def test_add_domain_to_hosting_account_wrong_domain_name_should_succeed(self):

        _wrong_domain_name = get_random_string(7)

        home_page = HomePage(self.driver).open_home_page()
        account_page = home_page.header.login(USER_DELTA, PASSWORD_DELTA)
        hosting_account_list = account_page.header.open_hosting_account_list()
        hosting_account_list.add_domains_to_hosting_account()
        hosting_account_list.add_domains_to_hosting_account_stage2(_wrong_domain_name)

        Assert.contains(u"Musisz podać poprawne nazwy domen", hosting_account_list.get_page_source())

    def test_zz_generate_plot_and_send_email(self):
        self._save_plot()
        self._send_email()

    def tally(self):
        return len(self._resultForDoCleanups.errors) + len(self._resultForDoCleanups.failures)

    def setUp(self):
        self.timeout = 30
        if run_locally:
            # fp = webdriver.FirefoxProfile()
            # fp.set_preference("browser.startup.homepage", "about:blank")
            # fp.set_preference("startup.homepage_welcome_url", "about:blank")
            # fp.set_preference("startup.homepage_welcome_url.additional", "about:blank")
            # fp.set_preference(" xpinstall.signatures.required", "false")
            # fp.set_preference("toolkit.telemetry.reportingpolicy.firstRun", "false")
            # binary = FirefoxBinary('/__stare/firefox45/firefox')
            # self.driver = webdriver.Firefox(firefox_binary=binary, firefox_profile=fp)
            sr_args = ["--verbose", "--log-path=chromedriver.log"]
            from selenium.webdriver.chrome.options import Options
            opts = Options()
            opts.binary_location = "/usr/bin/google-chrome"
            # opts.binary_location = "/usr/lib/chromium-browser/chromium-browser"
            opts.add_argument("--no-sandbox") #This make Chromium reachable
            opts.add_argument("--no-default-browser-check") #Overrides default choices
            opts.add_argument("--no-first-run")
            opts.add_argument("--disable-default-apps")
            self.driver = webdriver.Chrome(executable_path="/usr/lib/chromium-browser/chromedriver", service_args=sr_args, chrome_options=opts)
            # self.driver = webdriver.Chrome(service_args=sr_args, chrome_options=opts)
            self.driver.set_window_size(1024,768)
            # self.driver.implicitly_wait(self.timeout)
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
        err = len(self._resultForDoCleanups.errors)
        fail = len(self._resultForDoCleanups.failures)

        # The slices will be ordered and plotted counter-clockwise.
        labels = 'Errors', 'Failures', 'Passes'
        sizes = [err, fail, 7-err-fail]
        colors = ['red', 'gold', 'green']
        explode = (0.1, 0.1, 0.1)

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
                          To=["jedrzej.wojcieszczyk@testuj.pl"])
        message.Subject = "Raport Jenkins Aftermarket2 Testy Automatyczne"
        message.Html = """<head><meta http-equiv="Content-Type" content="text/html;charset=UTF-8"></head><p>Cześć!<br>
           Oto wygenerowany automatycznie raport z testów Aftermarket2.pl<br><br>
           Tabela raportowa z logami wykonanych testów, a pod nią linki do screenshotów i kodu html testów które nie przeszły oraz wykres statystyczny: <a href="http://ci.testuj.pl/job/Aftermarket2/ws/Aftermarket2ReportLogi.htm">Tabela z logami, screenshoty i wykres</a></p>"""

        sender = Mailer('smtp.gmail.com', use_tls=True, usr='jedrzej.wojcieszczyk@testuj.pl', pwd='paluch88')
        sender.send(message)

    def not_contains(self, needle, haystack, msg=''):
        try:
            assert not needle in haystack
        except AssertionError:
            raise AssertionError('%s is found in %s. %s' % (needle, haystack, msg))

open("Aftermarket2RaportScreeny.txt", 'w').close()
suite = unittest.TestLoader().loadTestsFromTestCase(SmokeTest)
outfile = open("Aftermarket2ReportLogi.htm", "wb")
runner = HTMLTestRunner(stream=outfile, title='Test Report', description='Aftermarket2', verbosity=2)
runner.run(suite)

     # htmltestrunner.main()
# if __name__ == '__main__':
#      unittest.main()

     # import xmlrunner
     # unittest.main(testRunner=xmlrunner.XMLTestRunner(output='test-reports'))