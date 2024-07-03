from selenium import webdriver
from time import sleep

chrome = webdriver.Chrome()
firefox = webdriver.Firefox()
try:
    count = 0
    chrome.get ("http://uitestingplayground.com/dynamicid")
    firefox.get ("http://uitestingplayground.com/dynamicid")

    # Клик на синюю кнопку
    blue_button = chrome.find_element(
        "xpath", '//button[text()="Button with Dynamic ID"]').click()
    blue_button = firefox.find_element(
        "xpath", '//button[text()="Button with Dynamic ID"]').click()
    # Клик на кнопку 3 раза
    for i in range(3):
        blue_button = chrome.find_element(
            "xpath", '//button[text()="Button with Dynamic ID"]').click()
        blue_button = firefox.find_element(
            "xpath", '//button[text()="Button with Dynamic ID"]').click()
        count = count + 1
        sleep(2)
        print(count)
except Exception as ex:
        print(ex)
finally:
        chrome.quit()
        firefox.quit()