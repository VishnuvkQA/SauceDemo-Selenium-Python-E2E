from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from utilities.screenshots import take_ss
class Checkout_Page:

    #Locators to be located in this page
    remove_tshirt = (By.ID, "remove-sauce-labs-bolt-t-shirt")
    cart_badge = (By.CLASS_NAME, "shopping_cart_badge")
    checkout_btn = (By.ID,"checkout")

    #Functions needed for this page

    def __init__(self,driver):
        self.driver = driver
        self.wait = WebDriverWait(driver,5)

    def remove_btn(self):
        return self.wait.until(ec.element_to_be_clickable(self.remove_tshirt)).click()

    def cart_num(self):
        return self.wait.until(ec.visibility_of_element_located(self.cart_badge)).text

    def checkout_button(self):
        return self.wait.until(ec.element_to_be_clickable(self.checkout_btn)).click()
    

    def checkout(self):
        self.remove_btn()
        self.cart_num()
        take_ss(self.driver, "Final_Products")
        self.checkout_button()
        return 
        
