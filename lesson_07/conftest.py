import pytest
from lesson_07.utils.factory import create_driver


def pytest_addoption(parser):
    parser.addoption(
        "--browser",
        action="store",
        default="firefox",
        help="Браузер для запуска: firefox, chrome или edge"
    )


@pytest.fixture
def driver(request):
    browser = request.config.getoption("--browser")
    driver = create_driver(browser)
    yield driver
    driver.quit()
