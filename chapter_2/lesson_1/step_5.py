"""
https://stepik.org/lesson/165493/step/5?unit=140087
"""

import math
import time

from selenium import webdriver
from selenium.webdriver.common.by import By


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


try:
    link = "https://suninjuly.github.io/math.html"
    browser = webdriver.Chrome()
    browser.get(link)
    browser.maximize_window()

    x_element = browser.find_element(By.CSS_SELECTOR, "#input_value")
    x = x_element.text
    y = calc(x)

    answer_input = browser.find_element(By.CSS_SELECTOR, "#answer")
    answer_input.send_keys(y)

    robot_checkbox = browser.find_element(By.XPATH, '//label[@for="robotCheckbox"]')
    robot_checkbox.click()

    robot_radio = browser.find_element(By.XPATH, '//label[@for="robotsRule"]')
    robot_radio.click()

    submit_button = browser.find_element(By.XPATH, '//button[@type="submit"]')
    submit_button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
