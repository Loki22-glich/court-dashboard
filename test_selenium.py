from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import time

options = Options()
driver = webdriver.Firefox(options=options)

driver.get("https://delhihighcourt.nic.in/case.asp")

# Fill the form
driver.find_element("name", "ctype").send_keys("W.P. (C)")
driver.find_element("name", "cno").send_keys("6094")
driver.find_element("name", "cyear").send_keys("2022")

# Submit form using JavaScript instead of .click()
driver.execute_script("document.forms[0].submit()")

# Wait and show output
time.sleep(5)
print("Title:", driver.title)
print("URL:", driver.current_url)

time.sleep(30)
driver.quit()
