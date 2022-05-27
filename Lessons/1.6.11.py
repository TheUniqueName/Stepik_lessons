from selenium import webdriver
# используем вебдрайвер-менеджер, чтобы не заморачиваться с вебдрайвером и его версиями
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.common.by import By

#link = "http://suninjuly.github.io/registration1.html"
link = "http://suninjuly.github.io/registration2.html"
browser = webdriver.Chrome(ChromeDriverManager().install())

try:
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    first_name = browser.find_element(By.CSS_SELECTOR, ".first_block .first")
    first_name.send_keys("John")

    last_name = browser.find_element(By.CSS_SELECTOR, ".first_block .second")
    last_name.send_keys("Doe")

    email = browser.find_element(By.CSS_SELECTOR, ".first_block .third")
    email.send_keys("j-doe@website.zone")

    phone = browser.find_element(By.CSS_SELECTOR, ".second_block .first")
    phone.send_keys("8 800 555 35 35")

    address = browser.find_element(By.CSS_SELECTOR, ".second_block .second")
    address.send_keys("Paper st. 420")

    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # смотрим на результат
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()
