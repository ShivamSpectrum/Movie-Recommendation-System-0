from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

service = Service("chromedriver.exe")
driver = webdriver.Chrome(service=service)

# Test Case 1: Open Home Page
driver.get("http://127.0.0.1:8000")
print("TC01: Home page opened")

# Test Case 2: Check Page Title
title = driver.title
print("TC02: Page title is:", title)

# Test Case 3: Verify Current URL
current_url = driver.current_url
print("TC03: Current URL:", current_url)

# Test Case 4: Check Page Body Exists
body = driver.find_element(By.TAG_NAME, "body")
print("TC04: Page body found")

# Test Case 5: Wait and Close Browser
time.sleep(3)
driver.quit()
print("TC05: Browser closed successfully")
