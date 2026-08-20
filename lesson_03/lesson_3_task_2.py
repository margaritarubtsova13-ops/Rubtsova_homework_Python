from smartphone import Smartphone

catalog = [
    Smartphone("Samsung", "Galaxy S23", "+79001112233"),
    Smartphone("Apple", "iPhone 15", "+79004445566"),
    Smartphone("Xiaomi", "Redmi Note 12", "+79007778899"),
    Smartphone("Google", "Pixel 8", "+79001234567"),
    Smartphone("OnePlus", "11", "+79009876543"),
]

for phone in catalog:
    print(phone.get_catalog_line())
