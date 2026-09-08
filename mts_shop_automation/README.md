# Автоматизация тестирования МТС Shop

## Описание проекта

Проект автоматизации тестирования интернет-магазина МТС Shop с использованием pytest и Selenium.

## Структура проекта

mts_shop_automation/
├── test/
│   ├── test_api.py      # 5 API тестов
│   └── test_ui.py       # 5 UI тестов
├── conftest.py          # Фикстуры и конфигурация
├── utils/
│   └── helpers.py       # Вспомогательные функции
├── requirements.txt     # Зависимости проекта
└── README.md            # Документация

## Запуск тестов

### Все тесты
pytest -v

### Только API тесты
pytest -m api -v

### Только UI тесты
pytest -m ui -v

### Запуск конкретного теста
pytest test/test_ui.py::TestUITests::test_logo_click

### Генерация Allure отчёта
pytest -v --alluredir=allure-results
allure serve allure-results

## Таблица тестов

### API тесты
№ | Название | Проверка
--- | --- | ---
1 | test_valid_price | Получение цены товара
2 | test_invalid_product_id | Обработка несуществующего ID
3 | test_missing_location | Обязательность локации
4 | test_product_search | Поиск товаров
5 | test_empty_cart | Пустая корзина

### UI тесты
№ | Название | Проверка
--- | --- | ---
1 | test_logo_click | Клик по логотипу возвращает на главную
2 | test_product_gallery | Кнопка галереи меняет основное фото
3 | test_favorites_without_auth | Добавление в избранное без авторизации
4 | test_page_load_and_mobile | Время загрузки и мобильный экран 360x800
5 | test_keyboard_and_contrast | Работа с клавиатурой и контрастность текста
