def test_product(browser, url):
    browser.get(url + '?route=product/product&path=57&product_id=49')
    browser.find_element_by_css_selector('#content > div > div.col-sm-8 > ul.thumbnails > li:nth-child(1) > a')
    browser.find_element_by_css_selector('#button-cart')
    browser.find_element_by_css_selector('#content > div > div.col-sm-8 > ul.thumbnails > li:nth-child(2) > a')
    browser.find_element_by_css_selector('#content > div > div.col-sm-8 > ul.nav.nav-tabs > li:nth-child(2)')
    browser.find_element_by_css_selector('#content > div > div.col-sm-4 > div.btn-group > button:nth-child(2)')
