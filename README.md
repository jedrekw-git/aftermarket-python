# aftermarket2-selenium
Testy nowego Aftermarket.pl

# Konfiguracja

Dane potrzebne do uruchomienia testów powinny znalezć się w pliku config.ini umieszczonym w głownym katalogu (tam gdzie README.md)

Przykładowa zawartość pliku config.ini:

[SiteUrl]

URL = https://devel:miodzio@testy.aftermarket2.pl/

[UserAccounts]


USER = alfa

PASSWORD = testujalfa


USER_BETA = beta

PASSWORD_BETA = testujbeta


USER_GAMMA = gamma

PASSWORD_GAMMA = testujgamma


USER_DELTA = delta

PASSWORD_DELTA = testujdelta



W części [SiteUrl] zmienna URL reprezentuje adres strony na której operują testy. Adres powinien być wpisany wg. zasady

URL = https://LOGIN:HASLO@ADRES.pl/

W cześci [UserAccounts] znajdują się dane do logowania do profilu użytkownika, które są potem wykorzystywane w testach np. w linijce

account_page = home_page.header.login(USER, PASSWORD)

Dane są parsowane w pliku configparse.py, który jest umieszczony w głownym katalogu.

Jeśli jest potrzeba można dopisać swoje zmienne do pliku congig.ini i configparse.py, lub operować na zmiennych już parsowanych