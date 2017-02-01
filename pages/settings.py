# coding=utf-8
from selenium.webdriver.common.by import By
from pages.base import BasePage
from utils.utils import *
from random import randint
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class SettingsPage(BasePage):
    _title = "Settings"

    _change_contact_data_button = (By.XPATH, "//div[3]/div[2]/span/a")
    _change_contact_data_name_field = (By.NAME, "name")
    _change_contact_data_name_value = get_random_string(7)+ " " +get_random_string(10)
    _change_contact_data_address_field = (By.NAME, "address")
    _change_contact_data_address_value = get_random_address()
    _change_contact_data_postalcode_field = (By.NAME, "zip")
    _change_contact_data_postalcode_value = get_random_integer(2)+"-"+get_random_integer(3)
    _change_contact_data_city_field = (By.NAME, "city")
    _change_contact_data_city_value = get_random_string(7)
    _change_contact_data_country_field = (By.NAME, "country")
    _change_contact_data_country_index = randint(1,248)
    _change_contact_data_directional_field = (By.NAME, "country3")
    _change_contact_data_directional_index = randint(1, 216)
    _change_contact_data_phone_number_field = (By.NAME, "phone")
    _change_contact_data_phone_number_value = get_random_integer(9)
    _change_contact_data_save_button = (By.XPATH, "//button")
    _change_email_notification_settings_button = (By.XPATH, "//span[2]/a")
    _change_email_notification_settings_send_only_indicated_button = (By.XPATH, "//label[2]")
    _change_email_notification_settings_about_account_condition_checkbox = (By.XPATH, "(//b[contains(text(),'Powiadomienia o stanie konta ')])")
    _change_email_notification_settings_about_domain_condition_change_checkbox = (By.XPATH, "//label[17]/b")
    _change_email_notification_settings_about_option_condition_change_checkbox = (By.XPATH, "//label[26]/b")
    _change_email_notification_settings_about_catching_domains_checkbox = (By.XPATH, "//label[42]/b")
    _change_email_notification_settings_about_purchase_at_auction_checkbox = (By.XPATH, "//label[52]/b")
    _change_email_notification_settings_about_purchase_at_escrow_checkbox = (By.XPATH, "//label[60]/b")
    _change_email_notification_settings_about_sale_at_auction_checkbox = (By.XPATH, "(//b[contains(text(),'Powiadomienia o sprzedaży na aukcjach ')])")
    _change_email_notification_settings_about_sale_at_escrow_checkbox = (By.XPATH, "(//b[contains(text(),'Powiadomienia o sprzedaży w transakcji Escrow ')])")
    _change_email_notification_settings_about_made_operations_checkbox = (By.XPATH, "(//b[contains(text(),'Powiadomienia o wykonanych operacjach ')])")
    _change_email_notification_settings_save_button = (By.XPATH, "//div[2]/button")
    _change_newsletter_settings_button = (By.PARTIAL_LINK_TEXT, u"Wyłącz otrzymywanie newsletterów")
    _change_newsletter_settings_overall_checkbox = (By.XPATH, "//label/b")
    _change_newsletter_settings_according_to_domain_market_checkbox = (By.XPATH, "(//b[contains(text(),'Newslettery związane z giełdą domen')])")
    _change_newsletter_settings_according_to_catching_domains_checkbox = (By.XPATH, "(//b[contains(text(),'Newslettery związane z przechwytywaniem domen')])")
    _change_newsletter_settings_according_to_watched_domains_checkbox = (By.XPATH, "(//b[contains(text(),'Newslettery związane z obserwowanymi domenami')])")
    _change_newsletter_settings_save_button = (By.XPATH, "//div[2]/button")
    _add_email_address_menu = (By.PARTIAL_LINK_TEXT, u"Zmień lub dodaj adres email")
    _add_email_address_button = (By.XPATH, "//button")
    _add_email_address_field = (By.NAME, "email")
    _add_email_address_value = "zz"+get_random_string(7)+"@ijasdnjiasnd.pl"
    _add_email_address_submit = (By.XPATH, "//div[2]/button")
    _add_email_address_header = (By.XPATH, "//h1")
    _back_to_email_addresses_list_button = (By.XPATH, "//button")
    _added_email_field = (By.XPATH, "//tbody[2]/tr/td[3]/div")
    _added_email_status_field = (By.XPATH, "//tbody[2]/tr/td[5]/div")
    _add_email_address_remove_added_email = (By.XPATH, "//td[6]/div/a/img")
    _add_email_address_remove_added_email_confirm = (By.XPATH, "//div[3]/button")
    _add_other_users_menu = (By.XPATH, "//div[4]/div[2]/span[3]/a")
    _add_other_user_button = (By.XPATH, "//button")
    _add_other_user_login_field = (By.NAME, "login")
    _add_other_user_login_value = "zz"+get_random_string(9)
    _add_other_user_password_field = (By.NAME, "password")
    _add_other_user_password_value = get_random_string(9)
    _add_other_user_repeat_password_field = (By.NAME, "password2")
    _add_other_user_description_field = (By.NAME, "description")
    _add_other_user_description_value = get_random_string(7)+ " " +get_random_string(10)+ " " +get_random_string(11)
    _add_other_user_can_do_only_few_operations_radio = (By.XPATH, "//label[2]/span[2]")
    _add_other_user_management_of_account_balance_checkbox = (By.XPATH, "(//b[contains(text(),'Zarządzanie saldem konta ')])")
    _add_other_user_management_of_domains_to_pay_checkbox = (By.XPATH, "(//b[contains(text(),'Zarządzanie domenami do opłacenia ')])")
    _add_other_user_management_of_invoices_checkbox = (By.XPATH, "(//b[contains(text(),'Zarządzanie fakturami ')])")
    _add_other_user_management_of_withdrawals_checkbox = (By.XPATH, "(//b[contains(text(),'Zarządzanie wypłatami z konta ')])")
    _add_other_user_management_of_bank_accounts_checkbox = (By.XPATH, "(//b[contains(text(),'Zarządzanie kontami bankowymi ')])")
    _add_other_user_management_of_domains_checkbox = (By.XPATH, "(//b[contains(text(),'Zarządzanie domenami ')])")
    _add_other_user_management_of_domain_transfers_to_account_checkbox = (By.XPATH, "(//b[contains(text(),'Zarządzanie transferami domen na konto ')])")
    _add_other_user_management_of_domain_transfers_from_account_checkbox = (By.XPATH, "(//b[contains(text(),'Zarządzanie transferami domen z konta ')])")
    _add_other_user_management_of_profiles_for_domain_registration_checkbox = (By.XPATH, "(//b[contains(text(),'Zarządzanie profilami do rejestracji domen ')])")
    _add_other_user_management_of_domain_parking_checkbox = (By.XPATH, "(//b[contains(text(),'Zarządzanie parkingiem domen ')])")
    _add_other_user_management_of_DNS_entries_checkbox = (By.XPATH, "(//b[contains(text(),'Zarządzanie profilami wpisów DNS ')])")
    _add_other_user_management_of_options_checkbox = (By.XPATH, "(//b[contains(text(),'Zarządzanie opcjami ')])")
    _add_other_user_management_of_option_transfers_to_account_checkbox = (By.XPATH, "(//b[contains(text(),'Zarządzanie transferami opcji na konto ')])")
    _add_other_user_management_of_option_transfers_from_account_checkbox = (By.XPATH, "(//b[contains(text(),'Zarządzanie transferami opcji z konta ')])")
    _add_other_user_change_account_settings_checkbox = (By.XPATH, "(//b[contains(text(),'Zmiana ustawień konta ')])")
    _add_other_user_management_of_email_addresses_checkbox = (By.XPATH, "(//b[contains(text(),'Zarządzanie adresami email ')])")
    _add_other_user_management_of_mobile_phones_checkbox = (By.XPATH, "(//b[contains(text(),'Zarządzanie telefonami komórkowymi ')])")
    _add_other_user_management_of_logins_checkbox = (By.XPATH, "(//b[contains(text(),'Zarządzanie loginami ')])")
    _add_other_user_management_of_data_exports_checkbox = (By.XPATH, "(//b[contains(text(),'Zarządzanie eksportami danych ')])")
    _add_other_user_save_button = (By.XPATH, "//div[2]/button")
    _add_other_user_added_login_field = (By.XPATH, "//tbody[2]/tr/td[3]/div/label")
    _add_other_user_added_description_field = (By.XPATH, "//tbody[2]/tr/td[6]/div")
    _add_other_user_remove_added_user_button = (By.XPATH, "//td[7]/div/a/img")
    _add_other_user_remove_added_user_confirm_button = (By.XPATH, "//div[3]/button")
    _add_other_user_change_priviledges_button = (By.XPATH, "//tr[8]/td/div/button")
    _change_company_data_menu = (By.XPATH, "//a[contains(text(),'Zmień dane swojej firmy')]")
    _change_company_data_company_name_field = (By.NAME, "name")
    _change_company_data_company_name_value = get_random_string(5)+' '+get_random_string(6)
    _change_company_data_street_field = (By.NAME, "address")
    _change_company_data_street_value = get_random_address()
    _change_company_data_zip_field = (By.NAME, "zip")
    _change_company_data_zip_value = get_random_integer(2)+"-"+get_random_integer(3)
    _change_company_data_city_field = (By.NAME, "city")
    _change_company_data_city_value = get_random_string(8)
    _change_company_address_save_button = (By.XPATH, "//button")
    _change_company_data_save_button = (By.XPATH, "//div[2]/button")
    _change_company_data_save_stage_2_button = (By.XPATH, "//button")
    _change_company_data_operation_succcessful = (By.XPATH, "//form/div/div")
    _change_company_data_change_company_name = (By.XPATH, "//div[2]/span/a")
    _change_company_data_change_company_name_stage_2 = (By.XPATH, "//button")
    _change_company_data_country_field = (By.NAME, "country")
    _change_company_data_country_index = get_random_integer(2)
    _change_company_data_account_type_company_radio = (By.XPATH, "//label[2]")
    _change_company_data_nip_field = (By.XPATH, "//div/input")
    _change_company_data_nip_value = "PL1234567890"
    _change_company_data_nip_result = (By.XPATH, "//div[6]/div/div[2]/div/span")
    _change_company_data_company_name_result = (By.XPATH, "//div/span")
    _change_company_data_currency_index = randint(0, 3)
    _change_company_data_currency_dropdown = (By.NAME, "currency")
    _add_bank_account_menu = (By.XPATH, "//a[contains(text(),'Dodaj lub zmień konto bankowe')]")
    _add_bank_account_button = (By.XPATH, "//button")
    _add_bank_account_account_name_field = (By.NAME, "name")
    _add_bank_account_account_name_value = get_random_string(10)
    _add_bank_account_account_number_field = (By.NAME, "account")
    _add_bank_account_receiver_name_field = (By.NAME, "recipient")
    _add_bank_account_receiver_name_value = get_random_string(15)
    _add_bank_account_submit_button = (By.XPATH, "//div[2]/button")
    _added_bank_account_number = (By.XPATH, "//td[3]/div")
    _added_bank_account_name = (By.XPATH, "//td[4]/div")
    _added_bank_account_remove_first_accouunt_button = (By.XPATH, "//td[5]/div/a/img")
    _added_bank_account_remove_first_accouunt_confirm_button = (By.XPATH, "//div[3]/button")
    _change_DNS_servers_menu = (By.XPATH, "//a[contains(text(),'Zmień domyślne serwery DNS')]")
    _change_DNS_servers_dropdown = (By.NAME, "dns")
    _change_DNS_servers_DNS3_field = (By.NAME, "ns3")
    _change_DNS_servers_DNS3_value = get_random_uuid(2)+"."+get_random_string(8)+".pl"
    _change_DNS_servers_DNS4_field = (By.NAME, "ns4")
    _change_DNS_servers_DNS4_value = get_random_uuid(2)+"."+get_random_string(8)+".pl"
    _change_DNS_servers_DNS1_field = (By.NAME, "ns1")
    _change_DNS_servers_DNS2_field = (By.NAME, "ns2")
    _change_DNS_servers_submit_button = (By.XPATH, "//div[2]/button")
    _change_DNS_servers_operation_successful = (By.XPATH, "/html/body/div[7]/div/div/form/div[1]")
    _new_DNS_profile_menu = (By.XPATH, "//a[contains(text(),'Zdefiniuj szablony wpisów DNS')]")
    _new_DNS_profile_button = (By.XPATH, "//button")
    _new_DNS_profile_name_field = (By.NAME, "name")
    _new_DNS_profile_name_value = get_random_string(10)
    _new_DNS_profile_name_submit = (By.XPATH, "//div[2]/button")
    _new_DNS_profile_host_field = (By.NAME, "host")
    _new_DNS_profile_host_value = get_random_string(7)
    _new_DNS_profile_type_dropdown = (By.NAME, "type")
    _new_DNS_profile_address_field = (By.NAME, "value")
    _new_DNS_profile_address_value = "172."+get_random_integer(2)+"."+get_random_integer(1)+"."+get_random_integer(1)
    _new_DNS_profile_submit = (By.XPATH, "//div[2]/button")
    _new_DNS_profile_successful_operation = (By.XPATH, "//form/div/div")
    _new_DNS_profile_successtul_opertation_profile = (By.XPATH, "//div/span")
    _new_DNS_profile_name = (By.XPATH, "//tbody[2]/tr/td[3]/div")
    _new_DNS_profile_manage_entries = (By.XPATH, "//td/div/button")
    _new_DNS_profile_add_new_DNS_entry_button = (By.XPATH, "//button")
    _new_DNS_profile_delete_first_profile = (By.XPATH, "//td[6]/div/a/img")
    _new_DNS_profile_delete_first_profile_confirm = (By.XPATH, "//div[3]/button")
    _notifications_about_ending_auctions_menu = (By.XPATH, "//a[contains(text(),'Powiadomienia o aukcjach')]")
    _notifications_about_ending_auctions_email_15_min = (By.XPATH, "//label")
    _notifications_about_ending_auctions_email_30_min = (By.XPATH, "//label[2]")
    _notifications_about_ending_auctions_email_1_hr = (By.XPATH, "//label[3]")
    _notifications_about_ending_auctions_email_2_hr  = (By.XPATH, "//label[4]")
    _notifications_about_ending_auctions_email_3_hr = (By.XPATH, "//label[5]")
    _notifications_about_ending_auctions_email_6_hr = (By.XPATH, "//label[6]")
    _notifications_about_ending_auctions_email_12_hr = (By.XPATH, "//label[7]")
    _notifications_about_ending_auctions_email_24_hr = (By.XPATH, "//label[8]")
    _notifications_about_ending_auctions_sms_15_min = (By.XPATH, "//div[3]/div/div[2]/div/div/label")
    _notifications_about_ending_auctions_sms_30_min = (By.XPATH, "//div[3]/div/div[2]/div/div/label[2]")
    _notifications_about_ending_auctions_sms_1_hr = (By.XPATH, "//div[3]/div/div[2]/div/div/label[3]")
    _notifications_about_ending_auctions_sms_2_hr  = (By.XPATH, "//div[3]/div/div[2]/div/div/label[4]")
    _notifications_about_ending_auctions_sms_3_hr = (By.XPATH, "//div[3]/div/div[2]/div/div/label[5]")
    _notifications_about_ending_auctions_sms_6_hr = (By.XPATH, "//div[3]/div/div[2]/div/div/label[6]")
    _notifications_about_ending_auctions_sms_12_hr = (By.XPATH, "//div[3]/div/div[2]/div/div/label[7]")
    _notifications_about_ending_auctions_sms_24_hr = (By.XPATH, "//div[3]/div/div[2]/div/div/label[8]")
    _notifications_about_ending_auctions_submit_button = (By.XPATH, "//div[2]/button")
    _domain_watching_settings_menu = (By.XPATH, "//a[contains(text(),'Ustawienia obserwacji domen')]")
    _domain_watching_settings_domain_set_on_auction_checkbox = (By.XPATH, "//label[2]")
    _domain_watching_settings_domain_set_on_last_minute_auction_checkbox = (By.XPATH, "//label[3]")
    _domain_watching_settings_domain_set_on_sale_checkbox = (By.XPATH, "//label[4]")
    _domain_watching_settings_buy_now_is_set_checkbox = (By.XPATH, "//label[5]")
    _domain_watching_settings_buy_now_is_lowered_checkbox = (By.XPATH, "//label[6]")
    _domain_watching_settings_buy_now_is_increased_checkbox = (By.XPATH, "//label[7]")
    _domain_watching_settings_domain_removed_from_market_checkbox = (By.XPATH, "//label[8]")
    _domain_watching_settings_domain_available_to_buy_in_instalments_checkbox = (By.XPATH, "//label[9]")
    _domain_watching_settings_domain_available_to_lease_checkbox = (By.XPATH, "//label[10]")
    _domain_watching_settings_domain_available_to_catch_checkbox = (By.XPATH, "//label[11]")
    _domain_watching_settings_submit_button = (By.XPATH, "//div[2]/button")
    _sellers_watching_settings_menu = (By.XPATH, "//a[contains(text(),'Ustawienia obserwacji sprzedawców')]")
    _sellers_watching_settings_domain_set_on_auction_checkbox = (By.XPATH, "//label[2]")
    _sellers_watching_settings_domain_set_on_last_minute_auction_checkbox = (By.XPATH, "//label[3]")
    _sellers_watching_settings_domain_set_on_sale_checkbox = (By.XPATH, "//label[4]")
    _sellers_watching_settings_buy_now_is_set_checkbox = (By.XPATH, "//label[5]")
    _sellers_watching_settings_buy_now_is_lowered_checkbox = (By.XPATH, "//label[6]")
    _sellers_watching_settings_buy_now_is_increased_checkbox = (By.XPATH, "//label[7]")
    _sellers_watching_settings_domain_removed_from_market_checkbox = (By.XPATH, "//label[8]")
    _sellers_watching_settings_domain_available_to_buy_in_instalments_checkbox = (By.XPATH, "//label[9]")
    _sellers_watching_settings_domain_available_to_lease_checkbox = (By.XPATH, "//label[10]")
    _sellers_watching_settings_domain_available_to_catch_checkbox = (By.XPATH, "//label[11]")
    _sellers_watching_settings_submit_button = (By.XPATH, "//div[2]/button")
    _change_seller_profile_menu = (By.XPATH, "//a[contains(text(),'Zmień opis w profilu')]")
    _change_seller_profile_description_value = get_random_string(7)+' '+get_random_string(8)+' '+get_random_string(6)
    _change_seller_profile_description_field = (By.XPATH, "//div/div[2]/div/div/div")
    _change_seller_profile_description_field_after_submit = (By.XPATH, "//div/div[2]/div/div/div")
    _change_seller_profile_submit_button = (By.XPATH, "//div[2]/button")
    _sending_notification_settings_menu = (By.XPATH, "//a[contains(text(),'Wyłącz wysyłanie powiadomień')]")
    _sending_notification_settings_domain_set_on_auction_checkbox = (By.XPATH, "//label[2]")
    _sending_notification_settings_domain_set_on_last_minute_auction_checkbox = (By.XPATH, "//label[3]")
    _sending_notification_settings_domain_set_on_sale_checkbox = (By.XPATH, "//label[4]")
    _sending_notification_settings_buy_now_is_set_checkbox = (By.XPATH, "//label[5]")
    _sending_notification_settings_buy_now_is_lowered_checkbox = (By.XPATH, "//label[6]")
    _sending_notification_settings_buy_now_is_increased_checkbox = (By.XPATH, "//label[7]")
    _sending_notification_settings_domain_removed_from_market_checkbox = (By.XPATH, "//label[8]")
    _sending_notification_settings_domain_available_to_buy_in_instalments_checkbox = (By.XPATH, "//label[9]")
    _sending_notification_settings_domain_available_to_lease_checkbox = (By.XPATH, "//label[10]")
    _sending_notification_settings_domain_available_to_catch_checkbox = (By.XPATH, "//label[11]")
    _sending_notification_settings_submit_button = (By.XPATH, "//div[2]/button")
    _sms_notification_settings_menu = (By.XPATH, "(//a[contains(text(),'Wyłącz otrzymywanie powiadomień')])[2]")
    _sms_notification_settings_first_phone_number_field = (By.XPATH, "//td[3]/div")
    _sms_notification_settings_first_phone_number_notifications_button = (By.XPATH, "//tr[3]/td/div/span")
    _sms_notification_settings_send_only_indicated = (By.XPATH, "//label[2]")
    _sms_notification_settings_auction_ends_soon = (By.XPATH, "//div[2]/div/div/label[2]")
    _sms_notification_settings_your_offer_was_gazumped = (By.XPATH, "//div[2]/div/div/label[3]")
    _sms_notification_settings_you_won_an_auction = (By.XPATH, "//label[4]")
    _sms_notification_settings_successful_domain_catching = (By.XPATH, "//label[5]")
    _sms_notification_settings_catched_domain_auction_has_started = (By.XPATH, "//label[6]")
    _sms_notification_settings_payment_date_is_comming = (By.XPATH, "//label[7]")
    _sms_notification_settings_payment_date_is_exceeded = (By.XPATH, "//label[8]")
    _change_sms_notification_settings_first_group_button = (By.XPATH, "//div[2]/div/div/label[%s]" %randint(2,3))
    _change_sms_notification_settings_second_group_button = (By.XPATH, "//label[%s]" %randint(4,9))
    _sms_notification_settings_submit = (By.XPATH, "//div[2]/button")
    _back_from_results_page_button = (By.XPATH, "//button")
    _confirmation_result_field = (By.XPATH, "//div/span")
    _confirmation_result_text = (By.XPATH, "//td[3]")

    def __init__(self, driver):
        super(SettingsPage, self).__init__(driver, self._title)

    def open_change_contact_data_page(self):
        self.click(self._change_contact_data_button)

    def fill_change_contact_data_form(self):
        self.clear_field_and_send_keys(self._change_contact_data_name_value, self._change_contact_data_name_field)
        self.clear_field_and_send_keys(self._change_contact_data_address_value, self._change_contact_data_address_field)
        self.clear_field_and_send_keys(self._change_contact_data_postalcode_value, self._change_contact_data_postalcode_field)
        self.clear_field_and_send_keys(self._change_contact_data_city_value, self._change_contact_data_city_field)
        self.select_index_from_dropdown(self._change_contact_data_country_index, self._change_contact_data_country_field)
        self.select_index_from_dropdown(self._change_contact_data_directional_index, self._change_contact_data_directional_field)
        self.clear_field_and_send_keys(self._change_contact_data_phone_number_value, self._change_contact_data_phone_number_field)

    def save_change_contact_data(self):
        self.click(self._change_contact_data_save_button)

    def change_contact_data_name_field_text(self):
        return self.get_value(self._change_contact_data_name_field)

    def change_contact_data_address_field_text(self):
        return self.get_value(self._change_contact_data_address_field)

    def change_contact_data_postalcode_field_text(self):
        return self.get_value(self._change_contact_data_postalcode_field)

    def change_contact_data_city_field_text(self):
        return self.get_value(self._change_contact_data_city_field)

    def open_change_email_notification_settings_page(self):
        self.click(self._change_email_notification_settings_button)

    def change_email_notification_settings(self):
        self.click(self._change_email_notification_settings_send_only_indicated_button)
        self.click(self._change_email_notification_settings_about_account_condition_checkbox)
        self.get_driver().execute_script("window.scrollTo(2700, 320);")
        self.click(self._change_email_notification_settings_about_domain_condition_change_checkbox)
        self.click(self._change_email_notification_settings_about_option_condition_change_checkbox)
        self.get_driver().execute_script("window.scrollTo(2700, 1000);")
        self.click(self._change_email_notification_settings_about_purchase_at_auction_checkbox)
        self.get_driver().execute_script("window.scrollTo(2700, 1200);")
        self.click(self._change_email_notification_settings_about_purchase_at_escrow_checkbox)
        self.get_driver().execute_script("window.scrollTo(2700, 1400);")
        self.click(self._change_email_notification_settings_about_sale_at_auction_checkbox)
        self.click(self._change_email_notification_settings_about_sale_at_escrow_checkbox)
        self.click(self._change_email_notification_settings_about_made_operations_checkbox)

    def save_change_email_notification_settings(self):
        self.click(self._change_email_notification_settings_save_button)

    def open_change_newsletter_settings_page(self):
        self.click(self._change_newsletter_settings_button)

    def change_newsletter_settings(self):
        self.click(self._change_newsletter_settings_overall_checkbox)
        self.click(self._change_newsletter_settings_according_to_domain_market_checkbox)
        self.click(self._change_newsletter_settings_according_to_catching_domains_checkbox)
        self.get_driver().execute_script("window.scrollTo(2700, 1000);")
        self.click(self._change_newsletter_settings_according_to_watched_domains_checkbox)

    def save_change_newsletter_settings(self):
        self.click(self._change_newsletter_settings_save_button)

    def open_add_email_address_page(self):
        self.click(self._add_email_address_menu)

    def add_email_address(self):
        self.click(self._add_email_address_button)
        self.clear_field_and_send_keys(self._add_email_address_value, self._add_email_address_field)
        self.click(self._add_email_address_submit)

    def back_to_email_addresses_list(self):
        self.click(self._back_to_email_addresses_list_button)

    def added_email_address_text(self):
        return self.get_text(self._added_email_field)

    def added_email_status_text(self):
        return self.get_text(self._added_email_status_field)

    def remove_all_email_addresses(self):
        while True:
            if "/assets/img/table/delete.svg" in self.get_page_source():
                self.click(self._add_email_address_remove_added_email)
                self.click(self._add_email_address_remove_added_email_confirm)
                WebDriverWait(self.get_driver(), 15).until(EC.text_to_be_present_in_element(self._confirmation_result_text, u"Operacja wykonana poprawnie"))
                self.click(self._back_to_email_addresses_list_button)
                WebDriverWait(self.get_driver(), 15).until(EC.text_to_be_present_in_element(self._add_email_address_header, u"Lista adresów email"))
            else:
                break

    def open_add_other_users_page(self):
        self.click(self._add_other_users_menu)

    def remove_all_users(self):
        while True:
            if "/assets/img/table/delete.svg" in self.get_page_source():
                self.click(self._add_other_user_remove_added_user_button)
                self.click(self._add_other_user_remove_added_user_confirm_button)
                WebDriverWait(self.get_driver(), 15).until(EC.text_to_be_present_in_element(self._confirmation_result_text, u"Login został usunięty"))
                self.click(self._back_from_results_page_button)
            else:
                break

    def add_other_user(self):
        self.click(self._add_other_user_button)
        self.clear_field_and_send_keys(self._add_other_user_login_value, self._add_other_user_login_field)
        self.clear_field_and_send_keys(self._add_other_user_password_value, self._add_other_user_password_field)
        self.clear_field_and_send_keys(self._add_other_user_password_value, self._add_other_user_repeat_password_field)
        self.clear_field_and_send_keys(self._add_other_user_description_value, self._add_other_user_description_field)
        self.click(self._add_other_user_save_button)
        sleep(2)

    def add_other_user_change_priviledges(self):
        self.click(self._add_other_user_can_do_only_few_operations_radio)
        self.click(self._add_other_user_management_of_account_balance_checkbox)
        self.click(self._add_other_user_management_of_domains_to_pay_checkbox)
        self.click(self._add_other_user_management_of_invoices_checkbox)
        self.get_driver().execute_script("window.scrollTo(2700, 500);")
        self.click(self._add_other_user_management_of_withdrawals_checkbox)
        self.click(self._add_other_user_management_of_bank_accounts_checkbox)
        self.get_driver().execute_script("window.scrollTo(2700, 1000);")
        self.click(self._add_other_user_management_of_domains_checkbox)
        self.get_driver().execute_script("window.scrollTo(2700, 1000);")
        self.click(self._add_other_user_management_of_domain_transfers_from_account_checkbox)
        self.click(self._add_other_user_management_of_domain_transfers_to_account_checkbox)
        self.click(self._add_other_user_management_of_profiles_for_domain_registration_checkbox)
        self.click(self._add_other_user_management_of_domain_parking_checkbox)
        self.get_driver().execute_script("window.scrollTo(2700, 1600);")
        # self.click(self._add_other_user_management_of_DNS_entries_checkbox)
        self.click(self._add_other_user_management_of_options_checkbox)
        self.click(self._add_other_user_management_of_option_transfers_from_account_checkbox)
        self.click(self._add_other_user_management_of_option_transfers_to_account_checkbox)
        self.get_driver().execute_script("window.scrollTo(2700, 5000);")
        self.click(self._add_other_user_change_account_settings_checkbox)
        self.click(self._add_other_user_management_of_email_addresses_checkbox)
        self.click(self._add_other_user_management_of_mobile_phones_checkbox)
        self.click(self._add_other_user_management_of_logins_checkbox)
        self.click(self._add_other_user_management_of_data_exports_checkbox)
        self.click(self._add_other_user_save_button)

    def added_user_login_text(self):
        return self.get_text(self._add_other_user_added_login_field)

    def added_user_description_text(self):
        return self.get_text(self._add_other_user_added_description_field)

    def open_change_company_data_page(self):
        self.click(self._change_company_data_menu)

    def edit_company_address(self):
        # self.clear_field_and_send_keys(self._change_company_data_company_name_value, self._change_company_data_company_name_field)
        self.clear_field_and_send_keys(self._change_company_data_street_value, self._change_company_data_street_field)
        self.clear_field_and_send_keys(self._change_company_data_zip_value, self._change_company_data_zip_field)
        self.clear_field_and_send_keys(self._change_company_data_city_value, self._change_company_data_city_field)
        self.click(self._change_company_address_save_button)
        sleep(2)

    def edit_company_data_operation_successful_text(self):
        return self.get_text(self._change_company_data_operation_succcessful)

    def edit_company_data_zip_text(self):
        return self.get_value(self._change_company_data_zip_field)

    def edit_company_data_street_text(self):
        return self.get_value(self._change_company_data_street_field)

    def edit_company_data_city_text(self):
        return self.get_value(self._change_company_data_city_field)

    def edit_company_data(self):
        self.click(self._change_company_data_change_company_name)
        self.click(self._change_company_data_change_company_name_stage_2)
        sleep(2)
        self.select_index_from_dropdown(self._change_company_data_country_index, self._change_company_data_country_field)
        self.click(self._change_company_data_account_type_company_radio)
        self.clear_field_and_send_keys(self._change_company_data_nip_value, self._change_company_data_nip_field)
        self.click(self._change_company_data_save_button)
        self.clear_field_and_send_keys(self._change_company_data_company_name_value, self._change_company_data_company_name_field)
        self.clear_field_and_send_keys(self._change_company_data_street_value, self._change_company_data_street_field)
        self.clear_field_and_send_keys(self._change_company_data_zip_value, self._change_company_data_zip_field)
        self.clear_field_and_send_keys(self._change_company_data_city_value, self._change_company_data_city_field)
        self.select_index_from_dropdown(self._change_company_data_currency_index, self._change_company_data_currency_dropdown)
        self.click(self._change_company_data_save_stage_2_button)

    def edit_company_data_company_name_text(self):
        return self.get_text(self._change_company_data_company_name_result)

    def edit_company_data_nip_text(self):
        return self.get_text(self._change_company_data_nip_result)

    def open_add_bank_account_page(self):
        self.click(self._add_bank_account_menu)

    def add_bank_account(self, number):
        self.click(self._add_bank_account_button)
        self.clear_field_and_send_keys(self._add_bank_account_account_name_value, self._add_bank_account_account_name_field)
        self.clear_field_and_send_keys(number ,self._add_bank_account_account_number_field)
        self.clear_field_and_send_keys(self._add_bank_account_receiver_name_value, self._add_bank_account_receiver_name_field)
        self.click(self._add_bank_account_submit_button)

    def added_bank_account_number_text(self):
        return self.get_text(self._added_bank_account_number)

    def added_bank_account_name_text(self):
        return self.get_text(self._added_bank_account_name)

    def remove_all_bank_accounts(self):
        while True:
            if "/assets/img/table/delete.svg" in self.get_page_source():
                self.click(self._added_bank_account_remove_first_accouunt_button)
                self.click(self._add_other_user_remove_added_user_confirm_button)
                WebDriverWait(self.get_driver(), 15).until(EC.text_to_be_present_in_element(self._confirmation_result_text, u"Operacja wykonana poprawnie"))
                self.click(self._back_from_results_page_button)
            else:
                break

    def open_change_DNS_servers_page(self):
        self.click(self._change_DNS_servers_menu)

    def change_DNS_servers(self):
        self.select_index_from_dropdown(2, self._change_DNS_servers_dropdown)
        self.clear_field_and_send_keys(self._change_DNS_servers_DNS3_value, self._change_DNS_servers_DNS3_field)
        self.clear_field_and_send_keys(self._change_DNS_servers_DNS4_value, self._change_DNS_servers_DNS4_field)
        self.click(self._change_DNS_servers_submit_button)

    def change_DNS_servers_DNS1_text(self):
        return self.get_value(self._change_DNS_servers_DNS1_field)

    def change_DNS_servers_DNS2_text(self):
        return self.get_value(self._change_DNS_servers_DNS2_field)

    def change_DNS_servers_DNS3_text(self):
        return self.get_value(self._change_DNS_servers_DNS3_field)

    def change_DNS_servers_DNS4_text(self):
        return self.get_value(self._change_DNS_servers_DNS4_field)

    def change_DNS_servers_operation_successful_text(self):
        return self.get_text(self._change_DNS_servers_operation_successful)

    def open_new_DNS_template_page(self):
        self.click(self._new_DNS_profile_menu)

    def new_DNS_template(self):
        self.click(self._new_DNS_profile_button)
        self.clear_field_and_send_keys(self._new_DNS_profile_name_value, self._new_DNS_profile_name_field)
        self.click(self._new_DNS_profile_name_submit)

    def new_DNS_entry(self):
        # self.click(self._new_DNS_profile_name)
        # self.click(self._new_DNS_profile_manage_entries)
        # self.click(self._new_DNS_profile_add_new_DNS_entry_button)
        self.clear_field_and_send_keys(self._new_DNS_profile_host_value, self._new_DNS_profile_host_field)
        self.select_index_from_dropdown(0, self._new_DNS_profile_type_dropdown)
        self.clear_field_and_send_keys(self._new_DNS_profile_address_value, self._new_DNS_profile_address_field)
        self.click(self._new_DNS_profile_submit)

    def new_DNS_profile_successful_operation_text(self):
        return self.get_text(self._new_DNS_profile_successful_operation)

    def new_DNS_profile_successtul_opertation_profile_text(self):
        return self.get_text(self._new_DNS_profile_successtul_opertation_profile)

    def new_DNS_profile_successtul_opertation_host_text(self):
        return self.get_value(self._new_DNS_profile_host_field)

    def new_DNS_profile_successtul_opertation_address_text(self):
        return self.get_value(self._new_DNS_profile_address_field)

    def new_DNS_profile_name_text(self):
        return self.get_text(self._new_DNS_profile_name)

    def delete_all_profiles(self):
        while True:
            if "/assets/img/table/delete.svg" in self.get_page_source():
                self.click(self._new_DNS_profile_delete_first_profile)
                self.click(self._new_DNS_profile_delete_first_profile_confirm)
                WebDriverWait(self.get_driver(), 15).until(EC.text_to_be_present_in_element(self._confirmation_result_text, u"Szablon DNS został usunięty"))
                self.click(self._back_from_results_page_button)
            else:
                break

    def open_notifications_about_ending_auctions_page(self):
        self.click(self._notifications_about_ending_auctions_menu)

    def change_notifications_about_ending_auctions(self):
        self.click(self._notifications_about_ending_auctions_email_15_min)
        self.click(self._notifications_about_ending_auctions_email_30_min)
        self.click(self._notifications_about_ending_auctions_email_1_hr)
        self.click(self._notifications_about_ending_auctions_email_2_hr)
        self.click(self._notifications_about_ending_auctions_email_3_hr)
        self.click(self._notifications_about_ending_auctions_email_6_hr)
        self.click(self._notifications_about_ending_auctions_email_12_hr)
        self.click(self._notifications_about_ending_auctions_email_24_hr)
        self.click(self._notifications_about_ending_auctions_sms_15_min)
        self.get_driver().execute_script("window.scrollTo(2700, 1000);")
        self.click(self._notifications_about_ending_auctions_sms_30_min)
        self.click(self._notifications_about_ending_auctions_sms_1_hr)
        self.click(self._notifications_about_ending_auctions_sms_2_hr)
        self.click(self._notifications_about_ending_auctions_sms_3_hr)
        self.click(self._notifications_about_ending_auctions_sms_6_hr)
        self.click(self._notifications_about_ending_auctions_sms_12_hr)
        self.click(self._notifications_about_ending_auctions_sms_24_hr)
        self.click(self._notifications_about_ending_auctions_submit_button)

    def open_domain_watching_settings_page(self):
        self.click(self._domain_watching_settings_menu)

    def change_domain_watching_settings(self):
        self.click(self._domain_watching_settings_domain_set_on_auction_checkbox)
        self.click(self._domain_watching_settings_domain_set_on_last_minute_auction_checkbox)
        self.click(self._domain_watching_settings_domain_set_on_sale_checkbox)
        self.click(self._domain_watching_settings_buy_now_is_set_checkbox)
        self.click(self._domain_watching_settings_buy_now_is_lowered_checkbox)
        self.click(self._domain_watching_settings_buy_now_is_increased_checkbox)
        self.click(self._domain_watching_settings_domain_removed_from_market_checkbox)
        self.click(self._domain_watching_settings_domain_available_to_buy_in_instalments_checkbox)
        self.click(self._domain_watching_settings_domain_available_to_lease_checkbox)
        self.click(self._domain_watching_settings_domain_available_to_catch_checkbox)
        self.click(self._domain_watching_settings_submit_button)

    def open_sellers_watching_settings_page(self):
        self.click(self._sellers_watching_settings_menu)

    def change_sellers_watching_settings(self):
        self.click(self._sellers_watching_settings_domain_set_on_auction_checkbox)
        self.click(self._sellers_watching_settings_domain_set_on_last_minute_auction_checkbox)
        self.click(self._sellers_watching_settings_domain_set_on_sale_checkbox)
        self.click(self._sellers_watching_settings_buy_now_is_set_checkbox)
        self.click(self._sellers_watching_settings_buy_now_is_lowered_checkbox)
        self.click(self._sellers_watching_settings_buy_now_is_increased_checkbox)
        self.click(self._sellers_watching_settings_domain_removed_from_market_checkbox)
        self.click(self._sellers_watching_settings_domain_available_to_buy_in_instalments_checkbox)
        self.click(self._sellers_watching_settings_domain_available_to_lease_checkbox)
        self.click(self._sellers_watching_settings_domain_available_to_catch_checkbox)
        self.click(self._sellers_watching_settings_submit_button)

    def open_change_seller_profile_page(self):
        self.click(self._change_seller_profile_menu)

    def change_seller_profile(self):
        self.clear_field_and_send_keys(self._change_seller_profile_description_value, self._change_seller_profile_description_field)
        self.click(self._change_seller_profile_submit_button)

    def change_seller_profile_description_text(self):
        return self.get_text(self._change_seller_profile_description_field_after_submit)

    def open_sending_notification_settings_page(self):
        self.click(self._sending_notification_settings_menu)

    def change_sending_notification_settings(self):
        self.click(self._sending_notification_settings_domain_set_on_auction_checkbox)
        self.click(self._sending_notification_settings_domain_set_on_last_minute_auction_checkbox)
        self.click(self._sending_notification_settings_domain_set_on_sale_checkbox)
        self.click(self._sending_notification_settings_buy_now_is_set_checkbox)
        self.click(self._sending_notification_settings_buy_now_is_lowered_checkbox)
        self.click(self._sending_notification_settings_buy_now_is_increased_checkbox)
        self.click(self._sending_notification_settings_domain_removed_from_market_checkbox)
        self.click(self._sending_notification_settings_domain_available_to_buy_in_instalments_checkbox)
        self.click(self._sending_notification_settings_domain_available_to_lease_checkbox)
        self.click(self._sending_notification_settings_domain_available_to_catch_checkbox)
        self.click(self._sending_notification_settings_submit_button)

    def open_sms_notification_settings_page(self):
        self.click(self._sms_notification_settings_menu)

    def open_first_number_notifications(self):
        self.click(self._sms_notification_settings_first_phone_number_field)
        self.click(self._sms_notification_settings_first_phone_number_notifications_button)

    def change_sms_notification_settings(self):
        self.click(self._sms_notification_settings_send_only_indicated)
        self.click(self._sms_notification_settings_auction_ends_soon)
        self.click(self._sms_notification_settings_your_offer_was_gazumped)
        self.click(self._sms_notification_settings_you_won_an_auction)
        self.click(self._sms_notification_settings_successful_domain_catching)
        self.click(self._sms_notification_settings_catched_domain_auction_has_started)
        self.click(self._sms_notification_settings_payment_date_is_comming)
        self.click(self._sms_notification_settings_payment_date_is_exceeded)
        self.click(self._sms_notification_settings_submit)
