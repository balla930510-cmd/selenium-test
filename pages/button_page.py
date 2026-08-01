from selenium.webdriver.common.by import By


class ButtonPage:

    URL = "https://the-internet.herokuapp.com/add_remove_elements/"

    ADD_BUTTON = (
        By.XPATH,
        "//button[text()='Add Element']"
    )

    DELETE_BUTTON = (
        By.CLASS_NAME,
        "added-manually"
    )

    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.get(self.URL)

    def click_add_element(self):
        self.driver.find_element(*self.ADD_BUTTON).click()

    def is_delete_button_displayed(self):
        return self.driver.find_element(
            *self.DELETE_BUTTON
        ).is_displayed()