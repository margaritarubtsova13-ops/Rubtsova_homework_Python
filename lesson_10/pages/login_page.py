from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:
    """Страница авторизации в демо-магазине."""
    URL = "https://www.saucedemo.com/"

    def __init__(self, driver) -> None:
        """
        Инициализация страницы входа.

        :param driver: Экземпляр WebDriver.
        :type driver: selenium.webdriver.remote.webdriver.WebDriver
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open(self) -> "LoginPage":
        """
        Открывает страницу входа.

        :return: Текущий экземпляр страницы.
        :rtype: LoginPage
        """
        self.driver.get(self.URL)
        return self

    def enter_username(self, username: str) -> "LoginPage":
        """
        Вводит имя пользователя.

        :param username: Логин пользователя.
        :type username: str
        :return: Текущий экземпляр страницы.
        :rtype: LoginPage
        """
        field = self.wait.until(
            EC.presence_of_element_located((By.ID, "user-name"))
        )
        field.clear()
        field.send_keys(username)
        return self

    def enter_password(self, password: str) -> "LoginPage":
        """
        Вводит пароль.

        :param password: Пароль пользователя.
        :type password: str
        :return: Текущий экземпляр страницы.
        :rtype: LoginPage
        """
        field = self.wait.until(
            EC.presence_of_element_located((By.ID, "password"))
        )
        field.clear()
        field.send_keys(password)
        return self

    def click_login(self) -> "LoginPage":
        """
        Нажимает кнопку входа.

        :return: Текущий экземпляр страницы.
        :rtype: LoginPage
        """
        button = self.wait.until(
            EC.element_to_be_clickable((By.ID, "login-button"))
        )
        button.click()
        return self
