from selenium import webdriver
from selenium.webdriver.common.by import By

def test_button_click():
    driver = webdriver.Chrome()
    driver.get("https://the-internet.herokuapp.com/add_remove_elements/")
    driver.find_element(By.CSS_SELECTOR, "button").click()

    delete_button = driver.find_element(By.CLASS_NAME, "added-manually")

    assert delete_button.is_displayed()

    print("按鈕測試成功！")

    driver.quit()