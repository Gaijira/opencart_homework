from pages.MainPage import *
import allure


def test_title(browser, url):
    main_page = MainPage(browser)
    with allure.step("Открываем главную страницу"):
        main_page.open_page(url)
    with allure.step("Проверяем тайтл"):
        main_page.wait_assert_title(2, 'Your Store')
