from pages.DesktopsPage import *
import allure


def test_desktop(browser, url):
    desktops_page = DesktopsPage(browser)
    with allure.step("Открываем  страницу с товаром"):
        desktops_page.open_page(url + DesktopsPage.URL)
    with allure.step("Проверяем наличие нав цепочки"):
        desktops_page.wait_visibility_find(2, DesktopsPageLocators.BREADCRUMBS_COMPONENT)
    with allure.step("Проверяем наличие фильтр элемента"):
        desktops_page.wait_visibility_find(2, DesktopsPageLocators.LEFT_FILTER_COLUMN)
    with allure.step("Проверяем наличие картинки товра"):
        desktops_page.wait_visibility_find(3, DesktopsPageLocators.LEFT_IMG)
    with allure.step("Проверяем наличие лист вью кнопки"):
        desktops_page.wait_visibility_find(2, DesktopsPageLocators.LIST_VIEW_BTN)
    with allure.step("Проверяем наличие грид вью кнопки"):
        desktops_page.wait_visibility_find(2, DesktopsPageLocators.GRID_VIEW_BTN)
