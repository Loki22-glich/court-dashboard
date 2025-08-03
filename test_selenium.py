from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time

# Set Chrome options
options = Options()
# options.add_argument('--headless')  # Uncomment only if needed later
options.add_argument('--disable-gpu')
options.add_argument('--no-sandbox')

# Use WebDriverManager to get the right driver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# Open the case search page
driver.get("https://delhihighcourt.nic.in/case.asp")

# Print page title
print("Page Title:", driver.title)

# Wait for 30 seconds to keep browser open
time.sleep(30)

# Close browser after wait
driver.quit()
