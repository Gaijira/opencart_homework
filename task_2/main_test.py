from pages.MainPage import *
from pages.Common import *
import allure


def test_index(browser, url):
    main_page = MainPage(browser)
    with allure.step("Открываем главную страницу"):
        main_page.open_page(url)
    with allure.step("Проверяем наличие кнопки корзины"):
        main_page.wait_visibility_find(3, CommonLocators.CART_BTN)
    with allure.step("Открываем наличие нав бара"):
        main_page.wait_visibility_find(3, CommonLocators.NAV_BAR)
    with allure.step("Открываем наличие сёрч поля"):
        main_page.wait_clickable_find(3, CommonLocators.SEARCH_FIELD)
    with allure.step("Открываем наличие лого"):
        main_page.wait_visibility_find(3, CommonLocators.LOGO)
    with allure.step("Открываем наличие слайдера"):
        main_page.wait_visibility_find(3, MainPageLocators.SLIDER)

