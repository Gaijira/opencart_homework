from pages.AdminPage import *
from pages.DashboardPage import *


def test_admin(browser, url):
    admin_page = AdminPage(browser)
    admin_page.open_page(url + AdminPage.URL)
    admin_page.login()
    dashboard_page = DashboardPage(browser)
    dashboard_page.logout()
    admin_page.wait_assert_title(3, 'Administration')


def test_products(browser, url):
    admin_page = AdminPage(browser)
    admin_page.open_page(url + AdminPage.URL)
    admin_page.login()
    dashboard_page = DashboardPage(browser)
    dashboard_page.open_catalog()
    dashboard_page.open_catalog_products()
    dashboard_page.wait_visibility_find(3, DashboardPageLocators.PRODUCT_TABLE)