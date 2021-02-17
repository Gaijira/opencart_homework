from selenium.webdriver.common.by import By


class CommonLocators:
    CART_BTN = (By.CSS_SELECTOR, '#cart > button')
    NAV_BAR = (By.CSS_SELECTOR, '#menu')
    SEARCH_FIELD = (By.CSS_SELECTOR, '#search > input')
    SEARCH_COMPONENT = (By.CSS_SELECTOR, '#search ')
    LOGO = (By.CSS_SELECTOR, '#logo > h1 > a')
