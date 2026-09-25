from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from Pages.Inventory_page import Products
from utilities.screenshots import take_ss
class LoginPage:
    #Locators for login page

    user_input = (By.ID, "user-name")
    password_input = (By.ID, "password")
    Login_btn = (By.ID, "login-button")

    #Functions for Login page

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver,5)

    def enter_username(self,username):
        self.wait.until(ec.visibility_of_element_located(self.user_input)).send_keys(username)
        return

    def enter_password(self,password):
        self.wait.until(ec.visibility_of_element_located(self.password_input)).send_keys(password)
        return 

    def click_btn(self):
        self.wait.until(ec.element_to_be_clickable(self.Login_btn)).click()

    def login(self,username,password):
        self.enter_username(username)
        self.enter_password(password)
        take_ss(self.driver, "Loginpage_details")
        self.click_btn()
        return Products(self.driver)
    #Products(self.driver)
    
