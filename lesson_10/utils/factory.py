from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.edge.options import Options as EdgeOptions

def create_driver(browser: str):
    browser = browser.lower()
    if browser == "chrome":
        options = ChromeOptions()
        return webdriver.Chrome(options=options)
    elif browser == "firefox":
        options = FirefoxOptions()
        return webdriver.Firefox(options=options)
    elif browser == "edge":
        options = EdgeOptions()
        return webdriver.Edge(options=options)
    else:
        raise ValueError(f"Неизвестный браузер: {browser}")
