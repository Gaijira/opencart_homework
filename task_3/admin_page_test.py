import time

def test_admin(browser, url):
    browser.get(url + '/admin')
    browser.find_element_by_css_selector(
        '#content > div > div > div > div > div.panel-body > form > div.text-right > button').click()
    browser.find_element_by_css_selector('#header > div > ul > li:nth-child(2) > a').click()
    assert browser.title == 'Administration'

def test_products(browser,url):
    browser.get(url + '/admin')
    browser.find_element_by_css_selector(
        '#content > div > div > div > div > div.panel-body > form > div.text-right > button').click()
    browser.find_element_by_css_selector('#menu-catalog > a').click()
    time.sleep(3)
    browser.find_element_by_css_selector('#collapse1 > li:nth-child(2)').click()
    browser.find_element_by_css_selector('#content > div.container-fluid > div > div.col-md-9.col-md-pull-3.col-sm-12 > div > div.panel-body')