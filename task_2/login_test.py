def test_login(browser, url):
    browser.get(url + '?route=account/login')
    browser.find_element_by_css_selector('#content > div > div:nth-child(1) > div > a')
    browser.find_element_by_css_selector('#input-email')
    browser.find_element_by_css_selector('#input-password')
    browser.find_element_by_css_selector('#content > div > div:nth-child(2) > div > form > input')
    browser.find_element_by_css_selector('#column-right > div')
