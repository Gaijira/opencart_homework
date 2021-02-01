def test_admin(browser, url):
    browser.get(url + '/admin')
    browser.find_element_by_css_selector('#input-username')
    browser.find_element_by_css_selector('#input-password')
    browser.find_element_by_css_selector(
        '#content > div > div > div > div > div.panel-body > form > div:nth-child(2) > span > a')
    browser.find_element_by_css_selector(
        '#content > div > div > div > div > div.panel-body > form > div.text-right > button')
    browser.find_element_by_css_selector('#header-logo > a > img')
