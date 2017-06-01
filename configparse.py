# -*- coding: utf-8 -*-
import configparser

config = configparser.ConfigParser()
config.read('config.ini')

_url = config['SiteUrl']['URL']
# _url_controls = config['SiteUrl']['URL_CONTROLS']

_user = config['UserAccounts']['USER']
_user_password = config['UserAccounts']['PASSWORD']

_user_beta = config['UserAccounts']['USER_BETA']
_user_beta_password = config['UserAccounts']['PASSWORD_BETA']

_user_gamma = config['UserAccounts']['USER_GAMMA']
_user_gamma_password = config['UserAccounts']['PASSWORD_GAMMA']

_user_delta = config['UserAccounts']['USER_DELTA']
_user_delta_password = config['UserAccounts']['PASSWORD_DELTA']
