from appium import webdriver as a
from selenium import webdriver as web_driver


class AppuimSessionHandler:
    __driver = None

    def __init__(self):
        pass

    @staticmethod
    def open_application(appium_host='http://127.0.0.1:8888/wd/hub', caps=None) -> web_driver:
        AppuimSessionHandler.__driver = a.Remote(str(appium_host), desired_capabilities=caps)
        return AppuimSessionHandler.__driver


    @staticmethod
    def get_session_instance() -> web_driver:
        if not AppuimSessionHandler.__driver:
            raise Exception('no application is open')
        return AppuimSessionHandler.__driver
