import pytest
import allure
from lesson_10.utils.factory import create_driver


def pytest_addoption(parser):
    """Регистрирует аргумент --browser для выбора браузера."""
    parser.addoption(
        "--browser",
        action="store",
        default="chrome",
        help="Браузер: chrome, firefox или edge",
    )


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """Прикрепляет скриншот к отчёту Allure при падении."""
    outcome = yield
    rep = outcome.get_result()
    if rep.when == "call" and rep.failed:
        driver = item.funcargs.get("driver")
        if driver:
            allure.attach(
                driver.get_screenshot_as_png(),
                name="screenshot_on_failure",
                attachment_type=allure.attachment_type.PNG,
            )


@pytest.fixture
def driver(request):
    browser_name = request.config.getoption("--browser")
    driver = create_driver(browser_name)
    yield driver
    driver.quit()
