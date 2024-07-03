from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

chrome = webdriver.Chrome()
firefox = webdriver.Firefox()
try:
    chrome.get("http://uitestingplayground.com/classattr")
    firefox.get("http://uitestingplayground.com/classattr")
    # Нажать синюю кнопку три раза
    for p in range(3):
           blue_button = chrome.find_element(
                  "xpath", "//button[contains(concat(' ', normalize-space(@class), ' '), ' btn-primary ')]")
           blue_button.click()
           blue_button = firefox.find_element(
                  "xpath", "//button[contains(concat(' ', normalize-space(@class), ' '), ' btn-primary ')]")
           blue_button.click()
           sleep(2)
        
           chrome.switch_to.alert.accept()
           firefox.switch_to.alert.accept()
except Exception as ex:
        print(ex)
finally:
        chrome.quit()
        firefox.quit()
