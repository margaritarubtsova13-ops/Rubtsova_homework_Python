import requests

BASE_URL = "https://ru.yougile.com/api-v2"
LOGIN = "margarita.rubtsova13@gmail.com"
PASSWORD = ""  # <-- ВСТАВЬ СВОЙ ПАРОЛЬ

# Шаг 1: Получаем company_id
print("🔍 Получаем company_id...")
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
    print("⚠️ Компании не найдены")
    exit()

company_id = content[0]["id"]
print(f"✅ Company ID: {company_id}")

# Шаг 2: Получаем список ключей
print("\n🔑 Получаем список ключей...")
r_keys = requests.post(
    f"{BASE_URL}/auth/keys/get",
    json={
        "login": LOGIN,
        "password": PASSWORD,
        "companyId": company_id
    },
    timeout=10
)

if r_keys.status_code != 200:
    print(f"❌ Ошибка: {r_keys.status_code} {r_keys.text}")
    exit()

keys = r_keys.json()
content_keys = keys.get("content", keys) if isinstance(keys, dict) else keys

if not content_keys:
    print("⚠️ Ключей не найдено")
    exit()

print(f"Найдено ключей: {len(content_keys)}")

# Шаг 3: Удаляем все активные ключи
for k in content_keys:
    key_value = k.get("key")
    is_deleted = k.get("deleted", False)
    
    if is_deleted:
        print(f"  ⏭️ Уже удалён: {key_value[:20]}...")
        continue
    
    print(f"  🗑️ Удаляем ключ: {key_value[:20]}...")
    
    r_delete = requests.delete(
        f"{BASE_URL}/auth/keys/{key_value}",
        headers={
            "Authorization": f"Bearer {key_value}",
            "Content-Type": "application/json"
        },
        timeout=10
    )
    
    if r_delete.status_code == 200:
        print(f"  ✅ Ключ удалён!")
    else:
        print(f"  ❌ Ошибка удаления: {r_delete.status_code} {r_delete.text}")

print("\n🎉 Готово! Все активные ключи отозваны.")
