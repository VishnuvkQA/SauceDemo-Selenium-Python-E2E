from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from utilities.screenshots import take_ss
import time
class Finalpage:

    #locators for this page
    finish_btn = (By.ID, "finish")
    home_btn = (By.ID, "back-to-products")

    #Functions 
    def __init__(self,driver):
        self.driver = driver
        self.wait = WebDriverWait(driver,5)

    def finish(self):
        return self.wait.until(ec.element_to_be_clickable(self.finish_btn)).click()
        

    def home(self):
        time.sleep(2)
        return self.wait.until(ec.element_to_be_clickable(self.home_btn)).click()

    def final(self):
        self.finish()
        time.sleep(2)
        take_ss(self.driver,"Finalpage")
        print("Final_screenshot_take_Successfully")
        

    