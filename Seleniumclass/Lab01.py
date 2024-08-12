import time

from selenium import webdriver

def test_open_vwologin():

    driver = webdriver.Edge()
    driver.get("https://app.vwo.com/#/login")

    #code -> converted to HTTP request -> post
    #Post request | crete the session
    #session is created - Unique ID - 16 digit ID

    print(driver.session_id)
    print(driver.title)
    assert driver.title == "Login - VWO"  #assert is used for verifying
    time.sleep(10)