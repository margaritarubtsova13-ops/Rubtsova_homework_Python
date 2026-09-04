import requests

BASE_URL = "https://ru.yougile.com/api-v2"
LOGIN = "margarita.rubtsova13@gmail.com"
PASSWORD = ""  # <-- ВСТАВЬ СВОЙ ПАРОЛЬ

print(f"🔍 Авторизация: {LOGIN}")

# Шаг 1: Получаем компании
resp_companies = requests.post(
    f"{BASE_URL}/auth/companies",
    json={"login": LOGIN, "password": PASSWORD},
    timeout=10
)

print(f"📡 Статус: {resp_companies.status_code}")

if resp_companies.status_code != 200:
    print(f"❌ Ошибка: {resp_companies.text}")
    exit()

data = resp_companies.json()

# Сервер возвращает пагинацию: {count, content: [...], ...}
content = data.get("content", [])

if not content:
    # Возможно, структура другая — попробуем как список
    if isinstance(data, list):
        content = data
    else:
        print(f"⚠️ Не удалось найти компании. Ответ: {data}")
        exit()

company_id = content[0]["id"]
print(f"✅ Company ID: {company_id}")

# Шаг 2: Получаем ключи
resp_keys = requests.post(
    f"{BASE_URL}/auth/keys/get",
    json={
        "login": LOGIN,
        "password": PASSWORD,
        "companyId": company_id
    },
    timeout=10
)

print(f"📡 Статус ключей: {resp_keys.status_code}")

if resp_keys.status_code != 200:
    print(f"❌ Ошибка: {resp_keys.text}")
    exit()

keys_data = resp_keys.json()
keys = keys_data.get("content", keys_data) if isinstance(keys_data, dict) else keys_data

print("\n🔑 Ключи:")
active_key = None

for k in keys:
    deleted = k.get("deleted", False)
    status = "✅ АКТИВЕН" if not deleted else "❌ УДАЛЁН"
    print(f"{status} | {k['key'][:20]}...")
    if not deleted and active_key is None:
        active_key = k["key"]

if active_key:
    print(f"\n🎉 АКТИВНЫЙ КЛЮЧ:\n{active_key}")
else:
    print("\n⚠️ Активных ключей нет.")
