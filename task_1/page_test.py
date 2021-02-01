def test_title(browser, url):
    browser.get(url)
    assert browser.title == 'Your Store'
