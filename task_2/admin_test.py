from pages.AdminPage import *
import allure
import allure


def test_admin_page(browser, url):
    admin_page = AdminPage(browser)
    with allure.step("Открываем  админ страницу"):
        admin_page.open_page(url + AdminPage.URL)
    with allure.step("Проверяем наличие username поля"):
        admin_page.wait_clickable_find(3, AdminPageLocators.USERNAME_FIELD)
    with allure.step("Проверяем наличие password поля"):
        admin_page.wait_clickable_find(3, AdminPageLocators.PASSWORD_FIELD)
    with allure.step("Проверяем наличие forgot password линки"):
        admin_page.wait_clickable_find(3, AdminPageLocators.FORGOT_PASSWORD_LINK)
    with allure.step("Проверяем наличие логин кнопки"):
        admin_page.wait_clickable_find(3, AdminPageLocators.LOGIN_BTN)
    with allure.step("Открываем  наличе лого"):
        admin_page.wait_visibility_find(3, AdminPageLocators.LOGO)
