from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.common.by import By

link = "https://suninjuly.github.io/simple_form_find_task.html"

try:
    option = webdriver.ChromeOptions()
    # option.add_argument("--headless")
    option.add_argument("--disable-gpu")
    browser = webdriver.Chrome(ChromeDriverManager().install(), options=option)
    browser.get(link)

    input1 = browser.find_element(By.CSS_SELECTOR, ".form-group:nth-child(1) input")
    input1.send_keys("Ivan")
    input2 = browser.find_element(By.CSS_SELECTOR, ".form-group:nth-child(2) input")
    input2.send_keys("Petrov")
    input3 = browser.find_element(By.CSS_SELECTOR, ".form-group:nth-child(3) input")
    input3.send_keys("Smolensk")
    input4 = browser.find_element(By.CSS_SELECTOR, ".form-group:nth-child(4) input")
    input4.send_keys("Russia")
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    #browser.quit()
