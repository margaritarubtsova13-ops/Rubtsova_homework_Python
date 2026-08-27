from selenium import webdriver
from selenium.webdriver.common.by import By


def test_form_submission():
    driver = webdriver.Chrome()
    try:
        driver.get("https://httpbin.qa-territory.online/forms/post")

        # Находим поле ввода по имени и вводим текст
        field = driver.find_element(By.NAME, "custname")
        field.send_keys("Margarita")

        # Находим кнопку Submit (текст "Submit order") и нажимаем
        button = driver.find_element(By.XPATH, "//button[contains(text(), 'Submit')]")
        button.click()

        # Проверяем, что URL изменился
        assert driver.current_url != "https://httpbin.qa-territory.online/forms/post"
    finally:
        driver.quit()


if __name__ == "__main__":
    test_form_submission()
