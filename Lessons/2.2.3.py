from selenium import webdriver
import time
import math
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


try:
    option = webdriver.ChromeOptions()
    # option.add_argument("--headless")
    option.add_argument("--disable-gpu")
    browser = webdriver.Chrome(ChromeDriverManager().install(), options=option)
    browser.get("http://suninjuly.github.io/selects1.html")

    num1_search = browser.find_element(By.ID, 'num1')
    num1 = num1_search.text
    number1 = int(num1)

    num2_search = browser.find_element(By.ID, 'num2')
    num2 = num2_search.text
    number2 = int(num2)

    result_sum = number1+number2
    result_sum_str = str(result_sum)

    dropdown = Select(browser.find_element(By.ID, 'dropdown'))
    dropdown.select_by_value(result_sum_str)

    button = browser.find_element_by_xpath("//button[text()='Submit']")
    button.click()


finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла
