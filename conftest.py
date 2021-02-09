import pytest
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption("--maximized", action="store_true", help="Maximize browser windows")
    parser.addoption("--headless", action="store_true", help="Run headless")
    parser.addoption("--browser", action="store", choices=["chrome", "firefox", "safari"], help="Browser")
    parser.addoption("--url", action="store", help="Input URL for test")


@pytest.fixture
def url(request):
    return request.config.getoption("--url")


@pytest.fixture
def browser(request):
    browser = request.config.getoption("--browser")
    headless = request.config.getoption("--headless")
    maximized = request.config.getoption("--maximized")

    driver = None

    if browser == "chrome":
        options = webdriver.ChromeOptions()
        if headless:
            options.headless = True
        driver = webdriver.Chrome(options=options)

    elif browser == "firefox":
        options = webdriver.FirefoxOptions()
        if headless:
            options.headless = True
        driver = webdriver.Firefox(options=options)

    elif browser == "ie":
        options = webdriver.IeOptions()
        if headless:
            options.headless = True
        driver = webdriver.ie(options=options)

    if maximized:
        driver.maximize_window()

    request.addfinalizer(driver.close)

    return driver
