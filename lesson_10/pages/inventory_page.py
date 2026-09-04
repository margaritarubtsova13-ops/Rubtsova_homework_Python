from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class InventoryPage:
    """Страница каталога товаров в демо-магазине."""

    def __init__(self, driver) -> None:
        """
        Инициализация страницы каталога.

        :param driver: Экземпляр WebDriver.
        :type driver: selenium.webdriver.remote.webdriver.WebDriver
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, 30)

    def add_item_by_name(self, item_name: str) -> "InventoryPage":
        """
        Добавляет товар в корзину по имени.

        :param item_name: Название товара
            (например, «Sauce Labs Backpack»).
        :type item_name: str
        :return: Текущий экземпляр страницы.
        :rtype: InventoryPage
        """
        item_id = (
            "add-to-cart-"
            + item_name.lower().replace(" ", "-")
        )
        button = self.wait.until(
            EC.element_to_be_clickable((By.ID, item_id))
        )
        button.click()
        return self

    def go_to_cart(self) -> "InventoryPage":
        """
        Переходит в корзину и дожидается загрузки страницы.

        :return: Текущий экземпляр страницы.
        :rtype: InventoryPage
        """
        cart_link = self.wait.until(
            EC.element_to_be_clickable(
                (By.CLASS_NAME, "shopping_cart_link")
            )
        )
        cart_link.click()
        self.wait.until(EC.url_contains("cart"))
        return self
