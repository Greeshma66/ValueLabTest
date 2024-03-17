import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.implicitly_wait(0.5)
driver.get("https://orikan-ui-automation-test.azurewebsites.net/")

driver.maximize_window()

driver.find_element(By.ID, "emailAddress").send_keys("def@gmail.com")
driver.find_element(By.ID, "password").send_keys("QWERTY")
driver.find_element(By.ID, "confirmPassword").send_keys("QWERTY")

driver.find_element(By.XPATH, "//button[contains(text(),'Next')]").click()
time.sleep(3)

driver.find_element(By.ID, "firstName").send_keys("Value")
driver.find_element(By.ID, "lastName").send_keys("Labs")
driver.find_element(By.ID, "addressLine1").send_keys("hitech city")
driver.find_element(By.ID, "postcode").send_keys("500044")
driver.find_element(By.ID, "city").send_keys("hyderabad")
s = Select(driver.find_element(By.XPATH, "//select[@id='state']"))
s.select_by_visible_text("Queensland")

driver.find_element(By.XPATH, "//button[contains(text(),'Next')]").click()
time.sleep(3)

driver.find_element(By.ID, "cardHolderName").send_keys("valueLabs")
driver.find_element(By.XPATH, "//input[@id='cardTypeVISA']").click()
driver.find_element(By.ID, "cardNumber").send_keys("1234 5678 0123")
driver.find_element(By.XPATH, "//input[@id='cardCVV']").send_keys("852")
s = Select(driver.find_element(By.XPATH, "//select[@id='cardExpiryMonth']"))
s.select_by_visible_text("July")
driver.find_element(By.XPATH, "//input[@id='cardExpiryYear']").send_keys("2030")

driver.find_element(By.XPATH, "//button[contains(text(),'Next')]").click()
time.sleep(3)

fBody = driver.find_element(By.ID, "termsAndConditions")
scroll = 0
while scroll < 5:  # this will scroll 3 times
    driver.execute_script('arguments[0].scrollTop = arguments[0].scrollTop + arguments[0].offsetHeight;',
                          fBody)
    scroll += 1
    # add appropriate wait here, of course. 1-2 seconds each
    time.sleep(3)

driver.find_element(By.XPATH, "//input[@id='agreedToTerms']").click()
driver.find_element(By.XPATH, "//button[contains(text(),'Submit')]").click()
time.sleep(3)

print("USER SUCCESSFULLY REGISTERED!!!")


