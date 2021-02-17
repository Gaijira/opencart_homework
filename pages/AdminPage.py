from selenium.webdriver.common.by import By
from pages.BasePage import *


class AdminPageLocators:
    USERNAME_FIELD = (By.CSS_SELECTOR, '#input-username')
    PASSWORD_FIELD = (By.CSS_SELECTOR, '#input-password')
    LOGO = (By.CSS_SELECTOR, '#header-logo > a > img')
    FORGOT_PASSWORD_LINK = (By.LINK_TEXT, 'Forgotten Password')
    LOGIN_BTN = (By.XPATH, '//*[@id="content"]/div/div/div/div/div[2]/form/div[3]/button')


class AdminPage(BasePage):
    URL = '/admin'

    def login(self):
        return self.wait_clickable_find(3, AdminPageLocators.LOGIN_BTN).click()
