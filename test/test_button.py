from selenium.webdriver.common.by import By


def test_button_click(driver):
    driver.get(
        "https://the-internet.herokuapp.com/add_remove_elements/"
    )

    add_button = driver.find_element(
        By.XPATH,
        "//button[text()='Add Element']"
    )

    add_button.click()

    delete_button = driver.find_element(
        By.CLASS_NAME,
        "added-manually"
    )

    assert delete_button.is_displayed()