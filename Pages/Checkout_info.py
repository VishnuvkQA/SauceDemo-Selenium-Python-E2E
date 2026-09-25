from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from utilities.screenshots import take_ss

class Checkoutinformation:

    #Locators in this page
    fn = (By.ID, "first-name")
    ln = (By.ID, "last-name")
    postal = (By.ID, "postal-code")
    cont = (By.ID, "continue")

    #Functions for this page

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver,5)

    def first_name(self,fname):
        return self.wait.until(ec.visibility_of_element_located(self.fn)).send_keys(fname)

    def last_name(self,lname):
        return self.wait.until(ec.visibility_of_element_located(self.ln)).send_keys(lname)

    def zipcode(self,zcode):
        return self.wait.until(ec.visibility_of_element_located(self.postal)).send_keys(zcode)

    def continue_btn(self):
        return self.wait.until(ec.element_to_be_clickable(self.cont)).click()

    def enter_det(self,fname,lname,zcode):
        self.first_name(fname)
        self.last_name(lname)
        self.zipcode(zcode)
        take_ss(self.driver, "Checkout_details")
        self.continue_btn()
        return