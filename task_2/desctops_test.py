def test_desktop(browser, url):
    browser.get(url + '?route=product/category&path=20')
    browser.find_element_by_css_selector('#product-category > ul')
    browser.find_element_by_css_selector('#column-left > div.list-group')
    browser.find_element_by_css_selector('#column-left > div.swiper-viewport')
    browser.find_element_by_css_selector('#list-view')
    browser.find_element_by_css_selector('#grid-view')