from pages.DesktopsPage import *


def test_desktop(browser, url):
    desktops_page = DesktopsPage(browser)
    desktops_page.open_page(url + DesktopsPage.URL)
    desktops_page.wait_visibility_find(2, DesktopsPageLocators.BREADCRUMBS_COMPONENT)
    desktops_page.wait_visibility_find(2, DesktopsPageLocators.LEFT_FILTER_COLUMN)
    desktops_page.wait_visibility_find(3, DesktopsPageLocators.LEFT_IMG)
    desktops_page.wait_visibility_find(2, DesktopsPageLocators.LIST_VIEW_BTN)
    desktops_page.wait_visibility_find(2, DesktopsPageLocators.GRID_VIEW_BTN)
