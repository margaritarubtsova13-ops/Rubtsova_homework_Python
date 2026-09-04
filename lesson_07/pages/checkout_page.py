from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CheckoutPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def fill_form(self, first_name, last_name, postal_code):
        fn = self.wait.until(
            EC.presence_of_element_located((By.ID, "first-name"))
        )
        fn.clear()
        fn.send_keys(first_name)

        ln = self.driver.find_element(By.ID, "last-name")
        ln.clear()
        ln.send_keys(last_name)

        pc = self.driver.find_element(By.ID, "postal-code")
        pc.clear()
        pc.send_keys(postal_code)

    def click_continue(self):
        button = self.driver.find_element(By.ID, "continue")
        button.click()

    def get_total(self):
        total = self.wait.until(
            EC.visibility_of_element_located(
                (By.CLASS_NAME, "summary_total_label")
            )
        )
        return total.text
