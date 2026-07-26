from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://the-internet.herokuapp.com/login")

username = driver.find_element(By.ID, "username")
password = driver.find_element(By.ID, "password")

username.send_keys("測試帳號")
password.send_keys("123456")

print("Username:", username.get_attribute("value"))
print("Password:", password.get_attribute("value"))

assert username.get_attribute("value") == "測試帳號"
assert password.get_attribute("value") == "123456"

print("表單測試成功！")

driver.quit()