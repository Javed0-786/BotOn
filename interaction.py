from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


import requests
import time
import pandas
import pyperclip


chrome_driver_path = "C:\Development\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("https://pricee.com/")
driver.maximize_window()
time.sleep(5)

search = driver.find_element(by=By.CSS_SELECTOR, value="search-box input")
search.send_keys("redmi note 7")
search.send_keys(Keys.ENTER)
time.sleep(27)
print(driver)
data = driver.find_element(
    by=By.ID, value='wtb-deal-list')
print(data.text)
time.sleep(60)
