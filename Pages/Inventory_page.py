from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from utilities.screenshots import take_ss

class Products:

    #Locators in the products page
    jacket = (By.CSS_SELECTOR, '[data-test="add-to-cart-sauce-labs-fleece-jacket"]')
    tshirt = (By.CSS_SELECTOR, '[data-test="add-to-cart-sauce-labs-bolt-t-shirt"]')
    cart_num = (By.CLASS_NAME, "shopping_cart_badge")
    checkout = (By.CLASS_NAME, "shopping_cart_link")

    #Create functions in this Page

    def __init__(self,driver):
        self.driver = driver
        self.wait = WebDriverWait(driver,5)

    def product_jacket(self):
        self.wait.until(ec.element_to_be_clickable(self.jacket)).click()
        return
    
    def product_tshirt(self):
        self.wait.until(ec.element_to_be_clickable(self.tshirt)).click()
        return
    
    def totall(self):
        return self.wait.until(ec.visibility_of_element_located(self.cart_num)).text

    def checkout_btn(self):
        return self.wait.until(ec.element_to_be_clickable(self.checkout)).click()

    def check_productpage(self):
        self.product_jacket()
        self.product_tshirt()
        self.totall()
        take_ss(self.driver, "Products_added")
        self.checkout_btn()
        return 
        