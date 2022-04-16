from time import sleep

from customLibrary.AppuimSessionHandler import AppuimSessionHandler
from selenium.webdriver.common.by import By
from appium.webdriver.common.touch_action import TouchAction
from  var.Menutab_locations import *
from customLibrary.Actions import Actions
class Menutab(Actions):
    def __init__(self):
        self.session_handler = AppuimSessionHandler()
        pass

    def select_security(self):
        self.find(By.ID,security,5).click()
        sleep(1)

    def logout_click(self):
        self.find(By.ID,logout,5).click()
        sleep(3)

    def select_auto_lock(self):
        self.find(By.ID,security_auto_lock,5).click()
        sleep(1)

    def send_auto_lock_minute(self, minute):
        driver = self.session_handler.get_session_instance()
        driver.find_element(by=By.ID, value="timer").send_keys(minute)
        sleep(1)

    def click_confirm_auto_lock(self):
        driver = self.session_handler.get_session_instance()
        driver.find_element(by=By.ID, value="ok_btn").click()
        sleep(1)

    def click_enable_pin_code(self):
        self.find(By.ID,pincode_switch,5).click()
        sleep(0.5)

    def home_button_click(self):
        driver = self.session_handler.get_session_instance()    #    457,2210
        driver.press_keycode(3)
        sleep(1)

    def home_sleep(self, secend):
        driver = self.session_handler.get_session_instance()
        driver.find_element(by=By.ID, value="hint_text_alignment")
        sleep(secend)
        sleep(1)

    def recent_apps_click(self):            #    217     2210
        driver = self.session_handler.get_session_instance()
        driver.press_keycode(187)
        sleep(1)

    def click_only_open_app(self):
        driver = self.session_handler.get_session_instance()
        driver.find_element(by=By.ID, value="task_view_thumbnail").click()
        sleep(0.5)
    def find_enter_pin(self):
        driver = self.session_handler.get_session_instance()
        driver.implicitly_wait(15)
        driver.find_element(by=By.ID, value="tv_enter_pin")
        sleep(1)
    def background_application(self,duration):
        driver=self.session_handler.get_session_instance()
        driver.implicitly_wait(10)
        driver.background_app(seconds=duration)
        sleep(3)


