from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CalculatorPage:
    """Страница медленного калькулятора (BoniGarcia demo)."""

    def __init__(self, driver) -> None:
        """
        Инициализация страницы.

        :param driver: Экземпляр WebDriver.
        :type driver: selenium.webdriver.remote.webdriver.WebDriver
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, 60)
        self.url = (
            "https://bonigarcia.dev/selenium-webdriver-java/"
            "slow-calculator.html"
        )

    def open(self) -> "CalculatorPage":
        """
        Открывает страницу калькулятора.

        :return: Текущий экземпляр страницы.
        :rtype: CalculatorPage
        """
        self.driver.get(self.url)
        return self

    def set_delay(self, seconds: int) -> "CalculatorPage":
        """
        Устанавливает задержку калькулятора.

        :param seconds: Значение задержки в секундах.
        :type seconds: int
        :return: Текущий экземпляр страницы.
        :rtype: CalculatorPage
        """
        delay_input = self.wait.until(
            EC.presence_of_element_located((By.ID, "delay"))
        )
        delay_input.clear()
        delay_input.send_keys(str(seconds))
        return self

    def click_button(self, label: str) -> "CalculatorPage":
        """
        Нажимает кнопку с указанным текстом.

        :param label: Текст кнопки (например, '7', '+', '=').
        :type label: str
        :return: Текущий экземпляр страницы.
        :rtype: CalculatorPage
        """
        locator = (
            By.XPATH,
            f"//span[contains(@class,'btn') "
            f"and text()='{label}']"
        )
        btn = self.wait.until(EC.element_to_be_clickable(locator))
        btn.click()
        return self

    def get_result(self) -> str:
        """
        Получает текст результата из экрана калькулятора.
        Ожидает завершения вычисления — пока с экрана
        не исчезнет символ операции.

        :return: Текст результата (очищенный от лишних пробелов).
        :rtype: str
        """
        screen = self.driver.find_element(
            By.CLASS_NAME, "screen"
        )
        self.wait.until(
            lambda d: screen.text.strip() != ""
            and "+" not in screen.text
        )
        return screen.text.strip()
