from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def create_driver(browser_name):
    """Создает и возвращает экземпляр драйвера."""
    if browser_name.lower() == "firefox":
        return webdriver.Firefox()
    elif browser_name.lower() == "edge":
        return webdriver.Edge()
    else:
        options = Options()
        prefs = {
            "credentials_enable_service": False,
            "profile.password_manager_enabled": False,
            "profile.password_manager_leak_detection": False,
        }
        options.add_experimental_option("prefs", prefs)
        options.add_argument("--disable-notifications")
        return webdriver.Chrome(options=options)
