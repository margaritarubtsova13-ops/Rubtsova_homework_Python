from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_dynamic_loading():
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 30)

    try:
        print("Шаг 1: Открываем страницу...")
        driver.get("https://the-internet.herokuapp.com/dynamic_loading/2")

        print("Шаг 2: Ищем и кликаем кнопку Start...")
        start_button = wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, "//button[normalize-space()='Start']")
            )
        )
        start_button.click()

        print("Шаг 3: Ждём появления текста 'Hello World!'...")
        wait.until(
            EC.text_to_be_present_in_element(
                (By.ID, "finish"), "Hello World!"
            )
        )

        finish_block = driver.find_element(By.ID, "finish")
        result_text = finish_block.text

        print(f"Шаг 4: Проверяем текст. Найдено: '{result_text}'")
        assert "Hello World!" in result_text, (
            f"Ожидался текст 'Hello World!', но получено: '{result_text}'"
        )

        # Сохраняем скриншот
        driver.save_screenshot("dynamic_loading_hello_world.png")
        print("✅ Скриншот сохранён: dynamic_loading_hello_world.png")

        print("✅ Тест 1 пройден успешно!")

    except Exception as e:
        print("❌ Тест 1 упал с ошибкой!")
        print(f"Причина: {e}")

        # Делаем скриншот в случае ошибки
        try:
            driver.save_screenshot("error_screenshot.png")
            print("❌ Скриншот ошибки сохранён: error_screenshot.png")
        except Exception:
            pass

        raise
    finally:
        driver.quit()

if __name__ == "__main__":
    test_dynamic_loading()
