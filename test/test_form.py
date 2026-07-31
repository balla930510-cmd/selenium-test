from selenium import webdriver
from selenium.webdriver.common.by import By


def test_form_success():
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--window-size=1920,1080")

    driver = webdriver.Chrome(options=options)

    try:
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

    finally:
        driver.quit()