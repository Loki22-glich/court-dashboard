from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# Optional: adjust if you have chromedriver path
service = Service('/usr/local/bin/chromedriver')

# Start the Chrome browser
driver = webdriver.Chrome(service=service)

# Open Delhi High Court website
driver.get("https://delhihighcourt.nic.in/")
driver.implicitly_wait(5)

# Print page title to confirm
print("Page title:", driver.title)

driver.quit()
