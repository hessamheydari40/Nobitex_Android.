from os.path import join
from pathlib import Path
from time import sleep

from selenium.webdriver.common.by import By

from customLibrary.AppuimSessionHandler import AppuimSessionHandler
from var.config_variables import *


class General:
    def open_application(self):
        app_path = Path(__file__).parent.parent
        app_path = join(str(app_path), 'app', 'Nobitex_Testnet.apk')
        caps = {
            'platformName': device_platform, 'fullReset': full_reset, 'deviceName': device_name,
            'automationName': 'UiAutomator2',
            'skipServerInstallation': False, 'appActivity': app_acctivity, 'noReset': no_reset,
            'udid': udid, 'newCommandTimeout': 1200, 'autoGrantPermissions': True,
            'appPackage': app_package, 'disableWindowAnimation': True, 'app': app_path, 'platformNAme': platformName
        }
        openn = AppuimSessionHandler.open_application(caps=caps)
        sleep(5)





