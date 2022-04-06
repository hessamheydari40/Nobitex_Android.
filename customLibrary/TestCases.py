import math
import pathlib
from os.path import join
import unittest
from appium import webdriver
from math import ceil

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

    def NOBIAPP53(self):
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
        sleep(2)
        openn.find_element_by_id("tradeTypeSpinner").click()
        sleep(3)
        openn.find_element_by_xpath("//*[@text='سریع']").click()
        sleep(1.5)
        openn.find_element_by_id('amountMET').send_keys('0.001')
        sleep(1.5)
        openn.find_element_by_xpath("//*[@text='خرید بیت‌کوین']").click()
        sleep(3)
        openn.find_element_by_xpath("//*[@text='افزایش موجودی']")
        sleep(5)

    def NOBIAPP59(self):
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
        sleep(2)
        openn.find_element_by_id("tradeTypeSpinner").click()
        sleep(1)
        openn.find_element_by_xpath("//*[@text='سریع']").click()
        sleep(1.5)
        openn.find_element_by_xpath("//*[@text='100%']").click()
        sleep(1.5)
        openn.find_element_by_xpath("//*[@text='خرید بیت‌کوین']").click()
        sleep(3)
        openn.find_element_by_xpath("//*[@text='افزایش موجودی']")
        sleep(5)

    def NOBIAPP54(self):
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
        sleep(2)
        openn.find_element_by_id("tradeTypeSpinner").click()
        sleep(3)
        openn.find_element_by_xpath("//*[@text='حد ضرر']").click()
        sleep(1.5)
        openn.find_element_by_id('triggerMET').send_keys('1125000000')
        sleep(1.5)
        openn.find_element_by_id('priceMET').send_keys('1100000000')
        sleep(1.5)
        openn.find_element_by_id('amountMET').send_keys('0.001')
        sleep(1.5)
        openn.find_element_by_xpath("//*[@text='خرید بیت‌کوین']").click()
        sleep(3)
        openn.find_element_by_xpath("//*[@text='افزایش موجودی']")
        sleep(5)

    def NOBIAPP60(self):
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
        sleep(2)
        openn.find_element_by_id("tradeTypeSpinner").click()
        sleep(1)
        openn.find_element_by_xpath("//*[@text='حد ضرر']").click()
        sleep(1.5)
        openn.find_element_by_id('triggerMET').send_keys('1125000000')
        sleep(1.5)
        openn.find_element_by_id('priceMET').send_keys('1100000000')
        sleep(1.5)
        openn.find_element_by_xpath("//*[@text='100%']").click()
        sleep(0.9)
        openn.find_element_by_xpath("//*[@text='خرید بیت‌کوین']").click()
        sleep(3)
        openn.find_element_by_xpath("//*[@text='افزایش موجودی']")
        sleep(5)

    def NOBIAPP55(self):
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
        openn.find_element_by_id("bck_tab_sell").click()
        priceMet = openn.find_elements_by_id("price")[1].text
        s = str(int(int(''.join(priceMet.split(',')))))
        openn.find_element_by_id('priceMET').send_keys(s)
        sleep(0.4)
        openn.find_element_by_id('amountMET').send_keys('0.001')
        sleep(0.5)
        openn.find_element_by_xpath("//*[@text='فروش بیت‌کوین']").click()
        sleep(1)
        openn.find_element_by_xpath("//*[@text='افزایش موجودی']")
        sleep(1.1)

    def NOBIAPP61(self):
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
        openn.find_element_by_id("bck_tab_sell").click()
        sleep(3)
        priceMet = openn.find_elements_by_id("price")[1].text
        s = str(int(int(''.join(priceMet.split(',')))))
        openn.find_element_by_id('priceMET').send_keys(s)
        sleep(0.4)
        openn.find_element_by_xpath("//*[@text='100%']").click()
        sleep(0.8)
        openn.find_element_by_xpath("//*[@text='فروش بیت‌کوین']").click()
        sleep(1)
        openn.find_element_by_xpath("//*[@text='افزایش موجودی']")
        sleep(2)

    def NOBIAPP56(self):
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
        openn.find_element_by_id("bck_tab_sell").click()
        openn.find_element_by_id("tradeTypeSpinner").click()
        sleep(0.4)
        openn.find_element_by_xpath("//*[@text='سریع']").click()
        sleep(0.5)
        openn.find_element_by_id('amountMET').send_keys('0.001')
        sleep(0.5)
        openn.find_element_by_xpath("//*[@text='فروش بیت‌کوین']").click()
        sleep(1)
        openn.find_element_by_xpath("//*[@text='افزایش موجودی']")
        sleep(1.1)

    def NOBIAPP57(self):
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
        openn.find_element_by_id("bck_tab_sell").click()
        openn.find_element_by_id("tradeTypeSpinner").click()
        sleep(0.4)
        openn.find_element_by_xpath("//*[@text='حد ضرر']").click()
        sleep(0.5)
        priceMet = openn.find_elements_by_id("price")[1].text
        s = str(int(int(''.join(priceMet.split(',')))))
        openn.find_element_by_id('priceMET').send_keys(s)
        s2 = str(int(s)+1)
        openn.find_element_by_id('triggerMET').send_keys(s2)
        sleep(0.6)
        openn.find_element_by_id('amountMET').send_keys('0.001')
        sleep(0.5)
        openn.find_element_by_xpath("//*[@text='فروش بیت‌کوین']").click()
        sleep(0.8)
        openn.find_element_by_xpath("//*[@text='افزایش موجودی']")
        sleep(1)
