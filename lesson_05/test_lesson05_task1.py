from selenium import webdriver
from selenium.webdriver.common.by import By


def test_navigation():
    driver = webdriver.Chrome()

    # Открываем главную страницу
    driver.get("https://httpbin.qa-territory.online")

    # Кликаем на ссылку HTML Form
    link = driver.find_element(By.LINK_TEXT, "HTML Form")
    link.click()

    # Проверяем, что URL изменился на /forms/post
    assert "/forms/post" in driver.current_url

    # Возвращаемся назад
    driver.back()

    # Проверяем, что вернулись на исходный URL
    assert driver.current_url == "https://httpbin.qa-territory.online/"

    driver.quit()

if __name__ == "__main__":
    test_navigation()
