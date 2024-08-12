
#option class ->headless mode - no ui

#from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.edge.options import Options

def test_open_vwologin():

    chrome_options = Options()
    chrome_options.add_argument("--windowsize = 1920x1080")

    driver = webdriver.Chrome(chrome_options)
    driver.get("https://app.vwo.com/#/login")
