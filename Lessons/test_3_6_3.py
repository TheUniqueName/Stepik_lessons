import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import time
import math
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


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


@pytest.mark.parametrize('pages', ["236895", "236896", "236897", "236898", "236899", "236903", "236904", "236905"])
def test_guest_should_see_login_link(browser, pages):
    landing_page = f"https://stepik.org/lesson/{pages}/step/1"
    browser.get(landing_page)

    ember_input = WebDriverWait(browser, 15).until(
        EC.presence_of_element_located((By.TAG_NAME, 'textarea'))
    )
    answer = math.log(int(time.time()))
    ember_input.send_keys(answer)
    submit_button = browser.find_element(By.CSS_SELECTOR, "button.submit-submission")
    submit_button.click()

    result_message = WebDriverWait(browser, 15).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, ".smart-hints__hint"))
    )
    result_text = result_message.text
    assert result_text == "Correct!", f"Result text is '{result_text}'"
