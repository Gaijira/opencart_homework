from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


def test_desktop(browser, url):
    browser.get(url + '?route=product/category&path=20')

    WebDriverWait(browser, 3).until(EC.visibility_of_element_located((By.CSS_SELECTOR, '#product-category > ul')))
    browser.find_element_by_css_selector('#product-category > ul')

    WebDriverWait(browser, 3).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, '#column-left > div.list-group')))
    browser.find_element_by_css_selector('#column-left > div.list-group')

    WebDriverWait(browser, 3).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, '#column-left > div.swiper-viewport')))
    browser.find_element_by_css_selector('#column-left > div.swiper-viewport')

    WebDriverWait(browser, 3).until(EC.visibility_of_element_located((By.CSS_SELECTOR, '#list-view')))
    browser.find_element_by_css_selector('#list-view')

    WebDriverWait(browser, 3).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#grid-view')))
    browser.find_element_by_css_selector('#grid-view')
