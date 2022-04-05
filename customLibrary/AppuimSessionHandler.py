from appium import webdriver as a
from selenium import webdriver as web_driver


class AppuimSessionHandler():

    def __init__(self):
        pass

    @staticmethod
    def open_application(appium_host='http://127.0.0.1:8888/wd/hub', caps=None):
        driver = a.Remote(str(appium_host), desired_capabilities=caps)
        return driver
