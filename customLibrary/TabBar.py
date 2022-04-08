from os.path import join
from pathlib import Path
from time import sleep

from selenium.webdriver.common.by import By

from customLibrary.AppuimSessionHandler import AppuimSessionHandler
from customLibrary import TestCases
from var.config_variables import *


class TabBar:
    def __init__(self):
        self.session_handler = AppuimSessionHandler()
        pass

    def dashboard_tab(self):
        driver = self.session_handler.get_session_instance()
        driver.find_element_by_id('navigation_dashboard').click()

    def markets_tab(self):
        driver = self.session_handler.get_session_instance()
        driver.find_element_by_id('navigation_markets').click()

    def trades_tab(self):
        driver = self.session_handler.get_session_instance()
        driver.find_element_by_id('navigation_trades').click()

    def funds_tab(self):
        driver = self.session_handler.get_session_instance()
        driver.find_element_by_id('navigation_funds').click()
        sleep(2)

    def account_tab(self):
        driver = self.session_handler.get_session_instance()
        driver.find_element(by=By.ID, value='navigation_account').click()
        sleep(1)
