import requests
import config

print("=== ПРОВЕРКА ТОКЕНА ===")
print(f"BASE_URL: {config.BASE_URL}")
print(f"TOKEN (первые 10 символов): {config.TOKEN[:10]}...")
print(f"HEADER Authorization: {config.HEADERS['Authorization'][:30]}...")
print()

# Пробуем с Bearer
print(">>> Тест 1: с префиксом Bearer")
headers_bearer = {
    "Authorization": f"Bearer {config.TOKEN}",
    "Content-Type": "application/json"
}
r1 = requests.get(f"{config.BASE_URL}/projects", headers=headers_bearer)
print(f"    Статус: {r1.status_code}")
print(f"    Ответ: {r1.text[:200]}")
print()

# Пробуем без Bearer (просто ключ)
print(">>> Тест 2: без префикса Bearer")
headers_plain = {
    "Authorization": config.TOKEN,
    "Content-Type": "application/json"
}
r2 = requests.get(f"{config.BASE_URL}/projects", headers=headers_plain)
print(f"    Статус: {r2.status_code}")
print(f"    Ответ: {r2.text[:200]}")
print()

# Пробуем через X-Auth-Key (иногда Yougile использует этот заголовок)
print(">>> Тест 3: через заголовок X-Auth-Key")
headers_xauth = {
    "X-Auth-Key": config.TOKEN,
    "Content-Type": "application/json"
}
r3 = requests.get(f"{config.BASE_URL}/projects", headers=headers_xauth)
print(f"    Статус: {r3.status_code}")
print(f"    Ответ: {r3.text[:200]}")

print(len(config.TOKEN))