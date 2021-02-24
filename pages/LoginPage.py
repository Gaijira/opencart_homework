from pages.BasePage import BasePage
from selenium.webdriver.common.by import By


class LoginPageLocators:
    CONTINUE_BTN = (By.LINK_TEXT, 'Continue')
    EMAIL_FIELD = (By.CSS_SELECTOR, '#input-email')
    PASSWORD_FIELD = (By.CSS_SELECTOR, '#input-password')
    LOGIN_BTN = (By.CSS_SELECTOR, '#content > div > div:nth-child(2) > div > form > input')
    RIGHT_COLUMN = (By.CSS_SELECTOR, '#column-right > div')


class LoginPage(BasePage):
    URL = '?route=account/login'
