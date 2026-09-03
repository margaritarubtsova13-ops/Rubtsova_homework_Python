from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CheckoutPage:
    """Страница оформления заказа в демо-магазине."""

    def __init__(self, driver) -> None:
        """
        Инициализация страницы оформления заказа.

        :param driver: Экземпляр WebDriver.
        :type driver: selenium.webdriver.remote.webdriver.WebDriver
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def fill_form(
        self,
        first_name: str,
        last_name: str,
        postal_code: str,
    ) -> "CheckoutPage":
        """
        Заполняет форму оформления заказа.

        :param first_name: Имя покупателя.
        :type first_name: str
        :param last_name: Фамилия покупателя.
        :type last_name: str
        :param postal_code: Почтовый индекс.
        :type postal_code: str
        :return: Текущий экземпляр страницы.
        :rtype: CheckoutPage
        """
        fn = self.wait.until(
            EC.presence_of_element_located((By.ID, "first-name"))
        )
        fn.clear()
        fn.send_keys(first_name)

        ln = self.wait.until(
            EC.presence_of_element_located((By.ID, "last-name"))
        )
        ln.clear()
        ln.send_keys(last_name)

        pc = self.wait.until(
            EC.presence_of_element_located((By.ID, "postal-code"))
        )
        pc.clear()
        pc.send_keys(postal_code)
        return self

    def click_continue(self) -> "CheckoutPage":
        """
        Нажимает кнопку «Продолжить».

        :return: Текущий экземпляр страницы.
        :rtype: CheckoutPage
        """
        button = self.wait.until(
            EC.element_to_be_clickable((By.ID, "continue"))
        )
        button.click()
        return self

    def get_total(self) -> str:
        """
        Получает итоговую сумму заказа.

        :return: Строка с итоговой суммой.
        :rtype: str
        """
        total = self.wait.until(
            EC.visibility_of_element_located(
                (By.CLASS_NAME, "summary_total_label")
            )
        )
        return total.text
