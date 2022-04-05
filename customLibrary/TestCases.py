import pathlib
from os.path import join
import unittest
from appium import webdriver

from pathlib import Path
from var.config_variables import *
from time import sleep
from customLibrary import AppuimSessionHandler



class TestCases():
    def __init__(self):
        pass

    def NOBIAPP52(self):
        app_path = Path(__file__).parent.parent
        app_path = join(str(app_path), 'app', 'Nobitex_Testnet.apk')
        caps = {
            'platformName': device_platform, 'fullReset': full_reset, 'deviceName': device_name,
            'automationName': 'UiAutomator2',
            'skipServerInstallation': False, 'appActivity': app_acctivity, 'noReset': no_reset,
            'udid': udid, 'newCommandTimeout': 1200, 'autoGrantPermissions': True,
            'appPackage': app_package, 'disableWindowAnimation': True, 'app': app_path
        }
        openn = AppuimSessionHandler.AppuimSessionHandler.open_application(caps=caps)
        sleep(4)

        openn.find_element_by_id('navigation_trades').click()
        openn.find_element_by_id('priceMET').send_keys('1125000000')
        openn.find_element_by_id('amountMET').send_keys('0.000001')
        openn.find_element_by_xpath("//*[@text='خرید بیت‌کوین']").click()
        sleep(5)
        openn.find_element_by_xpath("//*[@text='افزایش موجودی']")
        sleep(5)

