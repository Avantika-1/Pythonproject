from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = webdriver.ChromeOptions()
driver = webdriver.Chrome(options=options)
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options,service=Service(ChromeDriverManager().install()))

def verify_title():


    driver.get("https://testing.testaonline.com/signin")
    wait = WebDriverWait(driver, 10)
    title = driver.title
    expected_title = "Testa|Dev"
    if title == expected_title:
            print("title verification sucessfully")
    else:
           print(f"title verification failed. Expected '{expected_title}', but got {title}'.")


