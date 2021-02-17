from pages.BasePage import BasePage
from selenium.webdriver.common.by import By


class MainPageLocators:
    SLIDER = (By.CSS_SELECTOR, '#slideshow0')
    TITLE = 'Your Store'


class MainPage(BasePage):
    pass

