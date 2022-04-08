from os.path import join
from pathlib import Path
from time import sleep

from selenium.webdriver.common.by import By

from var.config_variables import *

from customLibrary.AppuimSessionHandler import AppuimSessionHandler


class Tradestab:
    def __init__(self):
        self.session_handler = AppuimSessionHandler()
        pass

    def select_order_type_changer(self):
        driver = self.session_handler.get_session_instance()
        driver.find_element(by=By.ID, value="tradeTypeSpinner").click()
        sleep(1.5)

    def select_fast_order_type(self):
        driver = self.session_handler.get_session_instance()
        driver.find_element(by=By.XPATH, value="//*[@text='سریع']").click()
        sleep(1)

    def select_trigger_order_type(self):
        driver = self.session_handler.get_session_instance()
        driver.find_element(by=By.XPATH, value="//*[@text='حد ضرر']").click()
        sleep(1)

    def select_sell_button(self):
        driver = self.session_handler.get_session_instance()
        driver.find_element(by=By.ID, value="bck_tab_sell").click()
        sleep(1)

    def send_price(self, price):
        driver = self.session_handler.get_session_instance()
        driver.find_element(by=By.ID, value="priceMET").send_keys(str(price))
        sleep(1)

    def send_ammount(self, amount):
        driver = self.session_handler.get_session_instance()
        driver.find_element(by=By.ID, value="amountMET").send_keys(str(amount))

    def send_trigger_ammount(self, trigger_amount):
        driver = self.session_handler.get_session_instance()
        driver.find_element(by=By.ID, value="triggerMET").send_keys(str(trigger_amount))

    def get_average_price(self):
        driver = self.session_handler.get_session_instance()
        average_amount = driver.find_elements(by=By.ID, value="price")[1].text
        return str(average_amount)

    def click_buy(self):
        driver = self.session_handler.get_session_instance()
        driver.find_element(by=By.XPATH, value="//*[@text='خرید بیت‌کوین']").click()
        sleep(1)
    def click_sell(self):
        driver = self.session_handler.get_session_instance()
        driver.find_element(by=By.XPATH, value="//*[@text='فروش بیت‌کوین']").click()
        sleep(1)
    def find_no_funds(self):
        driver=self.session_handler.get_session_instance()
        driver.find_element(by=By.XPATH,value="//*[@text='افزایش موجودی']")
        sleep(1)
    def click_100_percent(self):
        driver=self.session_handler.get_session_instance()
        driver.find_element(by=By.XPATH,value="//*[@text='100%']").click()
        sleep(1)
    def click_increase_amount(self):
        driver=self.session_handler.get_session_instance()
        driver.find_element(by=By.ID,value="addAmountIV").click()
        sleep(0.5)