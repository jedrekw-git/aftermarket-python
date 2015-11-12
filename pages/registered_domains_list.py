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

class RegisteredDomainsListPage(BasePage):
    _title = "Registered domains"

    _first_domain_checkbox = (By.XPATH, "//td[3]/span/label/span")
    _renew_button = (By.XPATH, "//div[7]/div/button")
    _renew_automatically_button = (By.XPATH, "//div[7]/div/div/div/div[2]")
    _renew_automatically_when_money_on_account_radio = (By.XPATH, "//div[3]/div/label")
    _renew_automatically_send_email_after_operation_radio = (By.XPATH, "/html/body/div[7]/div/div/form/div[4]/div[3]/div/label[1]/span[2]")
    _renew_manually_button = (By.XPATH, "//div[7]/div/div/div/div")
    _second_stage_domain_name_field = (By.XPATH, "/html/body/div[7]/div/div/form/div[1]/table/tbody/tr[1]/td[2]/label/span")
    _second_stage_text_field = (By.XPATH, "/html/body/div[7]/div/div/form/div[1]/table/tbody/tr[1]/td[3]/label/span")
    _second_stage_send_email_after_oparation_radio = (By.XPATH, "/html/body/div[7]/div/div/form/div[2]/div[3]/div/label[1]/span[2]")
    _second_stage_realize_immediately_radio = (By.XPATH, "/html/body/div[7]/div/div/form/div[3]/div[3]/div/label[1]/span[2]")
    _result_domain_name_field = (By.XPATH, "/html/body/div[7]/div/div/form/div[2]/table/tbody/tr[1]/td[2]/span")
    _result_text_field = (By.XPATH, "/html/body/div[7]/div/div/form/div[2]/table/tbody/tr[1]/td[3]")
    _move_button = (By.XPATH, "//div[7]/div/button[2]")
    _change_profile_data_button = (By.XPATH, "//div[7]/div/div/div[2]/div")
    _change_profile_data_dont_send_results_radio = (By.XPATH, "/html/body/div[7]/div/div/form/div[3]/div[3]/div/label[2]/span[2]")
    _submit_button = (By.XPATH, "//button[2]")
    _privacy_settings_button = (By.XPATH, "//div[7]/div/div/div[2]/div[2]")
    _privacy_settings_show_user_data_in_whois = (By.XPATH, "/html/body/div[7]/div/div/form/div[2]/div[3]/div[1]/label[1]")
    _get_authinfo_button = (By.XPATH, "//div[7]/div/div/div[2]/div[3]")
    _get_authinfo_dont_send_results_radio = (By.XPATH, "/html/body/div[7]/div/div/form/div[2]/div[3]/div/label[2]/span[2]")
    _redirect_button = (By.XPATH, "//div[7]/div/button[3]")
    _change_dns_servers_button = (By.XPATH, "//div/div/div[3]/div")
    _change_dns_servers_dropdown = (By.XPATH, "//select")
    _change_dns_servers_dropdown_index = randint(1, 5)
    _change_dns_servers_dont_send_email_after_operation_radio = (By.XPATH, "/html/body/div[7]/div/div/form/div[7]/div[3]/div/label[2]/span[2]")
    _change_redirection_button = (By.XPATH, "//div/div/div[3]/div[2]")
    _change_redirection_dropdown = (By.XPATH, "//select")
    _change_redirection_url_field = (By.NAME, "url")
    _change_redirection_url_value = "http://www."+get_random_string(10)+".com"
    _change_redirection_ip_value = "192."+get_random_integer(2)+"."+get_random_integer(1)+"."+get_random_integer(1)
    _change_redirection_dont_sent_results_after_operation_radio = (By.XPATH, "/html/body/div[7]/div/div/form/div[4]/div[3]/div/label[2]/span[2]")
    _change_dns_profile_button = (By.XPATH, "//div/div/div[3]/div[3]")
    _change_dns_profile_dropdown = (By.XPATH, "//select")
    _change_dns_profile_dont_sent_results_after_operation_radio = (By.XPATH, "/html/body/div[7]/div/div/form/div[3]/div[3]/div/label[2]/span[2]")
    _redirect_button_for_selected_domain = (By.XPATH, "//button[3]")
    _set_dns_entries_button = (By.XPATH, "//div[2]/div[3]/div[3]")
    _add_dns_entry_button = (By.XPATH, "//button")
    _add_dns_entry_host_name_field = (By.XPATH, "//div[2]/div[3]/div/input")
    _add_dns_entry_host_name_value = get_random_string(8)
    _add_dns_entry_type_dropdown = (By.XPATH, "//select")
    _add_dns_entry_priority_field = (By.XPATH, "//div[4]/div[3]/div/input")
    _add_dns_entry_priority_value = get_random_integer(2)
    _add_dns_entry_address_field = (By.XPATH, "//div[5]/div[3]/div/input")
    _add_dns_entry_address_value = "www."+get_random_string(10)+".com"
    _add_dns_entry_host_name_result = (By.XPATH, "/html/body/div[7]/div/div/form[1]/div[2]/table/tbody/tr[5]/td[2]/span/label")
    _delete_first_dns_priofile_button = (By.XPATH, "//button[2]")
    _new_dns_server_in_domain_button = (By.XPATH, "//div[3]/div[5]")
    _new_dns_server_in_domain_add_server_button = (By.XPATH, "//button")
    _new_dns_server_in_domain_name_field = (By.XPATH, "//div/input")
    _new_dns_server_in_domain_name_value = get_random_string(6)
    _new_dns_server_in_domain_ip_field = (By.XPATH, "//div[2]/div[3]/div/input")
    _new_dns_server_in_domain_ip_value = "192."+get_random_integer(2)+"."+get_random_integer(1)+"."+get_random_integer(1)
    _new_dns_server_in_domain_name_result = (By.XPATH, "/html/body/div[7]/div/div/form[1]/div[2]/table/tbody/tr[3]/td[2]/span/label")
    _delete_first_dns_server = (By.XPATH, "//button[2]")
    _parking_button_first_domain = (By.XPATH, "//button[4]")
    _change_parking_service_button_first_domain = (By.XPATH, "//td/div[2]/div[4]/div")
    _change_parking_service_redirect_domains_to_dns_server_checkbox = (By.XPATH, "/html/body/div[7]/div/div/form/div[3]/div[3]/div[1]/label/span[2]")
    _change_parking_service_send_email_after_oparation_radio = (By.XPATH, "/html/body/div[7]/div/div/form/div[4]/div[3]/div/label[1]/span[2]")
    _change_keyword_button_first_domain = (By.XPATH, "//td/div[2]/div[4]/div[2]")
    _change_keyword_field = (By.XPATH, "//div[3]/div/input")
    _change_keyword_value = get_random_string(10)
    _change_keyword_send_email_after_operation = (By.XPATH, "/html/body/div[7]/div/div/form/div[3]/div[3]/div/label[1]/span[2]")


    def __init__(self, driver):
        super(RegisteredDomainsListPage, self).__init__(driver, self._title)

    def renew_domain_automatically(self):
        self.click(self._renew_button)
        self.click(self._renew_automatically_button)
        self.click(self._renew_automatically_when_money_on_account_radio)
        self.click(self._renew_automatically_send_email_after_operation_radio)
        self.click(self._submit_button)

    def result_domain_text(self):
        return self.get_text(self._result_domain_name_field)

    def first_domain_text(self):
        self._first_domain_text_value = self.get_text(self._first_domain_checkbox)

    def renew_domain_manually(self):
        self.click(self._renew_button)
        self.click(self._renew_manually_button)

    def second_stage_domain_text(self):
        return self.get_text(self._second_stage_domain_name_field)

    def second_stage_checkboxes_and_submit(self):
        self.click(self._second_stage_send_email_after_oparation_radio)
        self.click(self._second_stage_realize_immediately_radio)
        self.click(self._submit_button)
        self.accept_alert()

    def select_first_domain(self):
        self.click(self._first_domain_checkbox)

    def change_profile_data(self):
        self.click(self._move_button)
        self.click(self._change_profile_data_button)
        self.click(self._change_profile_data_dont_send_results_radio)
        self.click(self._submit_button)

    def result_text(self):
        return self.get_text(self._result_text_field)

    def privacy_settings_first_stage(self):
        self.click(self._move_button)
        self.click(self._privacy_settings_button)
        self.click(self._privacy_settings_show_user_data_in_whois)
        self.click(self._submit_button)

    def get_authinfo(self):
        self.click(self._move_button)
        self.click(self._get_authinfo_button)
        self.click(self._get_authinfo_dont_send_results_radio)
        self.click(self._submit_button)

    def change_dns_servers_for_selected_domain(self):
        self.click(self._redirect_button)
        self.click(self._change_dns_servers_button)
        self.select_index_from_dropdown(self._change_dns_servers_dropdown_index, self._change_dns_servers_dropdown)
        self.click(self._change_dns_servers_dont_send_email_after_operation_radio)
        self.click(self._submit_button)

    def change_redirection_direct(self):
        self.click(self._redirect_button)
        self.click(self._change_redirection_button)
        self.select_index_from_dropdown(1, self._change_redirection_dropdown)
        self.clear_field_and_send_keys(self._change_redirection_url_value, self._change_redirection_url_field)
        self.click(self._change_redirection_dont_sent_results_after_operation_radio)
        self.click(self._submit_button)

    def change_redirection_hidden(self):
        self.click(self._redirect_button)
        self.click(self._change_redirection_button)
        self.select_index_from_dropdown(2, self._change_redirection_dropdown)
        self.clear_field_and_send_keys(self._change_redirection_url_value, self._change_redirection_url_field)
        self.click(self._change_redirection_dont_sent_results_after_operation_radio)
        self.click(self._submit_button)

    def change_redirection_ip(self):
        self.click(self._redirect_button)
        self.click(self._change_redirection_button)
        self.select_index_from_dropdown(3, self._change_redirection_dropdown)
        self.clear_field_and_send_keys(self._change_redirection_ip_value, self._change_redirection_url_field)
        self.click(self._change_redirection_dont_sent_results_after_operation_radio)
        self.click(self._submit_button)

    def change_dns_profile(self):
        self.click(self._redirect_button)
        self.click(self._change_dns_profile_button)
        self.select_index_from_dropdown(1, self._change_dns_profile_dropdown)
        self.click(self._change_dns_profile_dont_sent_results_after_operation_radio)
        self.click(self._submit_button)

    def new_dns_entry_for_senected_domain(self):
        self.click(self._redirect_button_for_selected_domain)
        self.click(self._set_dns_entries_button)

    def new_dns_entry_for_senected_domain_details(self):
        self.click(self._add_dns_entry_button)
        self.clear_field_and_send_keys(self._add_dns_entry_host_name_value, self._add_dns_entry_host_name_field)
        self.select_index_from_dropdown(1, self._add_dns_entry_type_dropdown)
        self.clear_field_and_send_keys(self._add_dns_entry_priority_value, self._add_dns_entry_priority_field)
        self.clear_field_and_send_keys(self._add_dns_entry_address_value, self._add_dns_entry_address_field)
        self.click(self._submit_button)

    def delete_new_dns_entry_for_senected_domain(self):
        self.click(self._add_dns_entry_host_name_result)
        self.click(self._delete_first_dns_priofile_button)
        self.click(self._delete_first_dns_priofile_button)

    def new_dns_server_in_domain(self):
        self.click(self._redirect_button_for_selected_domain)
        self.click(self._new_dns_server_in_domain_button)

    def new_dns_server_in_domain_details(self):
        self.click(self._new_dns_server_in_domain_add_server_button)
        self.clear_field_and_send_keys(self._new_dns_server_in_domain_name_value, self._new_dns_server_in_domain_name_field)
        self.clear_field_and_send_keys(self._new_dns_server_in_domain_ip_value, self._new_dns_server_in_domain_ip_field)
        self.click(self._submit_button)

    def delete_new_dns_server_in_domain(self):
        self.click(self._new_dns_server_in_domain_name_result)
        self.click(self._delete_first_dns_server)
        self.click(self._delete_first_dns_server)

    def change_parking_service(self):
        self.click(self._parking_button_first_domain)
        self.click(self._change_parking_service_button_first_domain)
        self.click(self._change_parking_service_redirect_domains_to_dns_server_checkbox)
        self.click(self._change_parking_service_send_email_after_oparation_radio)
        self.click(self._submit_button)

    def change_keyword(self):
        self.click(self._parking_button_first_domain)
        self.click(self._change_keyword_button_first_domain)
        self.clear_field_and_send_keys(self._change_keyword_value, self._change_keyword_field)
        self.click(self._change_keyword_send_email_after_operation)
        self.click(self._submit_button)