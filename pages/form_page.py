from selenium.webdriver.common.by import By


class FormPage:

    URL = "https://the-internet.herokuapp.com/login"

    USERNAME = (By.ID, "username")
    PASSWORD = (By.ID, "password")

    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.get(self.URL)

    def enter_username(self, username):
        self.driver.find_element(*self.USERNAME).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element(*self.PASSWORD).send_keys(password)

    def get_username(self):
        return self.driver.find_element(
            *self.USERNAME
        ).get_attribute("value")

    def get_password(self):
        return self.driver.find_element(
            *self.PASSWORD
        ).get_attribute("value")