from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CartPage:
    """Страница корзины в демо-магазине."""

    def __init__(self, driver) -> None:
        """
        Инициализация страницы корзины.

        :param driver: Экземпляр WebDriver.
        :type driver: selenium.webdriver.remote.webdriver.WebDriver
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, 30)

    def click_checkout(self) -> "CartPage":
        """
        Нажимает кнопку оформления заказа.

        :return: Текущий экземпляр страницы.
        :rtype: CartPage
        """
        button = self.wait.until(
            EC.element_to_be_clickable((By.ID, "checkout"))
        )
        button.click()
        return self
