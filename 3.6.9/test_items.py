from selenium.webdriver.common.by import By
import time

link = "http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/"


def test_guest_should_see_login_link_pass(browser):
    browser.get(link)
    time.sleep(30)
    browser.find_element(By.CLASS_NAME, "btn-add-to-basket")