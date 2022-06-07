import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service


@pytest.fixture(scope="session")
def browser():
    print("\nstart browser for test..")
    option = webdriver.ChromeOptions()
    # option.add_argument("--headless")
    option.add_argument("--disable-gpu")
    browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=option)
    yield browser
    print("\nquit browser..")
    browser.quit()