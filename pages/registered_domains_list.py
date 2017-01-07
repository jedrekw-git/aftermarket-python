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
from pages.page import *


def _element_is_visible(element):
    return True if element.is_displayed() else False


class RegisteredDomainsListPage(BasePage):
    _title = "Registered domains"

    _first_domain_checkbox = (
        By.XPATH, "//td[4]/div/label/span")
    _third_domain_checkbox = (
        By.XPATH, "//tbody[3]/tr/td[4]/div/label/span")
    _second_domain_checkbox = (By.XPATH, "//tbody[2]/tr/td[4]/div/label/span")
    _fourth_domain_checkbox = (By.XPATH, "//tbody[4]/tr/td[4]/div/label/span")
    _fifth_domain_checkbox = (By.XPATH, "//tbody[5]/tr/td[4]/div/label/span")
    _renew_button = (By.XPATH, "//div[2]/div[2]/span/a")
    _renew_automatically_button = (By.XPATH, "//div[2]/div[2]/span/div/a[3]")
    _renew_automatically_when_money_on_account_radio = (By.XPATH, "//div[2]/div/label")
    _renew_automatically_send_email_after_operation_radio = (
        By.XPATH, "//div[4]/div/div[2]/div/label/span[2]")
    _renew_automatically_start_from_dropdown = (By.NAME, "days")
    _renew_automatically_start_from_option = (By.XPATH, "//option[%s]" %randint(1,10))
    _renew_manually_button = (By.XPATH, "//div[2]/div[2]/span/div/a[2]")
    _second_stage_domain_name_field = (
        By.XPATH, "//td[2]/div/label/span")
    _second_stage_text_field = (By.XPATH, "//label/div")
    _second_stage_send_email_after_oparation_radio = (By.XPATH, "//label/span[2]")
    _second_stage_stop_realization_until_manual_activation_radio = (By.XPATH, "//div[5]/div/div[2]/div/label[2]/span[2]")
    _second_stage_stop_realization_until_manual_activation_radio2 = (By.XPATH, "//div[4]/div/div[2]/div/label[2]/span[2]")
    _second_stage_submit_button = (By.XPATH, "//div[6]/div/div[2]/div[2]/button")
    _second_stage_submit_confirm_button = (By.XPATH, "//div[3]/button")
    _result_domain_name_field = (By.XPATH, "//div/span")
    _result_text_field = (By.XPATH, "//td[3]")
    _add_escrow_transaction_result_text_field = (By.XPATH, "//p")
    _move_button = (By.XPATH, "//div[2]/div[2]/span[2]/a")
    _move_to_other_account_button = (By.XPATH, "//div[7]/div/div/div[2]/div[4]")
    _move_to_other_account_login_field = (By.NAME, "login")
    _change_profile_data_button = (By.XPATH, "//div[2]/span[2]/div/a[2]")
    _change_profile_data_profile_dropdown = (By.NAME, "id")
    _change_profile_data_profile_dropdown_option = (By.XPATH, "//option[%s]"%randint(1,8))
    _change_profile_data_dont_send_results_radio = (
        By.XPATH, "//label[2]/span[2]")
    _change_profile_data_second_stage_submit_button = (By.XPATH, "//button[@type='submit']")
    _submit_button = (By.XPATH, "//div[2]/button")
    _privacy_settings_button = (By.XPATH, "//div[7]/div/div/div[2]/div[2]")
    _privacy_settings_show_user_data_in_whois = (
        By.XPATH, "/html/body/div[7]/div/div/form/div[2]/div[3]/div[1]/label[1]")
    _get_authinfo_button = (By.XPATH, "//div[7]/div/div/div[2]/div[3]")
    _get_authinfo_dont_send_results_radio = (
        By.XPATH, "/html/body/div[7]/div/div/form/div[2]/div[3]/div/label[2]/span[2]")
    _redirect_button = (By.XPATH, "//div[7]/div/button[3]")
    _change_dns_servers_button = (By.XPATH, "//div[7]/div/div/div[3]/div")
    _change_dns_servers_dropdown = (By.XPATH, "//select")
    _change_dns_servers_dropdown_index = randint(1, 5)
    _change_dns_servers_dont_send_email_after_operation_radio = (
        By.XPATH, "/html/body/div[7]/div/div/form/div[7]/div[3]/div/label[2]/span[2]")
    _change_redirection_button = (By.XPATH, "//div[7]/div/div/div[3]/div[2]")
    _change_redirection_dropdown = (By.XPATH, "//select")
    _change_redirection_url_field = (By.NAME, "url")
    _change_redirection_url_value = "http://www." + get_random_string(10) + ".com"
    _change_redirection_ip_value = "192." + get_random_integer(2) + "." + get_random_integer(
        1) + "." + get_random_integer(1)
    _change_redirection_dont_sent_results_after_operation_radio = (
        By.XPATH, "/html/body/div[7]/div/div/form/div[4]/div[3]/div/label[2]/span[2]")
    _change_dns_profile_button = (By.XPATH, "//div/div/div[3]/div[3]")
    _change_dns_profile_dropdown = (By.XPATH, "//select")
    _change_dns_profile_dont_sent_results_after_operation_radio = (
        By.XPATH, "/html/body/div[7]/div/div/form/div[3]/div[3]/div/label[2]/span[2]")
    _redirect_button_for_selected_domain = (By.XPATH, "//button[3]")
    _set_dns_entries_button = (By.XPATH, "//div[2]/div[3]/div[3]")
    _add_dns_entry_button = (By.XPATH, "//button")
    _add_dns_entry_host_name_field = (By.XPATH, "//div[2]/div[3]/div/input")
    _add_dns_entry_host_name_value = get_random_string(8)
    _add_dns_entry_type_dropdown = (By.XPATH, "//select")
    _add_dns_entry_priority_field = (By.XPATH, "//div[4]/div[3]/div/input")
    _add_dns_entry_priority_value = get_random_integer(2)
    _add_dns_entry_address_field = (By.XPATH, "//div[5]/div[3]/div/input")
    _add_dns_entry_address_value = "www." + get_random_string(10) + ".com"
    _add_dns_entry_host_name_result = (By.XPATH, "//label")
    _delete_first_dns_priofile_button = (By.XPATH, "//button[2]")
    _dns_servers_in_domain_button = (By.XPATH, "//div[2]/div[3]/div[5]")
    _new_dns_server_in_domain_add_server_button = (By.XPATH, "//button")
    _new_dns_server_in_domain_name_field = (By.XPATH, "//div/input")
    _new_dns_server_in_domain_name_value = get_random_string(6)
    _new_dns_server_in_domain_ip_field = (By.XPATH, "//div[2]/div[3]/div/input")
    _new_dns_server_in_domain_ip_value = "192." + get_random_integer(2) + "." + get_random_integer(1) + "." + get_random_integer(1)
    _new_dns_server_in_domain_name_result = (By.XPATH, "//label")
    _delete_first_dns_server = (By.XPATH, "//button[2]")
    _parking_button_first_domain = (By.XPATH, "//button[4]")
    _change_parking_service_button_first_domain = (By.XPATH, "//td/div[2]/div[4]/div")
    _change_parking_service_redirect_domains_to_dns_server_checkbox = (
        By.XPATH, "/html/body/div[7]/div/div/form/div[3]/div[3]/div[1]/label/span[2]")
    _change_parking_service_send_email_after_oparation_radio = (
        By.XPATH, "/html/body/div[7]/div/div/form/div[4]/div[3]/div/label[1]/span[2]")
    _change_keyword_button_first_domain = (By.XPATH, "//td/div[2]/div[4]/div[2]")
    _change_keyword_field = (By.XPATH, "//div[3]/div/input")
    _change_keyword_value = get_random_string(10)
    _change_keyword_send_email_after_operation = (
        By.XPATH, "/html/body/div[7]/div/div/form/div[3]/div[3]/div/label[1]/span[2]")
    _sell_first_domain_button = (By.XPATH, "//button[6]")
    _sell_button = (By.XPATH, "//div[7]/div/button[4]")
    _sell_on_auction_button = (By.XPATH, "//div[7]/div/div/div[4]/div[2]")
    _add_on_marketplace_button = (By.XPATH, "//div[7]/div/div/div[4]/div")
    _sell_on_escrow_auction_button = (By.XPATH, "//div/div/div[4]/div[3]")
    _sell_on_auction_first_domain_button = (By.XPATH, "//div[2]/div[6]/div[2]")
    _sell_on_auction_price_start_field = (By.NAME, "price_start")
    _sell_on_auction_price_start_value = randint(1, 20)
    _sell_on_auction_currency_dropdown = (By.NAME, "currency")
    _sell_on_auction_currency_value = randint(0, 3)
    _sell_on_auction_end_date_field = (By.NAME, "end_date")
    _sell_on_auction_end_date_index = randint(1, 29)
    _sell_on_auction_end_time_field = (By.NAME, "end_time")
    _sell_on_auction_end_time_index = randint(1, 22)
    _sell_on_auction_minimal_price_checkbox = (By.XPATH, "//div[5]/div[3]/div/label")
    _sell_on_auction_buy_now_price_checkbox = (By.XPATH, "/html/body/div[7]/div/div/form/div[5]/div[3]/div[2]/label")
    _sell_on_auction_auction_description_checkbox = (
        By.XPATH, "/html/body/div[7]/div/div/form/div[5]/div[3]/div[3]/label")
    _sell_on_auction_category_field = (By.XPATH, "//span[2]/input")
    _sell_on_auction_category_technology = (By.XPATH, "//span[2]/div/div[2]/div[4]")
    _sell_on_auction_category_technology_computers = (By.XPATH, "//span[2]/div/div[6]/div")
    _sell_on_auction_price_minimum_field = (By.NAME, "price_minimum")
    _sell_on_auction_price_minimum_value = randint(21, 40)
    _sell_on_auction_price_buynow_field = (By.NAME, "price_buynow")
    _sell_on_auction_price_buynow_value = randint(41, 60)
    _sell_on_auction_description_field = (By.XPATH, "//div[10]/div[3]/div/div/div")
    _sell_on_auction_description_value = get_random_string(10) + " " + get_random_string(7) + " " + get_random_string(8)
    _sell_on_auction_stage2_domain_name_field = (By.XPATH, "/html/body/div[7]/div/div/form/div[1]/div[3]/div[1]/span")
    _sell_on_auction_stage2_category_field = (By.XPATH, "/html/body/div[7]/div/div/form/div[4]/div[3]/div[1]/span")
    # _sell_on_auction_stage2_stop_until_manual_activation_radio = (By.XPATH, "")
    _sell_on_auction_stage2_realize_immediately_radio = (By.XPATH, "//label/span[2]")
    _sell_on_auction_stage2_dont_send_email_radio = (By.XPATH, "//div[9]/div[3]/div/label[2]/span[2]")
    _sell_on_escrow_auction_first_domain_button = (By.XPATH, "//div[6]/div[3]")
    _sell_on_escrow_auction_buyer_login_field = (By.NAME, "login")
    _sell_on_escrow_auction_price_field = (By.NAME, "amount")
    _sell_on_escrow_auction_days_to_pay_dropdown = (By.NAME, "days")
    _sell_on_escrow_auction_days_to_pay_index = randint(0, 7)
    _sell_on_escrow_auction_stage2_buyer_login_field = (
        By.XPATH, "/html/body/div[7]/div/div/form/div[3]/div[3]/div[1]/span")
    _sell_on_escrow_auction_description_button = (By.XPATH, "//label")
    _sell_on_escrow_auction_description_field = (By.XPATH, "/html/body/div[7]/div/div/form/div[6]/div[3]/div[1]/div/div")
    _sell_on_escrow_auction_description_value = get_random_string(10) + " " + get_random_string(7) + " " + get_random_string(8)
    _delete_auction_button = (By.XPATH, "//div[7]/div/button[7]")
    _delete_auction_accept_deletion_indicated_domains_checkbox = (
        By.XPATH, "//label/span[2]")
    _add_on_marketplace_first_domain_button = (By.XPATH, "//div[2]/div[6]/div")
    _add_on_marketplace_buynow_field = (By.NAME, 'buynow')
    _add_on_marketplace_buynow_value = get_random_integer(2)
    _add_on_marketplace_minimum_price_field = (By.NAME, "minimum")
    _add_on_marketplace_minimum_price_value = get_random_integer(1)
    _add_on_marketplace_currency_dropdown = (By.NAME, "currency")
    _add_on_marketplace_currency_index = randint(0, 3)
    _add_on_marketplace_category_checkbox = (By.XPATH, "//div[8]/div[3]/div/label")
    _add_on_marketplace_description_checkbox = (By.XPATH, "//div[3]/div[2]/label")
    _add_on_marketplace_category_field = (By.XPATH, "//span[2]/input")
    _add_on_marketplace_category_technology = (By.XPATH, "//span[2]/div/div[2]/div[4]")
    _add_on_marketplace_category_technology_computers = (By.XPATH, "//span[2]/div/div[6]/div")
    _add_on_marketplace_description_field = (By.XPATH, "//div[12]/div[3]/div/div/div")
    _add_on_marketplace_description_value = get_random_string(10) + " " + get_random_string(15)
    _add_on_marketplace_instalment_schema_dropdown = (By.XPATH, "//div[6]/div[3]/div/span/select")
    _add_on_marketplace_lease_field = (By.XPATH, "//div[7]/div[3]/div/input")
    _add_on_marketplace_lease_value = get_random_integer(2)


    def __init__(self, driver):
        super(RegisteredDomainsListPage, self).__init__(driver, self._title)

    def renew_domain_automatically(self):
        self.click(self._renew_button)
        self.click(self._renew_automatically_button)
        self.click(self._renew_automatically_when_money_on_account_radio)
        self.click(self._renew_automatically_start_from_dropdown)
        self._renew_automatically_start_from_value =  self.get_text(self._renew_automatically_start_from_option)
        self.click(self._renew_automatically_start_from_dropdown)
        self.click(self._renew_automatically_start_from_option)
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
        self.click(self._second_stage_stop_realization_until_manual_activation_radio)
        self.click(self._second_stage_submit_button)
        self.click(self._second_stage_submit_confirm_button)

    def select_first_domain(self):
        self.click(self._first_domain_checkbox)

    def change_profile_data(self):
        self.click(self._move_button)
        sleep(2)
        self.click(self._change_profile_data_button)
        self.click(self._change_profile_data_profile_dropdown)
        self._change_profile_data_profile_dropdown_option_value = self.get_text(self._change_profile_data_profile_dropdown_option)
        self.click(self._change_profile_data_profile_dropdown)
        self.click(self._change_profile_data_profile_dropdown_option)
        self.click(self._submit_button)

    def change_profile_data_stage_2(self):
        self.click(self._change_profile_data_dont_send_results_radio)
        self.click(self._second_stage_stop_realization_until_manual_activation_radio2)
        self.click(self._change_profile_data_second_stage_submit_button)
        while True:
            try:
                self.click(self._second_stage_submit_confirm_button)
                break
            except:
                self.click(self._change_profile_data_second_stage_submit_button)

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
        # self.select_index_from_dropdown(1, self._change_dns_profile_dropdown)
        self.click(self._change_dns_profile_dont_sent_results_after_operation_radio)
        self.click(self._submit_button)

    def new_dns_entry_for_selected_domain(self):
        self.click(self._redirect_button_for_selected_domain)
        self.click(self._set_dns_entries_button)

    def new_dns_entry_for_selected_domain_details(self):
        self.click(self._add_dns_entry_button)
        self.clear_field_and_send_keys(self._add_dns_entry_host_name_value, self._add_dns_entry_host_name_field)
        self.select_index_from_dropdown(1, self._add_dns_entry_type_dropdown)
        self.clear_field_and_send_keys(self._add_dns_entry_priority_value, self._add_dns_entry_priority_field)
        self.clear_field_and_send_keys(self._add_dns_entry_address_value, self._add_dns_entry_address_field)
        self.click(self._submit_button)

    def delete_new_dns_entry_for_selected_domain(self):
        self.click(self._add_dns_entry_host_name_result)
        self.click(self._delete_first_dns_priofile_button)
        self.click(self._delete_first_dns_priofile_button)

    def dns_servers_in_domain(self):
        self.click(self._redirect_button_for_selected_domain)
        self.click(self._dns_servers_in_domain_button)

    def new_dns_server_in_domain_details(self):
        self.click(self._new_dns_server_in_domain_add_server_button)
        self.clear_field_and_send_keys(self._new_dns_server_in_domain_name_value,
                                       self._new_dns_server_in_domain_name_field)
        self.clear_field_and_send_keys(self._new_dns_server_in_domain_ip_value, self._new_dns_server_in_domain_ip_field)
        self.click(self._submit_button)
        sleep(2)

    def delete_new_dns_server_in_domain(self):
        self.click(self._new_dns_server_in_domain_name_result)
        self.click(self._delete_first_dns_server)
        self.click(self._delete_first_dns_server)

    def change_parking_service(self):
        self.click(self._parking_button_first_domain)
        self.click(self._change_parking_service_button_first_domain)
        sleep(2)
        self.click(self._change_parking_service_redirect_domains_to_dns_server_checkbox)
        self.click(self._change_parking_service_send_email_after_oparation_radio)
        self.click(self._submit_button)

    def change_keyword(self):
        self.click(self._parking_button_first_domain)
        self.click(self._change_keyword_button_first_domain)
        self.clear_field_and_send_keys(self._change_keyword_value, self._change_keyword_field)
        self.click(self._change_keyword_send_email_after_operation)
        self.click(self._submit_button)

    def sell_on_auction(self):
        self.click(self._sell_button)
        self.click(self._sell_on_auction_button)
        self.clear_field_and_send_keys(self._sell_on_auction_price_start_value, self._sell_on_auction_price_start_field)
        self.select_index_from_dropdown(self._sell_on_auction_currency_value, self._sell_on_auction_currency_dropdown)
        self.select_index_from_dropdown(self._sell_on_auction_end_date_index, self._sell_on_auction_end_date_field)
        self.select_index_from_dropdown(self._sell_on_auction_end_time_index, self._sell_on_auction_end_time_field)
        self.click(self._sell_on_auction_minimal_price_checkbox)
        self.click(self._sell_on_auction_buy_now_price_checkbox)
        self.click(self._sell_on_auction_auction_description_checkbox)
        self.click(self._sell_on_auction_category_field)
        self.click(self._sell_on_auction_category_technology)
        self.click(self._sell_on_auction_category_technology_computers)
        if _element_is_visible(self.find_element(self._sell_on_auction_price_minimum_field)):
            self.clear_field_and_send_keys(self._sell_on_auction_price_minimum_value, self._sell_on_auction_price_minimum_field)
        else:
            self.click(self._sell_on_auction_minimal_price_checkbox)
            self.clear_field_and_send_keys(self._sell_on_auction_price_minimum_value, self._sell_on_auction_price_minimum_field)
        self.clear_field_and_send_keys(self._sell_on_auction_price_buynow_value,
                                       self._sell_on_auction_price_buynow_field)
        self.clear_field_and_send_keys(self._sell_on_auction_description_value, self._sell_on_auction_description_field)
        self.click(self._submit_button)

    def sell_on_auction_stage2_domain_text(self):
        return self.get_text(self._sell_on_auction_stage2_domain_name_field)

    def sell_on_auction_stage2_category_text(self):
        return self.get_text(self._sell_on_auction_stage2_category_field)

    def sell_on_auction_submit(self):
        self.click(self._sell_on_auction_stage2_realize_immediately_radio)
        # self.click(self._sell_on_auction_stage2_stop_until_manual_activation_radio)
        # self.click(self._sell_on_auction_stage2_dont_send_email_radio)
        self.click(self._submit_button)
        self.accept_alert()

    def sell_on_escrow_auction(self, login_value, price):
        self.click(self._sell_button)
        self.click(self._sell_on_escrow_auction_button)
        self.clear_field_and_send_keys(login_value, self._sell_on_escrow_auction_buyer_login_field)
        self.clear_field_and_send_keys(price, self._sell_on_escrow_auction_price_field)
        self.select_index_from_dropdown(self._sell_on_auction_currency_value, self._sell_on_auction_currency_dropdown)
        self.select_index_from_dropdown(self._sell_on_escrow_auction_days_to_pay_index,
                                        self._sell_on_escrow_auction_days_to_pay_dropdown)
        self.click(self._submit_button)

    def sell_on_escrow_auction_stage2(self):
        self.click(self._sell_on_escrow_auction_description_button)
        self.clear_field_and_send_keys(self._sell_on_escrow_auction_description_value, self._sell_on_escrow_auction_description_field)
        self.click(self._submit_button)
        self.accept_alert()

    def sell_on_escrow_auction_stage2_buyer_login_text(self):
        return self.get_text(self._sell_on_escrow_auction_stage2_buyer_login_field)

    def delete_auction(self):
        self.click(self._delete_auction_button)
        self.click(self._delete_auction_accept_deletion_indicated_domains_checkbox)
        self.click(self._submit_button)

    def third_domain_text(self):
        self._third_domain_text_value = self.get_text(self._third_domain_checkbox)

    def select_third_domain(self):
        self.click(self._third_domain_checkbox)

    def fourth_domain_text(self):
        self._fourth_domain_text_value = self.get_text(self._fourth_domain_checkbox)

    def select_fourth_domain(self):
        self.click(self._fourth_domain_checkbox)

    def second_domain_text(self):
        self._second_domain_text_value = self.get_text(self._second_domain_checkbox)

    def select_second_domain(self):
        self.click(self._second_domain_checkbox)

    def fifth_domain_text(self):
        self._fifth_domain_text_value = self.get_text(self._fifth_domain_checkbox)

    def select_fifth_domain(self):
        self.click(self._fifth_domain_checkbox)

    def add_on_marketplace(self):
        self.click(self._sell_button)
        self.click(self._add_on_marketplace_button)
        self.clear_field_and_send_keys(self._add_on_marketplace_buynow_value, self._add_on_marketplace_buynow_field)
        self.select_index_from_dropdown(self._add_on_marketplace_currency_index,
                                        self._add_on_marketplace_currency_dropdown)
        self.clear_field_and_send_keys(self._add_on_marketplace_minimum_price_value,
                                       self._add_on_marketplace_minimum_price_field)
        self.select_index_from_dropdown(1, self._add_on_marketplace_instalment_schema_dropdown)
        self.clear_field_and_send_keys(self._add_on_marketplace_lease_value, self._add_on_marketplace_lease_field)
        if (_element_is_visible(self.find_element(self._add_on_marketplace_category_field))):
            pass
        else:
            self.click(self._add_on_marketplace_category_checkbox)
        if (_element_is_visible(self.find_element(self._add_on_marketplace_description_field))):
            pass
        else:
            self.click(self._add_on_marketplace_description_checkbox)
        self.click(self._add_on_marketplace_category_field)
        self.click(self._add_on_marketplace_category_technology)
        self.click(self._add_on_marketplace_category_technology_computers)
        self.clear_field_and_send_keys(self._add_on_marketplace_description_value,
                                       self._add_on_marketplace_description_field)
        self.click(self._submit_button)

    def store_authinfo(self):
        self._result_text = self.get_text(self._result_text_field)
        self._authinfo = self._result_text[14:]

    def move_domain_from_account(self, login):
        self.click(self._move_button)
        self.click(self._move_to_other_account_button)
        self.clear_field_and_send_keys(login, self._move_to_other_account_login_field)
        self.click(self._submit_button)