from pages.AdminPage import *


def test_admin(browser, url):
    admin_page = AdminPage(browser)
    admin_page.open_page(url + AdminPage.URL)
    admin_page.wait_clickable_find(3, AdminPageLocators.USERNAME_FIELD)
    admin_page.wait_clickable_find(3, AdminPageLocators.PASSWORD_FIELD)
    admin_page.wait_clickable_find(3, AdminPageLocators.FORGOT_PASSWORD_LINK)
    admin_page.wait_clickable_find(3, AdminPageLocators.LOGIN_BTN)
    admin_page.wait_visibility_find(3, AdminPageLocators.LOGO)
