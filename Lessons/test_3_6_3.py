from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
import math
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

link = "https://stepik.org/lesson/236895/step/1"

try:
    option = webdriver.ChromeOptions()
    # option.add_argument("--headless")
    option.add_argument("--disable-gpu")
    browser = webdriver.Chrome(ChromeDriverManager().install(), options=option)
    browser.get(link)

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


finally:
    # успеваем скопировать код за 30 секунд
    print(result_text)
    # time.sleep(25)
    # закрываем браузер после всех манипуляций
    browser.quit()
