from pages.LoginPage import *


def test_login(browser, url):
    login_page = LoginPage(browser)
    login_page.open_page(url + login_page.URL)
    login_page.wait_visibility_find(3, LoginPageLocators.CONTINUE_BTN)
    login_page.wait_clickable_find(3, LoginPageLocators.EMAIL_FIELD)
    login_page.wait_clickable_find(3, LoginPageLocators.PASSWORD_FIELD)
    login_page.wait_clickable_find(3, LoginPageLocators.LOGIN_BTN)
    login_page.wait_visibility_find(3, LoginPageLocators.RIGHT_COLUMN)