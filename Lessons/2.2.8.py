from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.common.by import By
import os

link = "http://suninjuly.github.io/file_input.html"
browser = webdriver.Chrome(ChromeDriverManager().install())

try:
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    input1 = browser.find_element(By.XPATH, "//input[@name='firstname']")
    input1.send_keys("Ivan")
    input2 = browser.find_element(By.XPATH, "//input[@name='lastname']")
    input2.send_keys("Petrov")
    input3 = browser.find_element(By.XPATH, "//input[@name='email']")
    input3.send_keys("j-doe@website.zone")
    file_input = browser.find_element(By.ID, "file")
    current_dir = os.path.abspath(os.path.dirname(__file__))  # получаем путь к директории текущего исполняемого файла
    file_path = os.path.join(current_dir, 'file.txt')  # добавляем к этому пути имя файла
    file_input.send_keys(file_path)

    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    # смотрим на результат
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()
