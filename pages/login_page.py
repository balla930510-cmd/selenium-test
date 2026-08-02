from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class LoginPage(BasePage):

    URL = "https://the-internet.herokuapp.com/login"

    USERNAME = (By.ID, "username")
    PASSWORD = (By.ID, "password")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "button[type='submit']")

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

    def click_login(self):
        self.wait_for_clickable(
            self.LOGIN_BUTTON
        ).click()

    def login(self, username, password):
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()