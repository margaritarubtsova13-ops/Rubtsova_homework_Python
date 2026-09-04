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


def test_form_validation(driver):
    driver.get(
        "https://bonigarcia.dev/selenium-webdriver-java/data-types.html"
    )
    driver.maximize_window()
    wait = WebDriverWait(driver, 10)

    fields = {
        "first-name": "Иван",
        "last-name": "Петров",
        "address": "Ленина, 55-3",
        "e-mail": "test@skypro.com",
        "phone": "+7985899998787",
        "city": "Москва",
        "country": "Россия",
        "job-position": "QA",
        "company": "SkyPro",
    }

    for name, value in fields.items():
        elem = wait.until(
            EC.presence_of_element_located((By.NAME, name))
        )
        elem.clear()
        elem.send_keys(value)
    
    submit = wait.until(
        EC.presence_of_element_located(
            (By.CSS_SELECTOR, "button[type='submit']")
        )
    )
    driver.execute_script("arguments[0].click();", submit)

    wait.until(
        lambda d: "data-types-submitted" in d.current_url
    )

    zip_div = wait.until(
        EC.presence_of_element_located((By.ID, "zip-code"))
    )
    zip_class = zip_div.get_attribute("class") or ""
    assert "alert-danger" in zip_class, (
        f"Zip code не подсвечен красным, класс: {zip_class}"
    )

    for field_id in fields:
        div = driver.find_element(By.ID, field_id)
        cls = div.get_attribute("class") or ""
        assert "alert-success" in cls, (
            f"Поле {field_id} не подсвечено зелёным, класс: {cls}"
        )
