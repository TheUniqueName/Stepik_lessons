from selenium import webdriver
import time
import math
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    option = webdriver.ChromeOptions()
    # option.add_argument("--headless")
    option.add_argument("--disable-gpu")
    browser = webdriver.Chrome(ChromeDriverManager().install(), options=option)
    browser.get("http://SunInJuly.github.io/execute_script.html")

    num_search = browser.find_element(By.ID, 'input_value')
    num = num_search.text
    number = int(num)
    result_sum = calc(number)

    button = browser.find_element_by_tag_name("button")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)

    answer_input = browser.find_element(By.ID, 'answer')
    answer_input.send_keys(result_sum)

    robot_checkbox = browser.find_element(By.ID, 'robotCheckbox')
    robot_checkbox.click()

    robot_radio = browser.find_element(By.ID, 'robotsRule')
    robot_radio.click()

    button = browser.find_element_by_xpath("//button[text()='Submit']")
    button.click()


finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла
