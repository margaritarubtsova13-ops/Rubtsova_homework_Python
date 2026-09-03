import allure
from lesson_10.pages.login_page import LoginPage
from lesson_10.pages.inventory_page import InventoryPage
from lesson_10.pages.cart_page import CartPage
from lesson_10.pages.checkout_page import CheckoutPage


@allure.title(
    "Тест: Оформление заказа — добавление товаров "
    "и проверка итоговой суммы"
)
@allure.description(
    "Проверяется полный сценарий оформления заказа: авторизация, "
    "добавление трёх товаров, переход в корзину, заполнение формы "
    "и проверка итоговой стоимости."
)
@allure.feature("Оформление заказа")
@allure.severity(allure.severity_level.CRITICAL)
def test_shop_checkout(driver):
    login_page = LoginPage(driver)
    inventory_page = InventoryPage(driver)
    cart_page = CartPage(driver)
    checkout_page = CheckoutPage(driver)

    with allure.step("Авторизуемся в системе"):
        login_page.open()
        login_page.enter_username("standard_user")
        login_page.enter_password("secret_sauce")
        login_page.click_login()

    items = [
        "Sauce Labs Backpack",
        "Sauce Labs Bolt T-Shirt",
        "Sauce Labs Onesie",
    ]
    with allure.step(f"Добавляем товары в корзину: {', '.join(items)}"):
        for item in items:
            inventory_page.add_item_by_name(item)

    with allure.step("Переходим в корзину и нажимаем «Оформить заказ»"):
        inventory_page.go_to_cart()
        cart_page.click_checkout()

    with allure.step("Заполняем форму оформления заказа"):
        checkout_page.fill_form("Иван", "Петров", "123456")
        checkout_page.click_continue()

    with allure.step("Проверяем итоговую сумму заказа"):
        total = checkout_page.get_total()
        assert "$58.29" in total, (
            f"Ожидалась сумма $58.29, но получено: {total}"
        )
