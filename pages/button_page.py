from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class ButtonPage(BasePage):

    URL = "https://the-internet.herokuapp.com/add_remove_elements/"

    ADD_BUTTON = (
        By.XPATH,
        "//button[text()='Add Element']"
    )

    DELETE_BUTTON = (
        By.CLASS_NAME,
        "added-manually"
    )

    def open(self):
        self.driver.get(self.URL)

    def click_add_element(self):
        self.click(self.ADD_BUTTON)

    def is_delete_button_displayed(self):
        return self.wait_for_element(
            self.DELETE_BUTTON
        ).is_displayed()