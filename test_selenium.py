from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

# Use the correct chromedriver path
service = Service('/opt/homebrew/bin/chromedriver')

# Optional: run in headless mode (no GUI)
options = Options()
options.add_argument("--headless")

# Create driver
driver = webdriver.Chrome(service=service, options=options)

# Test: Open Delhi High Court site
driver.get("https://delhihighcourt.nic.in/")
print("Page Title:", driver.title)

driver.quit()
