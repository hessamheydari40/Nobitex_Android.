from time import sleep
from customLibrary.AppuimSessionHandler import AppuimSessionHandler
from selenium.webdriver.common.by import By
from appium.webdriver.common.touch_action import TouchAction

class Actions():
    def __init__(self):
        pass

    def find(self, by , locator= None, timeout=3 ):
        driver = self.session_handler.get_session_instance()
        driver.implicitly_wait(timeout)
        el = driver.find_element(by=by, value=locator)
        return el