from pages.MainPage import *
from pages.Common import *


def test_index(browser, url):
    main_page = MainPage(browser)
    main_page.open_page(url)
    main_page.wait_visibility_find(3, CommonLocators.CART_BTN)
    main_page.wait_visibility_find(3, CommonLocators.NAV_BAR)
    main_page.wait_clickable_find(3, CommonLocators.SEARCH_FIELD)
    main_page.wait_visibility_find(3, CommonLocators.LOGO)
    main_page.wait_visibility_find(3, MainPageLocators.SLIDER)
