from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:
    URL = "https://www.saucedemo.com/"

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open(self):
        self.driver.get(self.URL)

    def enter_username(self, username):
        field = self.wait.until(
            EC.presence_of_element_located((By.ID, "user-name"))
        )
        field.clear()
        field.send_keys(username)

    def enter_password(self, password):
        field = self.driver.find_element(By.ID, "password")
        field.clear()
        field.send_keys(password)

    def click_login(self):
        button = self.driver.find_element(By.ID, "login-button")
        button.click()
