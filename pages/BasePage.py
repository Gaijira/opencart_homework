from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, browser):
        self.browser = browser

    def wait_visibility_find(self, time, locator):
        return WebDriverWait(self.browser, time).until(EC.visibility_of_element_located(locator))

    def wait_clickable_find(self, time, locator):
        return WebDriverWait(self.browser, time).until(EC.element_to_be_clickable(locator))

    def wait_assert_title(self, time, title):
        browser_title = WebDriverWait(self.browser, time).until(EC.title_is(title))
        assert self.browser.title == title
        return browser_title

    def open_page(self, url):
        return self.browser.get(url)
