import pytest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture
def driver():
    options = Options()
    driver = webdriver.Firefox(options=options)
    yield driver
    driver.quit()


def test_shop_checkout(driver):
    driver.get("https://www.saucedemo.com/")
    wait = WebDriverWait(driver, 10)

    wait.until(
        EC.presence_of_element_located((By.ID, "user-name"))
    ).send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    add_ids = [
        "add-to-cart-sauce-labs-backpack",
        "add-to-cart-sauce-labs-bolt-t-shirt",
        "add-to-cart-sauce-labs-onesie",
    ]
    for btn_id in add_ids:
        wait.until(
            EC.element_to_be_clickable((By.ID, btn_id))
        ).click()

    wait.until(
        EC.element_to_be_clickable(
            (By.CSS_SELECTOR, ".shopping_cart_container a")
        )
    ).click()

    wait.until(
        EC.element_to_be_clickable((By.ID, "checkout"))
    ).click()

    wait.until(
        EC.presence_of_element_located((By.ID, "first-name"))
    ).send_keys("Иван")
    driver.find_element(By.ID, "last-name").send_keys("Петров")
    driver.find_element(By.ID, "postal-code").send_keys("123456")
    driver.find_element(By.ID, "continue").click()

    total = wait.until(
        EC.visibility_of_element_located(
            (By.CLASS_NAME, "summary_total_label")
        )
    )
    total_text = total.text
    assert "$58.29" in total_text, (
        f"Ожидалось $58.29, получено: {total_text}"
    )
