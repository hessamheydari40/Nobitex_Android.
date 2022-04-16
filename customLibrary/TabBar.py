from os.path import join
from pathlib import Path
from time import sleep
from selenium.webdriver.common.by import By

from customLibrary.AppuimSessionHandler import AppuimSessionHandler
from var.config_variables import *
from customLibrary.Actions import Actions
from var.Tabbar_locations import *


class TabBar(Actions):
    def __init__(self):
        self.session_handler = AppuimSessionHandler()
        pass

    # navigation_dashboard
    def dashboard_tab(self):
        self.find(By.ID, dashboard_tab, 3).click()
        sleep(2)

    def markets_tab(self):
        self.find(By.ID,markets_tab,3).click()
        sleep(2)
    def trades_tab(self):
        self.find(By.ID,trades_tab,3).click()
        sleep(3)
    def funds_tab(self):
        self.find(By.ID,funds_tab,3).click()
        sleep(2)
    def account_tab(self):
        self.find(By.ID,account_tab,3).click()
        sleep(2)
