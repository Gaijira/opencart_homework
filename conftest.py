import pytest
from selenium import webdriver
import logging

logging.basicConfig(level=logging.INFO, filename="selenium.log",
                    format='%(levelname)s:[%(asctime)s]:%(name)s:%(message)s')


def pytest_addoption(parser):
    parser.addoption("--maximized", action="store_true", help="Maximize browser windows", default=False)
    parser.addoption("--browser", action="store", choices=["chrome", "firefox", "safari"], help="Browser")
    parser.addoption("--url", action="store", help="Input URL for test")
    parser.addoption("--logs", action="store_true", default=False)
    parser.addoption("--executor", action="store", default="192.168.1.27")
    parser.addoption("--bversion", action="store", default="88.0")
    parser.addoption("--vnc", action="store_true", default=False)


@pytest.fixture
def url(request):
    return request.config.getoption("--url")


@pytest.fixture
def browser(request):
    browser = request.config.getoption("--browser")
    maximized = request.config.getoption("--maximized")
    executor = request.config.getoption("--executor")
    vnc = request.config.getoption("--vnc")
    bversion = request.config.getoption("--bversion")
    logs = request.config.getoption("--logs")
    logger = logging.getLogger('BrowserLogger')
    test_name = request.node.name
    logger.info("Test {} started".format(test_name))

    executor_url = f"http://{executor}:4444/wd/hub"

    caps = {
        "browserName": browser,
        "browserVersion": bversion,
        "screenResolution": "1280x1024x24",
        "selenoid:options": {
            "enableVNC": vnc,
            "enableVideo": False,
            "enableLog": logs
        },
        'acceptSslCerts': True,
        'acceptInsecureCerts': True,
        'timeZone': 'Europe/Moscow'
    }
    driver = webdriver.Remote(command_executor=executor_url, desired_capabilities=caps)
    if maximized:
        driver.maximize_window()
    else:
        pass
    logger.info("Browser {} started with browser version:{}".format(browser, driver.capabilities['browserVersion']))
    request.addfinalizer(driver.quit)
    logger.info("Browser {} closed".format(browser))
    logger.info("Test {} finished".format(test_name))

    with open("allure-results/environment.properties", 'w') as f:
        f.write(f"Browser:{browser}\n"
                f"Browser.version:{driver.capabilities['browserVersion']}\n"
                f"Stand=Somestand\n")

    return driver
