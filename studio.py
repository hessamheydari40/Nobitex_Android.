import unittest
import time
from appium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions


class Untitled(unittest.TestCase):
    reportDirectory = 'reports'
    reportFormat = 'xml'
    dc = {}
    testName = 'Untitled'
    driver = None

    def setUp(self):
        self.dc['reportDirectory'] = self.reportDirectory
        self.dc['reportFormat'] = self.reportFormat
        self.dc['testName'] = self.testName
        self.dc['udid'] = '202a91e20409'
        self.dc['appPackage'] = 'app.nobitex.testnet'
        self.dc['appActivity'] = 'ir.nobitex.activities.SplashScreen'
        self.dc['platformName'] = 'android'
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', self.dc)

    def testUntitled(self):
        self.driver.find_element_by_xpath("xpath=//*[@text='ورود']").click()

    def tearDown(self):
        self.driver.quit()

    if __name__ == '__main__':
        unittest.main()
