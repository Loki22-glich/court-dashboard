from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service
import time

# Optional: If you know where your geckodriver is, set it here:
# service = Service("/opt/homebrew/bin/geckodriver")

# Firefox options
options = Options()
# Comment out headless if you want to see the browser
# options.add_argument("--headless")

# Start Firefox browser
# If you installed geckodriver with brew, you likely don't need to specify service
driver = webdriver.Firefox(options=options)

# Load Delhi High Court search page
driver.get("https://delhihighcourt.nic.in/case.asp")

# Fill the form
driver.find_element("name", "ctype").send_keys("W.P. (C)")
driver.find_element("name", "cno").send_keys("12345")
driver.find_element("name", "cyear").send_keys("2023")

# Click the submit button
driver.find_element("xpath", "//input[@type='submit']").click()

# Wait and print results
time.sleep(5)
print("Page title:", driver.title)
print("URL:", driver.current_url)

# Keep the browser open to see output
time.sleep(30)
driver.quit()
