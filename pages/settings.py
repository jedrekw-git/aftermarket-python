# coding=utf-8
from selenium.webdriver.common.by import By
from pages.base import BasePage
from utils.utils import *
from random import randint


class SettingsPage(BasePage):
    _title = "Settings"

    _change_contact_data_button = (By.XPATH, "//div[6]/div/div/div/div[2]/span/a")
    _change_contact_data_name_field = (By.NAME, "name")
    _change_contact_data_name_value = get_random_string(7)+ " " +get_random_string(10)
    _change_contact_data_address_field = (By.NAME, "address")
    _change_contact_data_address_value = get_random_address()
    _change_contact_data_postalcode_field = (By.NAME, "zip")
    _change_contact_data_postalcode_value = get_random_zip()
    _change_contact_data_city_field = (By.NAME, "city")
    _change_contact_data_city_value = get_random_string(7)
    _change_contact_data_country_field = (By.NAME, "country")
    _change_contact_data_country_index = get_random_integer(2)
    _change_contact_data_save_button = (By.XPATH, "//button")
    _change_notification_settings_button = (By.XPATH, "//div[2]/div[2]/span/a")
    _change_notification_settings_send_only_indicated_button = (By.XPATH, "/html/body/div[6]/div/div/form/div[2]/div[3]/div[1]/label[2]")
    _change_notification_settings_about_account_condition_checkbox = (By.XPATH, "/html/body/div[6]/div/div/form/div[3]/div[3]/div[1]/div/div[9]/div[2]/label/b")
    _change_notification_settings_about_domain_condition_change_checkbox = (By.XPATH, "/html/body/div[6]/div/div/form/div[3]/div[3]/div[1]/div/div[17]/div[2]/label/b")
    _change_notification_settings_about_option_condition_change_checkbox = (By.XPATH, "/html/body/div[6]/div/div/form/div[3]/div[3]/div[1]/div/div[33]/div[2]/label/b")
    _change_notification_settings_about_made_operations_checkbox = (By.XPATH, "/html/body/div[6]/div/div/form/div[3]/div[3]/div[1]/div/div[59]/div[2]/label/b")
    _change_notification_settings_save_button = (By.XPATH, "//button[2]")
    _change_newsletter_settings_button = (By.XPATH, "//div[2]/div[2]/span[2]/a")
    _change_newsletter_settings_overall_checkbox = (By.XPATH, "/html/body/div[6]/div/div/form/div[2]/div[3]/div[1]/div/div[1]/div[2]/label/b")
    _change_newsletter_settings_according_to_domain_market_checkbox = (By.XPATH, "/html/body/div[6]/div/div/form/div[2]/div[3]/div[1]/div/div[11]/div[2]/label/b")
    _change_newsletter_settings_according_to_catching_domains_checkbox = (By.XPATH, "/html/body/div[6]/div/div/form/div[2]/div[3]/div[1]/div/div[23]/div[2]/label/b")
    _add_email_address_menu = (By.XPATH, "//div[2]/div[2]/span[3]/a")
    _add_email_address_button = (By.XPATH, "//button")
    _add_email_address_field = (By.NAME, "email")
    _add_email_address_value = "z"+get_random_string(7)+"@ijasdnjiasnd.pl"
    _added_email_field = (By.XPATH, "/html/body/div[6]/div/div/form/div[2]/table/tbody/tr[6]/td[2]/span")
    _added_email_status_field = (By.XPATH, "/html/body/div[6]/div/div/form/div[2]/table/tbody/tr[6]/td[4]/span")
    _add_email_address_remove_added_email = (By.XPATH, "//td[5]/span/img")
    _add_email_address_remove_added_email_confirm = (By.XPATH, "//button[2]")
    _add_other_users_menu = (By.XPATH, "//div[4]/div[2]/span[3]/a")
    _add_other_user_button = (By.XPATH, "//button")
    _add_other_user_login_field = (By.NAME, "login")
    _add_other_user_login_value = "z"+get_random_string(9)
    _add_other_user_password_field = (By.NAME, "password")
    _add_other_user_password_value = get_random_string(9)
    _add_other_user_repeat_password_field = (By.NAME, "password2")
    _add_other_user_description_field = (By.NAME, "description")
    _add_other_user_description_value = get_random_string(7)+ " " +get_random_string(10)+ " " +get_random_string(11)
    _add_other_user_can_do_only_few_operations_radio = (By.XPATH, "/html/body/div[6]/div/div/form/div[2]/div[3]/div[1]/label[2]/span[2]")
    _add_other_user_management_of_account_balance_checkbox = (By.XPATH, "/html/body/div[6]/div/div/form/div[3]/div[3]/div[1]/div/div[1]/div[2]/label/b")
    _add_other_user_management_of_domains_to_pay_checkbox = (By.XPATH, "/html/body/div[6]/div/div/form/div[3]/div[3]/div[1]/div/div[9]/div[2]/label/b")
    _add_other_user_management_of_invoices_checkbox = (By.XPATH, "/html/body/div[6]/div/div/form/div[3]/div[3]/div[1]/div/div[19]/div[2]/label/b")
    _add_other_user_management_of_withdrawals_checkbox = (By.XPATH, "/html/body/div[6]/div/div/form/div[3]/div[3]/div[1]/div/div[25]/div[2]/label/b")
    _add_other_user_management_of_bank_accounts_checkbox = (By.XPATH, "/html/body/div[6]/div/div/form/div[3]/div[3]/div[1]/div/div[33]/div[2]/label/b")
    _add_other_user_management_of_domains_checkbox = (By.XPATH, "/html/body/div[6]/div/div/form/div[3]/div[3]/div[1]/div/div[43]/div[2]/label/b")
    _add_other_user_management_of_domain_transfers_to_account_checkbox = (By.XPATH, "/html/body/div[6]/div/div/form/div[3]/div[3]/div[1]/div/div[75]/div[2]/label/b")
    _add_other_user_management_of_domain_transfers_from_account_checkbox = (By.XPATH, "/html/body/div[6]/div/div/form/div[3]/div[3]/div[1]/div/div[83]/div[2]/label/b")
    _add_other_user_management_of_profiles_for_domain_registration_checkbox = (By.XPATH, "/html/body/div[6]/div/div/form/div[3]/div[3]/div[1]/div/div[91]/div[2]/label/b")
    _add_other_user_management_of_domain_parking_checkbox = (By.XPATH, "/html/body/div[6]/div/div/form/div[3]/div[3]/div[1]/div/div[101]/div[2]/label/b")
    _add_other_user_management_of_DNS_entries_checkbox = (By.XPATH, "/html/body/div[6]/div/div/form/div[3]/div[3]/div[1]/div/div[111]/div[2]/label/b")
    _add_other_user_management_of_options_checkbox = (By.XPATH, "/html/body/div[6]/div/div/form/div[3]/div[3]/div[1]/div/div[121]/div[2]/label/b")
    _add_other_user_management_of_option_transfers_to_account_checkbox = (By.XPATH, "/html/body/div[6]/div/div/form/div[3]/div[3]/div[1]/div/div[135]/div[2]/label/b")
    _add_other_user_management_of_option_transfers_from_account_checkbox = (By.XPATH, "/html/body/div[6]/div/div/form/div[3]/div[3]/div[1]/div/div[143]/div[2]/label/b")
    _add_other_user_change_account_settings_checkbox = (By.XPATH, "/html/body/div[6]/div/div/form/div[3]/div[3]/div[1]/div/div[151]/div[2]/label/b")
    _add_other_user_management_of_email_addresses_checkbox = (By.XPATH, "/html/body/div[6]/div/div/form/div[3]/div[3]/div[1]/div/div[165]/div[2]/label/b")
    _add_other_user_management_of_mobile_phones_checkbox = (By.XPATH, "/html/body/div[6]/div/div/form/div[3]/div[3]/div[1]/div/div[177]/div[2]/label/b")
    _add_other_user_management_of_logins_checkbox = (By.XPATH, "/html/body/div[6]/div/div/form/div[3]/div[3]/div[1]/div/div[187]/div[2]/label/b")
    _add_other_user_management_of_data_exports_checkbox = (By.XPATH, "/html/body/div[6]/div/div/form/div[3]/div[3]/div[1]/div/div[201]/div[2]/label/b")
    _add_other_user_save_button = (By.XPATH, "//button[2]")
    _add_other_user_added_login_field = (By.XPATH, "/html/body/div[6]/div/div/form/div[2]/table/tbody/tr[6]/td[2]/span")
    _add_other_user_added_description_field = (By.XPATH, "/html/body/div[6]/div/div/form/div[2]/table/tbody/tr[6]/td[5]/span")
    _add_other_user_remove_added_user_button = (By.XPATH, "//td[6]/span/img")
    _add_other_user_remove_added_user_confirm_button = (By.XPATH, "//button[2]")
    _change_company_data_menu = (By.XPATH, "//div[5]/div[2]/span/a")
    _change_company_data_street_field = (By.NAME, "address")
    _change_company_data_street_value = get_random_address()
    _change_company_data_zip_field = (By.NAME, "zip")
    _change_company_data_zip_value = get_random_zip()
    _change_company_data_city_field = (By.NAME, "city")
    _change_company_data_city_value = get_random_string(8)
    _change_company_data_save_button = (By.XPATH, "//button")
    _change_company_data_operation_succcessful = (By.XPATH, "/html/body/div[6]/div/div/form/div[1]")
    _change_company_data_change_invoicing_method = (By.XPATH, "//div[3]/span/a")
    _change_company_data_country_field = (By.NAME, "country")
    _change_company_data_country_index = get_random_integer(2)
    _change_company_data_account_type_company_radio = (By.XPATH, "/html/body/div[6]/div/div/form/div[2]/div[3]/div[1]/label[2]")
    _change_company_data_nip_field = (By.XPATH, "//div/input")
    _change_company_data_nip_value = "PL1234567"+get_random_integer(3)
    _change_company_data_nip_result = (By.XPATH, "/html/body/div[6]/div/div/form/div[6]/div[3]/div[1]/span")
    _change_company_data_company_name_field = (By.NAME, "name")
    _change_company_data_company_name_value = get_random_string(10)
    _change_company_data_company_name_result = (By.XPATH, "/html/body/div[6]/div/div/form/div[1]/div[3]/div[1]/span")
    _change_company_data_currency_index = randint(1, 4)
    _change_company_data_currency_dropdown = (By.NAME, "currency")

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

    def open_change_notification_settings_page(self):
        self.click(self._change_notification_settings_button)

    def change_notification_settings(self):
        self.click(self._change_notification_settings_send_only_indicated_button)
        self.click(self._change_notification_settings_about_account_condition_checkbox)
        self.click(self._change_notification_settings_about_domain_condition_change_checkbox)
        self.click(self._change_notification_settings_about_option_condition_change_checkbox)
        self.click(self._change_notification_settings_about_made_operations_checkbox)

    def save_change_notification_settings(self):
        self.click(self._change_notification_settings_save_button)

    def open_change_newsletter_settings_page(self):
        self.click(self._change_newsletter_settings_button)

    def change_newsletter_settings(self):
        self.click(self._change_newsletter_settings_overall_checkbox)
        self.click(self._change_newsletter_settings_according_to_domain_market_checkbox)
        self.click(self._change_newsletter_settings_according_to_catching_domains_checkbox)

    def open_add_email_address_page(self):
        self.click(self._add_email_address_menu)

    def add_email_address(self):
        self.click(self._add_email_address_button)
        self.clear_field_and_send_keys(self._add_email_address_value, self._add_email_address_field)
        self.click(self._change_notification_settings_save_button)
        self.click(self._add_email_address_button)

    def added_email_address_text(self):
        return self.get_text(self._added_email_field)

    def added_email_status_text(self):
        return self.get_text(self._added_email_status_field)

    def remove_added_email_address(self):
        self.click(self._add_email_address_remove_added_email)
        self.click(self._add_email_address_remove_added_email_confirm)

    def open_add_other_users_page(self):
        self.click(self._add_other_users_menu)

    def add_other_user(self):
        self.click(self._add_other_user_button)
        self.clear_field_and_send_keys(self._add_other_user_login_value, self._add_other_user_login_field)
        self.clear_field_and_send_keys(self._add_other_user_password_value, self._add_other_user_password_field)
        self.clear_field_and_send_keys(self._add_other_user_password_value, self._add_other_user_repeat_password_field)
        self.clear_field_and_send_keys(self._add_other_user_description_value, self._add_other_user_description_field)
        self.click(self._add_other_user_button)
        self.click(self._add_other_user_can_do_only_few_operations_radio)
        self.click(self._add_other_user_management_of_account_balance_checkbox)
        self.click(self._add_other_user_management_of_domains_to_pay_checkbox)
        self.click(self._add_other_user_management_of_invoices_checkbox)
        self.click(self._add_other_user_management_of_withdrawals_checkbox)
        self.click(self._add_other_user_management_of_bank_accounts_checkbox)
        self.click(self._add_other_user_management_of_domains_checkbox)
        self.click(self._add_other_user_management_of_domain_transfers_from_account_checkbox)
        self.click(self._add_other_user_management_of_domain_transfers_to_account_checkbox)
        self.click(self._add_other_user_management_of_profiles_for_domain_registration_checkbox)
        self.click(self._add_other_user_management_of_domain_parking_checkbox)
        self.click(self._add_other_user_management_of_DNS_entries_checkbox)
        self.click(self._add_other_user_management_of_options_checkbox)
        self.click(self._add_other_user_management_of_option_transfers_from_account_checkbox)
        self.click(self._add_other_user_management_of_option_transfers_to_account_checkbox)
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

    def remove_added_user(self):
        self.click(self._add_other_user_remove_added_user_button)
        self.click(self._add_other_user_remove_added_user_confirm_button)

    def open_change_company_data_page(self):
        self.click(self._change_company_data_menu)

    def edit_company_address(self):
        self.clear_field_and_send_keys(self._change_company_data_street_value, self._change_company_data_street_field)
        self.clear_field_and_send_keys(self._change_company_data_zip_value, self._change_company_data_zip_field)
        self.clear_field_and_send_keys(self._change_company_data_city_value, self._change_company_data_city_field)
        self.click(self._change_company_data_save_button)

    def edit_company_data_operation_successful_text(self):
        return self.get_text(self._change_company_data_operation_succcessful)

    def edit_company_data_zip_text(self):
        return self.get_value(self._change_company_data_zip_field)

    def edit_company_data_street_text(self):
        return self.get_value(self._change_company_data_street_field)

    def edit_company_data_city_text(self):
        return self.get_value(self._change_company_data_city_field)

    def edit_company_data(self):
        self.click(self._change_company_data_change_invoicing_method)
        self.select_index_from_dropdown(self._change_company_data_country_index, self._change_company_data_country_field)
        self.click(self._change_company_data_account_type_company_radio)
        self.clear_field_and_send_keys(self._change_company_data_nip_value, self._change_company_data_nip_field)
        self.click(self._change_company_data_save_button)
        self.clear_field_and_send_keys(self._change_company_data_company_name_value, self._change_company_data_company_name_field)
        self.clear_field_and_send_keys(self._change_company_data_street_value, self._change_company_data_street_field)
        self.clear_field_and_send_keys(self._change_company_data_zip_value, self._change_company_data_zip_field)
        self.clear_field_and_send_keys(self._change_company_data_city_value, self._change_company_data_city_field)
        self.select_index_from_dropdown(self._change_company_data_currency_index, self._change_company_data_currency_dropdown)
        self.click(self._change_company_data_save_button)

    def edit_company_data_company_name_text(self):
        return self.get_text(self._change_company_data_company_name_result)

    def edit_company_data_nip_text(self):
        return self.get_text(self._change_company_data_nip_result)