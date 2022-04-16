from os.path import join
from pathlib import Path
from time import sleep

from selenium.webdriver.common.by import By

from var.config_variables import *
from var.TradesRab_locations import *
from customLibrary.AppuimSessionHandler import AppuimSessionHandler
from customLibrary.Actions import Actions


class Tradestab(Actions):
    def __init__(self):
        self.session_handler = AppuimSessionHandler()
        pass

    def select_order_type_changer(self):
        self.find(By.ID, order_type_changer, 5).click()
        sleep(1)

    def select_fast_order_type(self):
        self.find(By.XPATH, fast_order_type, 5).click()
        sleep(1)

    def select_trigger_order_type(self):
        self.find(By.XPATH, trigger_order_type, 5).click()
        sleep(1)

    def select_sell_section_button(self):
        self.find(By.ID, sell_section).click()
        sleep(1)

    def send_price(self, pricee):
        self.find(By.ID, price, 5).send_keys(str(pricee))
        sleep(1)

    def send_ammount(self, amountt):
        self.find(By.ID, ammount, 5).send_keys(str(amountt))
        sleep(1)

    def send_trigger_ammount(self, trigger_amount):
        self.find(By.ID, trigger_ammount, 5).send_keys(str(trigger_amount))
        sleep(1)

    def get_average_price(self):
        average_amount = self.find(By.ID, prices, 5)[5].text
        return str(average_amount)

    def click_buy(self):
        self.find(By.XPATH, buy, 5).click()
        sleep(1)

    def click_sell(self):
        self.find(By.XPATH, sell, 5).click()
        sleep(1)

    def find_no_funds(self):
        self.find(By.XPATH, increase_found, 5)
        sleep(1)

    def click_100_percent(self):
        self.find(By.XPATH, c_100_perceent, 5).click()
        sleep(1)

    def click_increase_amount(self):
        self.find(By.ID, increase_amount, 5).click()
        sleep(0.5)

    def click_confirm(self):
        self.find(By.ID, confirm, 5).click()
        sleep(0.5)

    def find_succesfull(self):
        self.find(By.XPATH, order_successfull, 5)
        sleep(0.9)
