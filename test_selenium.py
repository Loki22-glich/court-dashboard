from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import time

# Setup
options = Options()
# options.add_argument("--headless")  # Use this later for background automation

driver = webdriver.Firefox(options=options)

# Step 1: Open the Case Search Page
driver.get("https://delhihighcourt.nic.in/case.asp")

# Step 2: Fill the form fields
driver.find_element("name", "ctype").send_keys("W.P. (C)")     # Case Type
driver.find_element("name", "cno").send_keys("12345")          # Case Number
driver.find_element("name", "cyear").send_keys("2023")         # Filing Year

# Step 3: Submit the form
driver.find_element("xpath", "//input[@type='submit']").click()

# Step 4: Wait to load results
time.sleep(5)

# Step 5: Print the new page title or URL
print("After Search - Title:", driver.title)
print("Current URL:", driver.current_url)

# Optional: Wait before quitting
time.sleep(20)
driver.quit()
