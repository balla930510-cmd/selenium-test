from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class FormPage(BasePage):

    URL = "https://the-internet.herokuapp.com/login"

    USERNAME = (By.ID, "username")
    PASSWORD = (By.ID, "password")

    def open(self):
        self.driver.get(self.URL)

    def enter_username(self, username):
        self.wait_for_element(
            self.USERNAME
        ).send_keys(username)

    def enter_password(self, password):
        self.wait_for_element(
            self.PASSWORD
        ).send_keys(password)

    def get_username(self):
        return self.wait_for_element(
            self.USERNAME
        ).get_attribute("value")

    def get_password(self):
        return self.wait_for_element(
            self.PASSWORD
        ).get_attribute("value")