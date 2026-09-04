import allure
from lesson_10.pages.calculator_page import CalculatorPage


@allure.title("Тест: Медленный калькулятор — проверка сложения 7 + 8")
@allure.description(
    "Проверяется корректность работы медленного калькулятора: "
    "установка задержки, ввод выражения и получение результата."
)
@allure.feature("Калькулятор")
@allure.severity(allure.severity_level.NORMAL)
def test_slow_calculator(driver):
    page = CalculatorPage(driver)

    with allure.step("Открываем страницу калькулятора"):
        page.open()

    with allure.step("Устанавливаем задержку 25 секунд"):
        page.set_delay(25)

    buttons = ["7", "+", "8", "="]
    with allure.step(f"Нажимаем кнопки: {', '.join(buttons)}"):
        for label in buttons:
            page.click_button(label)

    with allure.step("Получаем результат из экрана калькулятора"):
        result = page.get_result()

    with allure.step(
        "Проверяем, что результат соответствует "
        "ожидаемому выражению"
    ):
        assert result == "15", (
            f"Ожидалось '15', но получено: '{result}'"
        )
