import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.implicitly_wait(0.5)
driver.get("https://orikan-ui-automation-test.azurewebsites.net/")

driver.maximize_window()
time.sleep(3)

driver.find_element(By.ID, "emailAddress").send_keys("betty@orikan.com")
time.sleep(3)

driver.find_element(By.ID, "password").send_keys("qwerty")
time.sleep(3)

driver.find_element(By.ID, "confirmPassword").send_keys("qwerty")
time.sleep(5)

driver.find_element(By.XPATH, "//button[contains(text(),'Next')]").click()
time.sleep(3)

print("Existing User already !!!")
