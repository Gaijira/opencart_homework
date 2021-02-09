from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


def test_login(browser, url):
    browser.get(url + '?route=account/login')

    WebDriverWait(browser, 3).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, '#content > div > div:nth-child(1) > div > a')))
    browser.find_element_by_css_selector('#content > div > div:nth-child(1) > div > a')

    WebDriverWait(browser, 3).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#input-email')))
    browser.find_element_by_css_selector('#input-email')

    WebDriverWait(browser, 3).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#input-password')))
    browser.find_element_by_css_selector('#input-password')

    WebDriverWait(browser, 3).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, '#content > div > div:nth-child(2) > div > form > input')))
    browser.find_element_by_css_selector('#content > div > div:nth-child(2) > div > form > input')

    WebDriverWait(browser, 3).until(EC.visibility_of_element_located((By.CSS_SELECTOR, '#column-right > div')))
    browser.find_element_by_css_selector('#column-right > div')
