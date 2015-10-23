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

        Assert.contains(u"Lista adresów email", settings_page.get_page_source())
        Assert.contains(u"Oto lista twoich adresów email. Dla każdego adresu możesz wybrać, jakie powiadomienia i newslettery będziesz otrzymywać.", settings_page.get_page_source())

    def test_change_newsletter_settings_should_succeed(self):
        home_page = HomePage(self.driver).open_home_page()
        account_page = home_page.header.login(USER, PASSWORD)
        settings_page = account_page.header.open_settings_page()
        change_newsletter_settings_page = settings_page.open_change_newsletter_settings_page()
        settings_page.change_newsletter_settings()
        settings_page.save_change_notification_settings()

        Assert.contains(u"Lista adresów email", settings_page.get_page_source())
        Assert.contains(u"Oto lista twoich adresów email. Dla każdego adresu możesz wybrać, jakie powiadomienia i newslettery będziesz otrzymywać.", settings_page.get_page_source())

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

        settings_page.remove_added_user()

        self.not_contains(settings_page._add_other_user_login_value, settings_page.get_page_source())
        self.not_contains(settings_page._add_other_user_description_value, settings_page.get_page_source())

    def test_change_company_address_should_succeed(self):
        home_page = HomePage(self.driver).open_home_page()
        account_page = home_page.header.login(USER_BETA, PASSWORD_BETA)
        settings_page = account_page.header.open_settings_page()
        change_company_address_page = settings_page.open_change_company_data_page()
        settings_page.edit_company_address()

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

        Assert.contains("Lista kont bankowych", settings_page.get_page_source())
        Assert.contains(u"Na tej liście znajdują się konta bankowe, na które możesz zlecać wypłaty.", settings_page.get_page_source())
        Assert.contains("Oto lista twoich kont bankowych.", settings_page.get_page_source())
        self.not_contains(settings_page._add_bank_account_account_number_value, settings_page.get_page_source())
        self.not_contains(settings_page._add_bank_account_account_name_value, settings_page.get_page_source())

    def test_change_DNS_servers_should_succeed(self):
        home_page = HomePage(self.driver).open_home_page()
        account_page = home_page.header.login(USER, PASSWORD)
        settings_page = account_page.header.open_settings_page()
        bank_accounts_page = settings_page.open_change_DNS_servers_page()
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
        bank_accounts_page = settings_page.open_new_DNS_profile_page()
        settings_page.new_DNS_profile()

        Assert.equal("Operacja wykonana poprawnie", settings_page.new_DNS_profile_successful_operation_text())
        Assert.equal(settings_page._new_DNS_profile_name_value, settings_page.new_DNS_profile_successtul_opertation_profile_text())
        Assert.equal(settings_page._new_DNS_profile_host_value, settings_page.new_DNS_profile_successtul_opertation_host_text())
        Assert.equal(settings_page._new_DNS_profile_address_value, settings_page.new_DNS_profile_successtul_opertation_address_text())

        settings_page = account_page.header.open_settings_page()
        bank_accounts_page = settings_page.open_new_DNS_profile_page()

        Assert.contains("Lista profili DNS", settings_page.get_page_source())
        Assert.equal(settings_page._new_DNS_profile_name_value, settings_page.new_DNS_profile_name_text())

        settings_page.delete_added_profile()

        self.not_contains(settings_page._new_DNS_profile_name_value, settings_page.get_page_source())

    def test_register_domain_should_succeed(self):
        home_page = HomePage(self.driver).open_home_page()
        account_page = home_page.header.login(USER_BETA, PASSWORD_BETA)
        register_domain_page = account_page.header.open_register_domain_page()
        register_domain_page.enter_domain_to_register()
        WebDriverWait(self.driver, 30).until(EC.text_to_be_present_in_element(register_domain_page._domain_status_field, u"Dostępna do rejestracji"))
        register_domain_page.register_domain()
        WebDriverWait(self.driver, 20).until(EC.text_to_be_present_in_element(register_domain_page._registration_effect_text_field,"Domena zarejestrowana poprawnie"))

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
        sizes = [err, 86-err]
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
                          To=["jedrzej.wojcieszczyk@testuj.pl", "nic@po7352672n.pl"])
        message.Subject = "Raport Jenkins Aftermarket2 Testy Automatyczne"
        message.Html = """<p>Cześć!<br>
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