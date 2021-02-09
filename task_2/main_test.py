from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


def test_index(browser, url):
    browser.get(url)

    WebDriverWait(browser, 3).until(EC.visibility_of_element_located((By.CSS_SELECTOR, '#cart > button')))
    browser.find_element_by_css_selector('#cart > button')

    WebDriverWait(browser, 3).until(EC.visibility_of_element_located((By.CSS_SELECTOR, '#menu > div.navbar-header')))
    browser.find_element_by_css_selector('#menu > div.navbar-header')

    WebDriverWait(browser, 3).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#search')))
    browser.find_element_by_css_selector('#search')

    WebDriverWait(browser, 3).until(EC.visibility_of_element_located((By.CSS_SELECTOR, '#logo > h1 > a')))
    browser.find_element_by_css_selector('#logo > h1 > a')

    WebDriverWait(browser, 3).until(EC.visibility_of_element_located((By.CSS_SELECTOR, '#slideshow0')))
    browser.find_element_by_css_selector('#slideshow0')
