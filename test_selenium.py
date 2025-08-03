from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time

# Set path to your installed ChromeDriver
service = Service('/opt/homebrew/bin/chromedriver')

options = Options()
# Not headless, so you can see it
# options.add_argument('--headless')  ← make sure this line is commented or removed

# Start the driver
driver = webdriver.Chrome(service=service, options=options)

# Go to the Case Search page
driver.get("https://delhihighcourt.nic.in/case.asp")

# Print the page title
print("Page Title:", driver.title)

# ❗ Wait before closing the browser
time.sleep(20)  # Keeps the browser open for 20 seconds

# Close the browser (you can comment this too if needed)
# driver.quit()
