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
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
import re

SCREEN_DUMP_LOCATION = os.path.join(
    os.path.dirname(os.path.abspath(__file__)), 'screendumps'
)
run_locally = True

# @on_platforms(browsers)


class SmokeTest(unittest.TestCase):
    _internal_non_grouped_domain_text = 1

    def test_filter_monitored_domains_registered_should_succeed(self):

        home_page = HomePage(self.driver).open_home_page()
        account_page = home_page.header.login(USER_DELTA, PASSWORD_DELTA)
        monitor_domains_list = account_page.header.open_monitor_domains_list()
        monitor_domains_list.filter_registered()

        WebDriverWait(self.driver, 30).until(EC.text_to_be_present_in_element(monitor_domains_list._first_domain_status_field, u"Zarejestrowana"))

    def test_search_domain_in_catalog_should_succeed(self):

        home_page = HomePage(self.driver).open_home_page()
        account_page = home_page.header.login(USER_GAMMA, PASSWORD_GAMMA)
        domain_catalog_list = account_page.header.open_domain_catalog_list()
        domain_catalog_list.search_second_domain_in_catalog()

        WebDriverWait(self.driver, 30).until(EC.text_to_be_present_in_element(domain_catalog_list._first_domain_in_catalog_field, domain_catalog_list.second_domain_value))

    def test_login_wrong_credentials_should_succeed(self):

        home_page = HomePage(self.driver).open_home_page()
        account_page = home_page.header.login(get_random_string(7), get_random_uuid(6))

        Assert.contains(u"Nieprawidłowy login lub hasło", account_page.get_page_source())
    def test_search_buyer_escrow_auctions_should_succeed(self):

        home_page = HomePage(self.driver).open_home_page()
        account_page = home_page.header.login(USER_DELTA, PASSWORD_DELTA)
        escrow_auction_page = account_page.header.open_escrow_transactions_buyer_list()
        escrow_auction_page.get_text_second_domain_status_and_price()
        escrow_auction_page.search_for_auction(escrow_auction_page.second_domain_text)

        WebDriverWait(self.driver, 30).until(EC.text_to_be_present_in_element(escrow_auction_page._first_auction_domain_name_field, escrow_auction_page.second_domain_text))
        Assert.equal(escrow_auction_page.second_domain_status_text, escrow_auction_page.first_auction_buyer_status_text())
        Assert.equal(escrow_auction_page.second_domain_price_text, escrow_auction_page.first_auction_price_text())

    def test_new_hire_seller_transaction_should_succeed(self):

        login = "alfa"

        home_page = HomePage(self.driver).open_home_page()
        account_page = home_page.header.login(USER_DELTA, PASSWORD_DELTA)
        hire_seller_list = account_page.header.open_hire_seller_list()
        hire_seller_list.add_hire_transaction_stage1()

        WebDriverWait(self.driver, 30).until(EC.text_to_be_present_in_element(hire_seller_list._add_hire_transaction_domain_name_second_checkbox, ".pl"))

        hire_seller_list.add_hire_transaction_stage2(login)

        Assert.contains(hire_seller_list._hire_domain_name_text, hire_seller_list.get_page_source())
        Assert.contains(login, hire_seller_list.get_page_source())
        Assert.contains(hire_seller_list._add_hire_transaction_monthly_installment_value, hire_seller_list.get_page_source())
        Assert.contains(str(hire_seller_list._add_hire_transaction_number_of_installments_value)+" miesi", hire_seller_list.get_page_source())
        Assert.contains(str(int(hire_seller_list._add_hire_transaction_monthly_installment_value) * int(hire_seller_list._add_hire_transaction_number_of_installments_value)), hire_seller_list.get_page_source())

        hire_seller_list.add_hire_transaction_submit()
        WebDriverWait(self.driver, 40).until_not(EC.text_to_be_present_in_element(hire_seller_list._add_hire_transaction_performing_text_field, "Trwa wykonywanie operacji..."))
        account_page.header.open_hire_seller_list()

        Assert.contains(hire_seller_list._hire_domain_name_text, hire_seller_list.get_page_source())
        Assert.contains(login, hire_seller_list.get_page_source())
        Assert.contains(str(int(hire_seller_list._add_hire_transaction_monthly_installment_value) * int(hire_seller_list._add_hire_transaction_number_of_installments_value)), hire_seller_list.get_page_source())

        hire_seller_list.cancel_first_hire_transaction()

        Assert.contains(hire_seller_list._hire_domain_name_text, hire_seller_list.get_page_source())
        Assert.contains(login, hire_seller_list.get_page_source())
        Assert.contains(hire_seller_list._add_hire_transaction_monthly_installment_value, hire_seller_list.get_page_source())
        Assert.contains(str(hire_seller_list._add_hire_transaction_number_of_installments_value)+" miesi", hire_seller_list.get_page_source())
        Assert.contains(str(int(hire_seller_list._add_hire_transaction_monthly_installment_value) * int(hire_seller_list._add_hire_transaction_number_of_installments_value)), hire_seller_list.get_page_source())

        hire_seller_list.cancel_first_hire_transaction_submit()

        Assert.contains(u"Transakcja sprzedaży na raty została anulowana.", hire_seller_list.get_page_source())

#TRWA WYKONYWANIE OPERACJI, zgłoszone

    def test_search_appraisal_list_should_succeed(self):

        home_page = HomePage(self.driver).open_home_page()
        account_page = home_page.header.login(USER_DELTA, PASSWORD_DELTA)
        appraisal_list = account_page.header.open_appraisal_list()
        appraisal_list.get_fourth_appraisal_domain_time_type_and_status()
        appraisal_list.search_for_appraisal(appraisal_list.fourth_appraisal_domain)

        WebDriverWait(self.driver, 30).until(EC.text_to_be_present_in_element(appraisal_list._first_appraisal_domain_field, appraisal_list.fourth_appraisal_domain))
        WebDriverWait(self.driver, 30).until(EC.text_to_be_present_in_element(appraisal_list._first_appraisal_time_field, appraisal_list.fourth_appraisal_time))
        WebDriverWait(self.driver, 30).until(EC.text_to_be_present_in_element(appraisal_list._first_appraisal_type_field, appraisal_list.fourth_appraisal_type))
        WebDriverWait(self.driver, 30).until(EC.text_to_be_present_in_element(appraisal_list._first_appraisal_status_field, appraisal_list.fourth_appraisal_status))

#BŁĄD BRAK WYNIKÓW

    def test_search_active_appraisals_list_should_succeed(self):

        home_page = HomePage(self.driver).open_home_page()
        account_page = home_page.header.login(USER_DELTA, PASSWORD_DELTA)
        appraisal_list = account_page.header.open_active_appraisals_list()
        appraisal_list.get_fourth_appraisal_domain_time_and_propositions()
        appraisal_list.search_for_appraisal(appraisal_list.fourth_appraisal_domain)

        WebDriverWait(self.driver, 30).until(EC.text_to_be_present_in_element(appraisal_list._first_appraisal_domain_field, appraisal_list.fourth_appraisal_domain))
        WebDriverWait(self.driver, 30).until(EC.text_to_be_present_in_element(appraisal_list._first_appraisal_time_field, appraisal_list.fourth_appraisal_time))
        WebDriverWait(self.driver, 30).until(EC.text_to_be_present_in_element(appraisal_list._first_appraisal_propositions_field, appraisal_list.fourth_appraisal_propositions))

#BŁĄD BRAK WYNIKÓW

    def test_zz_generate_plot_and_send_email(self):
        self._save_plot()
        self._send_email()

    def tally(self):
        return len(self._resultForDoCleanups.errors) + len(self._resultForDoCleanups.failures)

    def setUp(self):
        self.timeout = 30
        if run_locally:
            fp = webdriver.FirefoxProfile()
            fp.set_preference("browser.startup.homepage", "about:blank")
            fp.set_preference("startup.homepage_welcome_url", "about:blank")
            fp.set_preference("startup.homepage_welcome_url.additional", "about:blank")
            fp.set_preference(" xpinstall.signatures.required", "false")
            fp.set_preference("toolkit.telemetry.reportingpolicy.firstRun", "false")
            binary = FirefoxBinary('/__stare/firefox45/firefox')
            self.driver = webdriver.Firefox(firefox_binary=binary, firefox_profile=fp)
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
        err = len(self._resultForDoCleanups.errors)
        fail = len(self._resultForDoCleanups.failures)
        succ = len(self._resultForDoCleanups.success)

        # The slices will be ordered and plotted counter-clockwise.
        labels = 'Errors', 'Failures', 'Passes'
        sizes = [err, fail, succ]
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