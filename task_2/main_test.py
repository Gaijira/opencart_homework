def test_index(browser, url):
    browser.get(url)
    browser.find_element_by_css_selector('#cart > button')
    browser.find_element_by_css_selector('#menu > div.navbar-header')
    browser.find_element_by_css_selector('#search')
    browser.find_element_by_css_selector('#logo > h1 > a')
    browser.find_element_by_css_selector('#slideshow0')
