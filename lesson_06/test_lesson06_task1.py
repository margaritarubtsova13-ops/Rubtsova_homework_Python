from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_dynamic_loading():
    driver = webdriver.Chrome()
    try:
       
        driver.get("https://the-internet.herokuapp.com/dynamic_loading/2")

        wait = WebDriverWait(driver, 20)

        start_button = wait.until(
            EC.presence_of_element_located((By.XPATH, "//button[normalize-space()='Start']"))
        )
        
        start_button.click()

        result_block = wait.until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, ".example-result"))
        )

        wait.until(lambda d: result_block.text.strip() != "")

        assert "Hello World!" in result_block.text, (
            f"Не найден текст 'Hello World!'. Содержимое блока: '{result_block.text}'"
        )

        # 5. Скриншот
        driver.save_screenshot("dynamic_loading_hello_world.png")

    finally:
        driver.quit()

if __name__ == "__main__":
    test_dynamic_loading()
