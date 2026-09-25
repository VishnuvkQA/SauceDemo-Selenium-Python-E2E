#using this page just to create a function for taking screenshot and saving it in a folder so that i can call this function whenever i want
import os
import sys

def take_ss(driver,pagename):
    folder = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "Screenshots")
    os.makedirs(folder, exist_ok=True)
    path = os.path.join(folder, f"{pagename}.png")
    print("Saving screenshot to:", path)
    driver.save_screenshot(os.path.join(folder,f"{pagename}.png"))