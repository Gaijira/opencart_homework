from selenium.webdriver.common.by import By
from pages.BasePage import *


class DashboardPageLocators:
    LOGOUT_BTN = (By.XPATH, '//*[@id="header"]/div/ul/li[2]/a')
    CATALOG_BTN = (By.LINK_TEXT, 'Catalog')
    PRODUCTS_BTN = (By.LINK_TEXT, 'Products')
    PRODUCT_TABLE = (By.CLASS_NAME, 'panel-body')


class DashboardPage(BasePage):
    def open_catalog(self):
        return self.wait_clickable_find(3, DashboardPageLocators.CATALOG_BTN).click()

    def open_catalog_products(self):
        return self.wait_clickable_find(3, DashboardPageLocators.PRODUCTS_BTN).click()

    def logout(self):
        return self.wait_clickable_find(3, DashboardPageLocators.LOGOUT_BTN).click()
