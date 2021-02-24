from pages.BasePage import BasePage
from selenium.webdriver.common.by import By


class ProductPageLocators:
    CART_ADD_BTN = (By.CSS_SELECTOR, '#button-cart')
    MAIN_IMG = (By.XPATH, '//*[@id="content"]/div/div[1]/ul[1]/li[1]/a')
    IMG_1 = (By.XPATH, '//*[@id="content"]/div/div[1]/ul[1]/li[2]/a/img')
    REVIEWS_BTN = (By.PARTIAL_LINK_TEXT, 'Reviews')
    COMPARE_BTN = (By.XPATH, '//*[@id="content"]/div/div[2]/div[1]/button[2]')


class ProductPage(BasePage):
    URL = '?route=product/product&path=57&product_id=49'
