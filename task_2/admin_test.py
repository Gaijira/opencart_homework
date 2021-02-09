from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


def test_admin(browser, url):
    browser.get(url + '/admin')

    WebDriverWait(browser, 3).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#input-username')))
    browser.find_element_by_css_selector('#input-username')

    WebDriverWait(browser, 3).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#input-password')))
    browser.find_element_by_css_selector('#input-password')

    WebDriverWait(browser, 3).until(EC.element_to_be_clickable(
        (By.CSS_SELECTOR, '#content > div > div > div > div > div.panel-body > form > div:nth-child(2) > span > a')))
    browser.find_element_by_css_selector(
        '#content > div > div > div > div > div.panel-body > form > div:nth-child(2) > span > a')

    WebDriverWait(browser, 3).until(EC.element_to_be_clickable(
        (By.CSS_SELECTOR, '#content > div > div > div > div > div.panel-body > form > div.text-right > button')))
    browser.find_element_by_css_selector(
        '#content > div > div > div > div > div.panel-body > form > div.text-right > button')

    WebDriverWait(browser, 3).until(EC.visibility_of_element_located((By.CSS_SELECTOR, '#header-logo > a > img')))
    browser.find_element_by_css_selector('#header-logo > a > img')
