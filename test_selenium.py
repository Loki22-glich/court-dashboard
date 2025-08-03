from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

# Set ChromeDriver path
service = Service('/opt/homebrew/bin/chromedriver')

# Open browser normally (no headless for now)
options = Options()
# options.add_argument('--headless')  ← comment this out for now

# Start driver
driver = webdriver.Chrome(service=service, options=options)

# Open case search page directly
driver.get("https://delhihighcourt.nic.in/case.asp")

# Print page title
print("Page Title:", driver.title)

# Comment this out temporarily so you can see the browser
# driver.quit()
