from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class FormPage(BasePage):

    URL = "https://the-internet.herokuapp.com/login"

    USERNAME = (By.ID, "username")
    PASSWORD = (By.ID, "password")

    def open(self):
        self.driver.get(self.URL)

    def enter_username(self, username):
        self.send_keys(self.USERNAME, username)

    def enter_password(self, password):
        self.send_keys(self.PASSWORD, password)

    def get_username(self):
        return self.get_attribute(self.USERNAME, "value")

    def get_password(self):
        return self.get_attribute(self.PASSWORD, "value")