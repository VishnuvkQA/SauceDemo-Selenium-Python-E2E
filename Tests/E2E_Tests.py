from selenium import webdriver
from selenium.webdriver.chrome import options
import datetime
import time
import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from Pages.Login_page import LoginPage
from Pages.Inventory_page import Products
from Pages.checkout_page import Checkout_Page
from Pages.Checkout_info import Checkoutinformation
from Pages.final_overview import Finalpage

#Assign the driver and its options
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.saucedemo.com/")

try:
    #Call the pages functions in order to proceed
    #Login to the page
    Login = LoginPage(driver)
    Login.login("standard_user","secret_sauce")
    time.sleep(3)
    print("Logged in Successfully\n")


    #Adding products to cart 
    Inventory = Products(driver)
    Inventory.check_productpage()
    time.sleep(2)
    assert Inventory.totall() == "2", f"It should be 2 but we got {Inventory.totall()}"
    print("Added products to the cart successfully")

    #Checkout Page
    Checkout = Checkout_Page(driver)
    Checkout.checkout()
    time.sleep(2)

    assert Checkout.cart_num() == "1", f"It should be 1 as we removed one product out of 2 but it is {Checkout.cart_num()}"
    print("\nChecked out successfully")

    #Checkout information 
    info = Checkoutinformation(driver)
    info.enter_det("Vishnu","Kumar", "600118")
    time.sleep(2)
    print("\nDetails entered successfully")

    #Final page
    Final_page = Finalpage(driver)
    Final_page.final()
    assert driver.current_url == "https://www.saucedemo.com/checkout-complete.html" , f"Expected url is https://www.saucedemo.com/checkout-complete.html but we got {driver.current_url}"
    Final_page.home()
    print("\nReturned to home successfully")
    time.sleep(2)
except:
    driver.quit()
    raise
