from pages.LoginPage import *
import allure

def test_login(browser, url):
    login_page = LoginPage(browser)
    with allure.step("Открываем страницу логина"):
        login_page.open_page(url + login_page.URL)
    with allure.step("Проверяем наличие continue кнопки"):
        login_page.wait_visibility_find(3, LoginPageLocators.CONTINUE_BTN)
    with allure.step("Проверяем наличие email поля"):
        login_page.wait_clickable_find(3, LoginPageLocators.EMAIL_FIELD)
    with allure.step("Проверяем наличие password поля"):
        login_page.wait_clickable_find(3, LoginPageLocators.PASSWORD_FIELD)
    with allure.step("Проверяем наличие password поля"):
        login_page.wait_clickable_find(3, LoginPageLocators.LOGIN_BTN)
    with allure.step("Проверяем наличие правой колонки"):
        login_page.wait_visibility_find(3, LoginPageLocators.RIGHT_COLUMN)
