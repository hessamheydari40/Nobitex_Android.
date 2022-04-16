from time import sleep

from customLibrary.AppuimSessionHandler import AppuimSessionHandler
from selenium.webdriver.common.by import By
from appium.webdriver.common.touch_action import TouchAction
class DashboardTab:
    def __init__(self):
        self.session_handler = AppuimSessionHandler()
        pass

    def find_btc_starred_favoriute(self):
        driver = self.session_handler.get_session_instance()
        driver.find_element(by=By.XPATH,value="//*[@text='BTC']")
        sleep(1)
    def refresh_dashboard_tab(self):
        driver=self.session_handler.get_session_instance()
        driver.swipe(44,276,44,992,1000)
        sleep(3)