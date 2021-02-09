from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


def test_admin(browser, url):
    browser.get(url + '/admin')
    WebDriverWait(browser, 3).until(EC.element_to_be_clickable(
        (By.CSS_SELECTOR, '#content > div > div > div > div > div.panel-body > form > div.text-right > button')))
    browser.find_element_by_css_selector(
        '#content > div > div > div > div > div.panel-body > form > div.text-right > button').click()
    WebDriverWait(browser, 3).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, '#header > div > ul > li:nth-child(2) > a')))
    browser.find_element_by_css_selector('#header > div > ul > li:nth-child(2) > a').click()
    assert browser.title == 'Administration'


def test_products(browser, url):
    browser.get(url + '/admin')

    WebDriverWait(browser, 3).until(EC.element_to_be_clickable(
        (By.CSS_SELECTOR, '#content > div > div > div > div > div.panel-body > form > div.text-right > button')))
    browser.find_element_by_css_selector(
        '#content > div > div > div > div > div.panel-body > form > div.text-right > button').click()

    WebDriverWait(browser, 3).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#menu-catalog > a')))
    browser.find_element_by_css_selector('#menu-catalog > a').click()

    WebDriverWait(browser, 3).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#collapse1 > li:nth-child(2)')))
    browser.find_element_by_css_selector('#collapse1 > li:nth-child(2)').click()

    WebDriverWait(browser, 3).until(EC.visibility_of_element_located((By.CSS_SELECTOR,
    '#content > div.container-fluid > div > div.col-md-9.col-md-pull-3.col-sm-12 > div > div.panel-body')))
    browser.find_element_by_css_selector(
        '#content > div.container-fluid > div > div.col-md-9.col-md-pull-3.col-sm-12 > div > div.panel-body')
