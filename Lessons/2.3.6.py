from selenium import webdriver
import time
import math
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    option = webdriver.ChromeOptions()
    option.add_argument("--disable-gpu")
    browser = webdriver.Chrome(ChromeDriverManager().install(), options=option)
    browser.get("http://suninjuly.github.io/redirect_accept.html")

    button = browser.find_element(By.XPATH, "//button")
    button.click()

    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)

    num_search = browser.find_element(By.ID, 'input_value')
    num = num_search.text
    number = int(num)
    result_sum = calc(number)

    answer_input = browser.find_element(By.ID, 'answer')
    answer_input.send_keys(result_sum)

    button = browser.find_element(By.XPATH, "//button[text()='Submit']")
    button.click()

    alert = browser.switch_to.alert
    print(alert.text)

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла
