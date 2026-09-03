import requests

BASE_URL = "https://ru.yougile.com/api-v2"
LOGIN = "margarita.rubtsova13@gmail.com"
PASSWORD = ""  # <-- ВСТАВЬ СВОЙ ПАРОЛЬ

print("🔍 Шаг 1: Получаем company_id")
r_companies = requests.post(
    f"{BASE_URL}/auth/companies",
    json={"login": LOGIN, "password": PASSWORD},
    timeout=10
)

if r_companies.status_code != 200:
    print(f"❌ Ошибка: {r_companies.status_code} {r_companies.text}")
    exit()

content = r_companies.json().get("content", [])
if not content:
    print("⚠️ Не удалось найти company_id")
    exit()
company_id = content[0]["id"]
print(f"✅ Company ID: {company_id}")

print("\n🔑 Шаг 2: Создаём новый ключ")
r_create = requests.post(
    f"{BASE_URL}/auth/keys",
    json={
        "login": LOGIN,
        "password": PASSWORD,
        "companyId": company_id
    },
    timeout=10
)

if r_create.status_code == 200:
    result = r_create.json()
    key = result.get("key")
    if key:
        print(f"\n🎉 НОВЫЙ КЛЮЧ:\n{key}")
        print(f"Длина: {len(key)} символов")
    else:
        print("⚠️ Ключ не найден в ответе:", result)
else:
    print(f"❌ Ошибка: {r_create.status_code} {r_create.text}")
