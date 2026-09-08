import allure
import pytest
import requests


@pytest.mark.api
class TestAPITests:
    """API-тесты для эндпоинта modeled-conversion."""

    @allure.title("Отправка события с неверным Content-Type")
    @allure.story("Валидация запросов")
    def test_wrong_content_type(
        self, api_config: dict[str, str]
    ) -> None:
        """
        Кейс 1: Content-Type: application/json —
        неверный для данного эндпоинта.
        """
        with allure.step("Формируем URL и параметры"):
            url = (
                f"{api_config['base_url']}"
                "/bundle/v2/modeled-conversion"
            )
            params = {"projectId": api_config['project_id']}
            headers = {"Content-Type": "application/json"}

        with allure.step("Отправляем POST с пустым телом"):
            response = requests.post(
                url, data="", headers=headers, params=params
            )

        with allure.step("Проверяем статус 415"):
            assert response.status_code == 415, \
                f"Ожидался 415, получен {response.status_code}. " \
                f"Ответ: {response.text}"

    @allure.title("Отправка события с мусорным телом")
    @allure.story("Валидация запросов")
    def test_garbage_body(
        self, api_config: dict[str, str]
    ) -> None:
        """
        Кейс 2: В теле строка 'f;dgnadbn' вместо JSON.
        """
        with allure.step("Формируем URL и параметры"):
            url = (
                f"{api_config['base_url']}"
                "/bundle/v2/modeled-conversion"
            )
            params = {"projectId": api_config['project_id']}
            headers = {"Content-Type": "application/json"}

        with allure.step("Отправляем POST с мусорным телом"):
            garbage = "f;dgnadbn"
            response = requests.post(
                url, data=garbage, headers=headers, params=params
            )

        with allure.step("Проверяем статус 415"):
            assert response.status_code == 415, \
                f"Ожидался 415, получен {response.status_code}. " \
                f"Ответ: {response.text}"

    @allure.title("Отправка события без projectId в query")
    @allure.story("Авторизация и доступ")
    def test_missing_project_id(
        self, api_config: dict[str, str]
    ) -> None:
        """
        Кейс 3: POST без параметра projectId.
        """
        with allure.step("Формируем URL без projectId"):
            url = (
                f"{api_config['base_url']}"
                "/bundle/v2/modeled-conversion"
            )

        with allure.step("Отправляем POST без параметров"):
            response = requests.post(url)

        with allure.step("Проверяем статус 403"):
            assert response.status_code == 403, \
                f"Ожидался 403, получен {response.status_code}. " \
                f"Ответ: {response.text}"

        with allure.step("Проверяем текст 'Project was suspended'"):
            assert "Project was suspended" in response.text, \
                f"Ожидается 'Project was suspended', " \
                f"получено: {response.text}"

    @allure.title("Отправка запроса с пустым телом")
    @allure.story("Валидация запросов")
    def test_empty_body(
        self, api_config: dict[str, str]
    ) -> None:
        """
        Кейс 4: POST с projectId, но без тела.
        """
        with allure.step("Формируем URL и параметры"):
            url = (
                f"{api_config['base_url']}"
                "/bundle/v2/modeled-conversion"
            )
            params = {"projectId": api_config['project_id']}

        with allure.step("Отправляем POST без тела"):
            response = requests.post(url, params=params)

        with allure.step("Проверяем статус 400"):
            assert response.status_code == 400, \
                f"Ожидался 400 для пустого тела, " \
                f"получен {response.status_code}. " \
                f"Ответ: {response.text}"

    @allure.title("Использование неверного HTTP-метода")
    @allure.story("Валидация запросов")
    def test_wrong_http_method(
        self, api_config: dict[str, str]
    ) -> None:
        """
        Кейс 5: GET вместо POST.
        """
        with allure.step("Формируем URL и параметры"):
            url = (
                f"{api_config['base_url']}"
                "/bundle/v2/modeled-conversion"
            )
            params = {"projectId": api_config['project_id']}

        with allure.step("Отправляем GET вместо POST"):
            response = requests.get(url, params=params)

        with allure.step("Проверяем статус 405"):
            assert response.status_code == 405, \
                f"Ожидался 405 для неверного метода, " \
                f"получен {response.status_code}. " \
                f"Ответ: {response.text}"
