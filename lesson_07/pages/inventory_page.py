from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class InventoryPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def add_item_by_name(self, item_name):
        item_id = "add-to-cart-" + item_name.lower().replace(" ", "-")
        button = self.wait.until(
            EC.element_to_be_clickable((By.ID, item_id))
        )
        button.click()

    def go_to_cart(self):
        cart_link = self.wait.until(
            EC.element_to_be_clickable(
                (By.CSS_SELECTOR, ".shopping_cart_container a")
            )
        )
        cart_link.click()
