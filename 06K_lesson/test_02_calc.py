import pytest
from selenium import webdriver
from selenium.webdriver.edge.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture
def driver():
    options = Options()
    driver = webdriver.Edge(options=options)
    yield driver
    driver.quit()


def test_slow_calculator(driver):
    driver.get(
        "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html"
    )
    wait = WebDriverWait(driver, 60)

    delay = wait.until(EC.presence_of_element_located((By.ID, "delay")))
    delay.clear()
    delay.send_keys("45")

    buttons = ["7", "+", "8", "="]
    for label in buttons:
        btn = wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, f"//span[contains(@class,'btn') and text()='{label}']")
            )
        )
        btn.click()

    screen = wait.until(
        EC.presence_of_element_located((By.CLASS_NAME, "screen"))
    )
    wait.until(lambda d: screen.text.strip() == "15")

    assert screen.text.strip() == "15", (
        f"Ожидалось 15, получено: {screen.text}"
    )
