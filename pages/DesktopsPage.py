from pages.BasePage import BasePage
from selenium.webdriver.common.by import By


class DesktopsPageLocators:
    BREADCRUMBS_COMPONENT = (By.CSS_SELECTOR, '#product-category > ul')
    LEFT_FILTER_COLUMN = (By.CSS_SELECTOR, '#column-left > div.list-group')
    LEFT_IMG = (By.CSS_SELECTOR, '#banner0 > div > div > a > img')
    LIST_VIEW_BTN = (By.CSS_SELECTOR, '#list-view')
    GRID_VIEW_BTN = (By.CSS_SELECTOR, '#grid-view')


class DesktopsPage(BasePage):
    URL = '?route=product/category&path=20'
