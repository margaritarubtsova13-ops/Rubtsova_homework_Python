from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CalculatorPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 60)
        self.url = "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html"

    def open(self):
        self.driver.get(self.url)

    def set_delay(self, seconds: int):
        # Находим поле ввода задержки и устанавливаем значение
        delay_input = self.wait.until(EC.presence_of_element_located((By.ID, "delay")))
        delay_input.clear()
        delay_input.send_keys(str(seconds))

    def click_button(self, label: str):
        locator = (By.XPATH, f"//span[contains(@class,'btn') and text()='{label}']")
        btn = self.wait.until(EC.element_to_be_clickable(locator))
        btn.click()

    def get_result(self):
        # Ждем, пока в поле screen появится текст, и возвращаем его
        screen = self.wait.until(EC.presence_of_element_located((By.CLASS_NAME, "screen")))
        return screen.text.strip()
