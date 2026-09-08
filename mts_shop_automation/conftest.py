import pytest


@pytest.fixture
def api_config() -> dict[str, str]:
    """Возвращает конфигурацию для API-тестов."""
    return {
        "base_url": "https://api.sales-ninja.me",
        "project_id": "dde84553-62e4-4b17-bd7a-032028797341",
        "shop_base_url": "https://shop.mts.ru",
        "location_id": "7700000000000000000000000",
        "product_id": "733512",
    }


@pytest.fixture
def ui_config() -> dict[str, str]:
    """Возвращает конфигурацию для UI-тестов."""
    return {
        "base_url": "https://shop.mts.ru",
        "catalog_url": "https://shop.mts.ru/catalog/smartfony/",
        "product_iphone": (
            "https://shop.mts.ru/product/"
            "smartfon-apple-iphone-15-128gb-e-sim-sim-rozovyj"
        ),
        "product_samsung": (
            "https://shop.mts.ru/product/"
            "smartfon-samsung-galaxy-a56-8-256-gb-5g"
            "-grafitovyj-a566e"
        ),
        "product_yandex": (
            "https://shop.mts.ru/product/"
            "umnaja-kolonka-jandeks-stantsija-midi-s-zigbee"
            "-seraja"
        ),
    }
