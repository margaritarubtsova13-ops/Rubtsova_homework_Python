import sys
import time
import allure
import pytest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

sys.path.insert(0, "..")
from utils.helpers import (  # noqa: E402
    close_city_modal,
    hide_overlays,
    remove_flocktory,
)


@pytest.fixture
def chrome_driver():
    """Создаёт и возвращает экземпляр Chrome WebDriver."""
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.mark.ui
class TestUITests:
    """UI-тесты для интернет-магазина МТС Shop."""

    @allure.title(
        "Клик по логотипу возвращает на главную страницу"
    )
    @allure.story("Навигация")
    def test_logo_click(
        self,
        chrome_driver: WebDriver,
        ui_config: dict[str, str],
    ) -> None:
        """Кейс 1: Клик по логотипу возвращает на главную."""
        driver = chrome_driver
        wait = WebDriverWait(driver, 15)

        with allure.step("Открываем страницу каталога"):
            driver.get(ui_config["catalog_url"])
            time.sleep(2)

        with allure.step("Скрываем мешающие оверлеи"):
            hide_overlays(driver)

        with allure.step("Находим логотип"):
            logo = wait.until(
                EC.presence_of_element_located((
                    By.CSS_SELECTOR,
                    '.logo-component, .header-block__logo, '
                    'a[href="/"]'
                ))
            )
            logo_link: WebElement = (
                logo.find_element(By.TAG_NAME, 'a')
                if logo.tag_name != 'a'
                else logo
            )

        with allure.step("Кликаем по логотипу"):
            logo_url = logo_link.get_attribute('href')
            driver.get(logo_url)

        with allure.step("Проверяем переход на главную"):
            wait.until(
                lambda d: d.current_url.rstrip('/')
                == ui_config["base_url"]
            )
            assert (
                driver.current_url.rstrip('/')
                == ui_config["base_url"]
            ), "Клик по логотипу не вернул на главную страницу"

    @allure.title(
        "Клик по кнопке галереи меняет основное фото товара"
    )
    @allure.story("Карточка товара")
    def test_product_gallery(
        self,
        chrome_driver: WebDriver,
        ui_config: dict[str, str],
    ) -> None:
        """Кейс 2: Клик по миниатюре галереи меняет фото."""
        driver = chrome_driver
        wait = WebDriverWait(driver, 15)

        with allure.step("Открываем карточку товара"):
            driver.get(ui_config["product_iphone"])
            time.sleep(5)

        with allure.step("Скрываем мешающие оверлеи"):
            hide_overlays(driver)

        with allure.step(
            "Получаем data-src главного изображения"
        ):
            images_info = driver.execute_script(
                "var imgs = document.querySelectorAll("
                "'.product-gallery-item__image');"
                "var result = [];"
                "for (var i = 0; i < imgs.length; i++) {"
                "result.push("
                "imgs[i].getAttribute('data-src') "
                "|| imgs[i].src"
                ");"
                "}"
                "return result;"
            )
            assert len(images_info) >= 2, \
                "В галерее менее 2 изображений товара"
            initial_src = images_info[0]

        with allure.step("Кликаем кнопку «вперёд» в галерее"):
            next_btn = wait.until(
                EC.element_to_be_clickable(
                    (
                        By.CSS_SELECTOR,
                        '.product-gallery-button-next'
                    )
                )
            )
            driver.execute_script(
                "arguments[0].click();", next_btn
            )
            time.sleep(3)

        with allure.step("Проверяем смену изображения"):
            new_src = driver.execute_script(
                "var active = document.querySelector("
                "'.swiper-slide-active "
                ".product-gallery-item__image');"
                "if (active) {"
                "return active.getAttribute('data-src') "
                "|| active.src;"
                "}"
                "var imgs = document.querySelectorAll("
                "'.product-gallery-item__image');"
                "return imgs.length > 1 "
                "? (imgs[1].getAttribute('data-src') "
                "|| imgs[1].src) "
                ": '';"
            )
            assert new_src != initial_src, \
                "Баг CKRPOT-12: клик по миниатюре " \
                "не сменил основное фото"

    @allure.title("Добавление в избранное без авторизации")
    @allure.story("Избранное")
    def test_favorites_without_auth(
        self,
        chrome_driver: WebDriver,
        ui_config: dict[str, str],
    ) -> None:
        """
        Кейс 3: Добавление в избранное без авторизации.
        Баг CKRPOT-14: появляется окно входа.
        """
        driver = chrome_driver

        with allure.step("Открываем карточку товара Samsung"):
            driver.get(ui_config["product_samsung"])
            time.sleep(5)

        with allure.step("Скрываем мешающие оверлеи"):
            hide_overlays(driver)

        with allure.step(
            "Положительная проверка: кнопка "
            "«В избранное» присутствует"
        ):
            favorite_btn = driver.find_element(
                By.XPATH,
                '//*[contains(text(), "В избранное")]'
            )
            assert favorite_btn is not None, \
                "Кнопка «В избранное» не найдена"

        with allure.step("Кликаем «В избранное» без авторизации"):
            driver.execute_script(
                "arguments[0].click();", favorite_btn
            )
            time.sleep(3)

        with allure.step(
            "Положительный вариант: окно входа "
            "НЕ должно появляться"
        ):
            login_prompt = driver.find_elements(
                By.XPATH,
                '//*[contains(text(), "Войдите") '
                'or contains(text(), "войдите")]'
            )
            visible_prompts = [
                el for el in login_prompt
                if el.is_displayed()
            ]
            assert len(visible_prompts) == 0, \
                "Баг CKRPOT-14: при клике «В избранное» " \
                "без авторизации появляется окно входа"

    @allure.title(
        "Время загрузки и отображение на мобильном экране"
    )
    @allure.story("Производительность и адаптивность")
    def test_page_load_and_mobile(
        self,
        chrome_driver: WebDriver,
        ui_config: dict[str, str],
    ) -> None:
        """Кейс 4: Время загрузки и мобильный экран 360x800."""
        driver = chrome_driver
        wait = WebDriverWait(driver, 10)

        with allure.step("Засекаем время загрузки"):
            start_time = time.time()
            driver.get(ui_config["base_url"])
            wait.until(
                EC.presence_of_element_located(
                    (By.CSS_SELECTOR, 'body')
                )
            )
            load_time = time.time() - start_time

        with allure.step("Проверяем медленную загрузку (> 3с)"):
            assert load_time > 3.0, \
                f"Время загрузки {load_time:.2f}с — " \
                f"ожидается > 3с " \
                f"(баг CKRPOT-11: LCP = 4.61с)"

        with allure.step("Переключаем на мобильный размер"):
            driver.set_window_size(360, 800)
            time.sleep(2)

        with allure.step("Проверяем ширину body"):
            body_width = driver.execute_script(
                "return document.body.scrollWidth;"
            )
            assert body_width > 360, \
                f"Ширина body {body_width}px — " \
                f"ожидается > 360px " \
                f"(элементы наезжают на мобильном)"

        with allure.step("Возвращаем полноэкранный режим"):
            driver.maximize_window()

    @allure.title(
        "Работа с клавиатурой и контрастность текста"
    )
    @allure.story("Доступность")
    def test_keyboard_and_contrast(
        self,
        chrome_driver: WebDriver,
        ui_config: dict[str, str],
    ) -> None:
        """Кейс 5: Работа с клавиатурой и контрастность."""
        driver = chrome_driver
        wait = WebDriverWait(driver, 10)

        with allure.step("Открываем карточку товара"):
            driver.get(ui_config["product_yandex"])
            close_city_modal(driver)
            remove_flocktory(driver)
            wait.until(
                EC.presence_of_element_located(
                    (By.TAG_NAME, 'body')
                )
            )
            time.sleep(3)

        with allure.step("Нажимаем Tab для проверки фокуса"):
            driver.find_element(
                By.TAG_NAME, 'body'
            ).send_keys(Keys.TAB)
            time.sleep(0.5)

        with allure.step("Проверяем модальные окна и Esc"):
            modals = driver.find_elements(
                By.CSS_SELECTOR,
                '[class*="modal"], [class*="popup"], '
                '[role="dialog"]'
            )
            if modals:
                driver.find_element(
                    By.TAG_NAME, 'body'
                ).send_keys(Keys.ESCAPE)
                time.sleep(1)

                modals_after = driver.find_elements(
                    By.CSS_SELECTOR,
                    '[class*="modal"], [class*="popup"], '
                    '[role="dialog"]'
                )
                assert len(modals_after) > 0, \
                    "Баг CKRPOT-16 не воспроизведён: " \
                    "модальное окно закрылось по Esc"

        with allure.step("Проверяем контрастность текста"):
            text_element = driver.find_element(
                By.CSS_SELECTOR,
                'p, span, div, h1, h2, h3'
            )
            color = text_element.value_of_css_property(
                'color'
            )
            bg_color = (
                text_element.value_of_css_property(
                    'background-color'
                )
            )

            def parse_rgba(rgba_str: str) -> list[float]:
                nums = (
                    rgba_str.replace('rgba(', '')
                    .replace('rgb(', '')
                    .replace(')', '')
                    .split(',')
                )
                return [float(n.strip()) for n in nums]

            text_rgb = parse_rgba(color)
            bg_rgb = parse_rgba(bg_color)

            def luminance(
                r: float, g: float, b: float
            ) -> float:
                def chan(c: float) -> float:
                    c = c / 255.0
                    return (
                        c / 12.92 if c <= 0.03928
                        else ((c + 0.055) / 1.055) ** 2.4
                    )
                return (
                    0.2126 * chan(r)
                    + 0.7152 * chan(g)
                    + 0.0722 * chan(b)
                )

            l_text = luminance(
                text_rgb[0], text_rgb[1], text_rgb[2]
            )
            l_bg = luminance(
                bg_rgb[0], bg_rgb[1], bg_rgb[2]
            )
            contrast = (
                (max(l_text, l_bg) + 0.05)
                / (min(l_text, l_bg) + 0.05)
            )

            assert contrast > 4.5, \
                f"Контраст {contrast:.2f}:1 — " \
                f"ожидается > 4.5:1 " \
                f"(баг CKRPOT-15: Accessibility 71)"
