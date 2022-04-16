from time import sleep

from customLibrary.AppuimSessionHandler import AppuimSessionHandler
from selenium.webdriver.common.by import By
from appium.webdriver.common.touch_action import TouchAction
from customLibrary.Actions import Actions
from var.Mrketstab_locations import *


class MarketsTab(Actions):
    def __init__(self):
        self.session_handler = AppuimSessionHandler()
        pass

    def nobitex_coins_click_subtab(self):
        self.find(By.ID, nobitex_subtab, 5).click()
        sleep(2)

    def nobitex_toman_subtab_click(self):
        self.find(By.ID, toman_nobitex_subtab, 5).click()
        sleep(2)

    def nobitex_tether_subtab_click(self):
        self.find(By.ID, tether_nobitex_subtab, 5).click()
        sleep(2)

    def btc_irt_star_click_favorite(self):
        self.find(By.ID, star_favorite_first_checkbox, 5).click()
        sleep(2)

    def click_btc_market(self):
        driver = self.session_handler.get_session_instance()
        driver.find_element(by=By.XPATH, value="BTC").click()
        sleep(2)

    def click_buy_in_market_detail(self):
        driver = self.session_handler.get_session_instance()
        driver.find_element(by=By.ID, value="buy_btn").click()
        sleep(2)

    def click_sell_in_market_detail(self):
        driver = self.session_handler.get_session_instance()
        driver.find_element(by=By.ID, value="sell_btn").click()
        sleep(3)

    def find_btc_tarde_page(self):
        driver = self.session_handler.get_session_instance()
        driver.find_element(by=By.XPATH, value="//*[@text='مقدار(BTC)']")
        sleep(2)
