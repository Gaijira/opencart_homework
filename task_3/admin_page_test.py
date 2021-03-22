from pages.AdminPage import *
from pages.DashboardPage import *
import allure


def test_admin_login(browser, url):
    admin_page = AdminPage(browser)
    with allure.step("Открываем админ страницу"):
        admin_page.open_page(url + AdminPage.URL)
    with allure.step("Логинимся в дэшборд"):
        admin_page.login()
    dashboard_page = DashboardPage(browser)
    with allure.step("Разлогиниваемся"):
        dashboard_page.logout()
    with allure.step("Проверяем тайтл страницы"):
        admin_page.wait_assert_title(3, 'Administration')


def test_products(browser, url):
    admin_page = AdminPage(browser)
    with allure.step("Открываем админ страницу"):
        admin_page.open_page(url + AdminPage.URL)
    with allure.step("Логинимся в дэшборд"):
        admin_page.login()
    dashboard_page = DashboardPage(browser)
    with allure.step("Открываем каталог"):
        dashboard_page.open_catalog()
    with allure.step("Открываем продукты"):
        dashboard_page.open_catalog_products()
    with allure.step("Проверяем таблицу с продуктами"):
        dashboard_page.wait_visibility_find(3, DashboardPageLocators.PRODUCT_TABLE)
