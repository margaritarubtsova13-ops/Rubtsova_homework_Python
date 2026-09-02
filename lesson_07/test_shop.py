from lesson_07.pages.login_page import LoginPage
from lesson_07.pages.inventory_page import InventoryPage
from lesson_07.pages.cart_page import CartPage
from lesson_07.pages.checkout_page import CheckoutPage



def test_shop_checkout(driver):
    login_page = LoginPage(driver)
    login_page.open()
    login_page.enter_username("standard_user")
    login_page.enter_password("secret_sauce")
    login_page.click_login()

    inventory_page = InventoryPage(driver)
    inventory_page.add_item_by_name("Sauce Labs Backpack")
    inventory_page.add_item_by_name("Sauce Labs Bolt T-Shirt")
    inventory_page.add_item_by_name("Sauce Labs Onesie")
    inventory_page.go_to_cart()

    cart_page = CartPage(driver)
    cart_page.click_checkout()

    checkout_page = CheckoutPage(driver)
    checkout_page.fill_form("Иван", "Петров", "123456")
    checkout_page.click_continue()
    total = checkout_page.get_total()

    assert "$58.29" in total
