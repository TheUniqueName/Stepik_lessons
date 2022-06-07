import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.chrome.service import Service as GService
from selenium.webdriver.firefox.service import Service as FService


def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default="chrome",
                     help="Choose browser: chrome or firefox")


@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("browser_name")
    browser = None
    if browser_name == "chrome":
        print("\nstart chrome browser for test..")
        option = webdriver.ChromeOptions()
        # option.add_argument("--headless")
        option.add_argument("--disable-gpu")
        browser = webdriver.Chrome(service=GService(ChromeDriverManager().install()), options=option)
    elif browser_name == "firefox":
        print("\nstart firefox browser for test..")
        option = webdriver.FirefoxOptions()
        # option.add_argument("--headless")
        option.add_argument("--disable-gpu")
        browser = webdriver.Firefox(service=FService(GeckoDriverManager().install()), options=option)
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")
    yield browser
    print("\nquit browser..")
    browser.quit()
