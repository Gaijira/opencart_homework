from pages.MainPage import *


def test_title(browser, url):
    main_page = MainPage(browser)
    main_page.open_page(url)
    main_page.wait_assert_title(2, 'Your Store')
