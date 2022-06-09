import logging
import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as GService


def pytest_addoption(parser):
    parser.addoption('--language', action='store', default="ru",
                     help="Choose language from the list: "
                          "ar, ca, cs, da, de, en-gb, el, es, fi, fr,it, ko, nl, pl, pt, pt-br, ro, ru, sk, uk, zh-hans")


@pytest.fixture(scope="session")
def browser(request):
    browser_language = request.config.getoption("language")
    browser = None
    # Проверяем дозволенные на сайте языки
    if browser_language in ["ar", "ca", "cs", "da", "de", "en-gb", "el", "es", "fi", "fr", "it", "ko", "nl", "pl", "pt",
                            "pt-br", "ro", "ru", "sk", "uk", "zh-hans"]:
        logging.info("start chrome browser for test..")
        option = webdriver.ChromeOptions()
        option.add_argument("-lang=es")
        # option.add_argument("--headless")
        # option.add_argument("--disable-gpu")
        browser = webdriver.Chrome(service=GService(ChromeDriverManager().install()), options=option)
    else:
        raise pytest.UsageError("Select a proper --language")
    yield browser
    logging.info("quit browser..")
    browser.quit()
