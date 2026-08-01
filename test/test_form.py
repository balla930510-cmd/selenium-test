from selenium.webdriver.common.by import By


def test_form_success(driver):
    driver.get("https://the-internet.herokuapp.com/login")

    username = driver.find_element(By.ID, "username")
    password = driver.find_element(By.ID, "password")

    username.send_keys("測試帳號")
    password.send_keys("123456")

    assert username.get_attribute("value") == "測試帳號"
    assert password.get_attribute("value") == "123456"