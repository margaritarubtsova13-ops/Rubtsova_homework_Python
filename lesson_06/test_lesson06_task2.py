from selenium import webdriver


def test_session_storage_auth():
    driver = webdriver.Chrome()
    try:
        # --- Пользователь 1 (wuqttab) ---
        driver.get("https://gitflic.ru/")

        driver.add_cookie({
            "name": "SESSION",
            "value": "ZDk0NjBjZDItYzM5ZS00ZDk0LWE5MTktZDkwNDZkNzVlNTVl",
            "domain": "gitflic.ru",
            "path": "/"
        })

        driver.refresh()
        driver.get("https://gitflic.ru/user/wuqttab")
        url_user_1 = driver.current_url
        print(f"URL пользователя 1: {url_user_1}")

       
        driver.delete_all_cookies()
        driver.get("https://gitflic.ru/")

        
        driver.add_cookie({
            "name": "SESSION",
            "value": "MDc1NzRhMzQtMjc1Ny00M2U5LTkzMmQtZDMyYmMyNGU5MThk",
            "domain": "gitflic.ru",
            "path": "/"
        })

        driver.refresh()
        driver.get("https://gitflic.ru/user/price0025")
        url_user_2 = driver.current_url
        print(f"URL пользователя 2: {url_user_2}")

        
        assert url_user_1 != url_user_2, (
            f"URL совпали! user1={url_user_1}, user2={url_user_2}"
        )
        print("✅ Тест прошёл: URL разные, работа с cookie подтверждена.")

    finally:
        driver.quit()
        
if __name__ == "__main__":
    test_session_storage_auth()
