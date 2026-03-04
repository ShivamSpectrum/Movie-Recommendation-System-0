from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time

# Path to ChromeDriver
service = Service("chromedriver.exe")

# Start Chrome browser
driver = webdriver.Chrome(service=service)

# Test Case 1: Open home page
driver.get("http://127.0.0.1:8000")

print("Page title is:", driver.title)

# Wait for observation
time.sleep(5)

# Close browser
driver.quit()

print("Selenium test executed successfully!")
