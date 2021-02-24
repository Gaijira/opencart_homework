from pages.ProductPage import *


def test_product(browser, url):
    product_page = ProductPage(browser)
    product_page.open_page(url + ProductPage.URL)
    product_page.wait_visibility_find(3, ProductPageLocators.MAIN_IMG)
    product_page.wait_visibility_find(3, ProductPageLocators.IMG_1)
    product_page.wait_visibility_find(3, ProductPageLocators.COMPARE_BTN)
    product_page.wait_visibility_find(3, ProductPageLocators.CART_ADD_BTN)
    product_page.wait_visibility_find(3, ProductPageLocators.REVIEWS_BTN)
