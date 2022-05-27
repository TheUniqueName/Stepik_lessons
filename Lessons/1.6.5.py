from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.common.by import By
import math

link = "http://suninjuly.github.io/find_link_text"
link_text = "224592"

try:
    option = webdriver.ChromeOptions()
    # option.add_argument("--headless")
    option.add_argument("--disable-gpu")
    browser = webdriver.Chrome(ChromeDriverManager().install(), options=option)
    browser.get(link)

    da_link = browser.find_element_by_partial_link_text(link_text)
    da_link.click()

    input1 = browser.find_element_by_css_selector(".form-group:nth-child(1) input")
    input1.send_keys("Ivan")
    input2 = browser.find_element_by_css_selector(".form-group:nth-child(2) input")
    input2.send_keys("Petrov")
    input3 = browser.find_element_by_css_selector(".form-group:nth-child(3) input")
    input3.send_keys("Smolensk")
    input4 = browser.find_element_by_css_selector(".form-group:nth-child(4) input")
    input4.send_keys("Russia")
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    #browser.quit()
