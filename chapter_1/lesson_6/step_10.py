"""
https://stepik.org/lesson/138920/step/8?unit=196194
"""

import time

from selenium import webdriver
from selenium.webdriver.common.by import By

try:
    link = "http://suninjuly.github.io/registration2.html"
    browser = webdriver.Chrome()
    browser.get(link)
    browser.maximize_window()

    # Ваш код, который заполняет обязательные поля
    first_name_input = browser.find_element(By.XPATH, '//input[@placeholder="Input your first name"]')
    first_name_input.send_keys("John")

    last_name_input = browser.find_element(By.XPATH, '//input[@placeholder="Input your last name"]')
    last_name_input.send_keys("Wick")

    email_input = browser.find_element(By.XPATH, '//input[@class="form-control third"]')
    email_input.send_keys("john.wick@dog.com")

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
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
