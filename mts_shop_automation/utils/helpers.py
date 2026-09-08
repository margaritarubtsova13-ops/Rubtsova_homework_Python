import time

from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


def wait_for_element(
    driver: WebDriver,
    by: str,
    value: str,
    timeout: int = 10,
) -> WebElement:
    """Ждёт появления элемента на странице."""
    return WebDriverWait(driver, timeout).until(
        EC.presence_of_element_located((by, value))
    )


def hide_overlays(driver: WebDriver) -> None:
    """Скрывает мешающие оверлеи на странице."""
    driver.execute_script(
        "document.querySelectorAll("
        "'.flocktory-widget-overlay, .modal, "
        ".popup, .overlay'"
        ").forEach(function(el) {"
        "el.style.display = 'none';"
        "});"
    )
    time.sleep(1)


def close_city_modal(driver: WebDriver) -> None:
    """Закрывает модальное окно выбора города."""
    try:
        wait = WebDriverWait(driver, 5)
        btn = wait.until(
            EC.element_to_be_clickable((
                "xpath",
                '//button[contains(text(), "Да") and '
                'ancestor::*[contains(@class, "region") or '
                'contains(@class, "modal") or '
                'contains(@class, "popup")]] | '
                '//button[contains(@class, "confirm-region")]'
            ))
        )
        driver.execute_script("arguments[0].click();", btn)
        time.sleep(1)
    except Exception:
        try:
            btn = driver.find_element(
                "xpath", '//button[contains(text(), "Да")]'
            )
            driver.execute_script(
                "arguments[0].click();", btn
            )
            time.sleep(1)
        except Exception:
            pass


def remove_flocktory(driver: WebDriver) -> None:
    """Удаляет виджеты Flocktory со страницы."""
    driver.execute_script(
        "var iframe = document.querySelector("
        "'iframe[title=\"Flocktory widget\"]');"
        "if (iframe) iframe.remove();"
        "var overlays = document.querySelectorAll("
        "'[class*=\"flocktory\"], [class*=\"overlay\"]');"
        "overlays.forEach(function(el) { el.remove(); });"
    )
    time.sleep(0.5)
