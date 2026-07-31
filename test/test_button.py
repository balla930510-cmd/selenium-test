from selenium import webdriver
from selenium.webdriver.common.by import By


def test_button_click():
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--window-size=1920,1080")

    driver = webdriver.Chrome(options=options)

    try:
        driver.get("https://the-internet.herokuapp.com/add_remove_elements/")

        button = driver.find_element(By.XPATH, "//button[text()='Add Element']")
        button.click()

        delete_button = driver.find_element(By.CLASS_NAME, "added-manually")

        assert delete_button.is_displayed()

    finally:
        driver.quit()