from pages.ProductPage import *
import allure


def test_product(browser, url):
    product_page = ProductPage(browser)
    with allure.step("Открываем страницу продукта"):
        product_page.open_page(url + ProductPage.URL)
    with allure.step("Проверяем наличие картинки товара"):
        product_page.wait_visibility_find(3, ProductPageLocators.MAIN_IMG)
    with allure.step("Проверяем наличие 1 картинки под основной"):
        product_page.wait_visibility_find(3, ProductPageLocators.IMG_1)
    with allure.step("Проверяем наличие compare кнопки"):
        product_page.wait_visibility_find(3, ProductPageLocators.COMPARE_BTN)
    with allure.step("Проверяем наличие add to cart кнопки"):
        product_page.wait_visibility_find(3, ProductPageLocators.CART_ADD_BTN)
    with allure.step("Проверяем наличие reviews кнопки"):
        product_page.wait_visibility_find(3, ProductPageLocators.REVIEWS_BTN)
