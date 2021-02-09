from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_title(browser, url):
    browser.get(url)
    WebDriverWait(browser, 3).until(EC.title_is('Your Store'))
    assert browser.title == 'Your Store'
