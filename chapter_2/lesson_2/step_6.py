"""
https://stepik.org/lesson/228249/step/6?unit=200781
"""

import math
import time

from selenium import webdriver
from selenium.webdriver.common.by import By


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


try:
    link = "http://suninjuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)
    browser.maximize_window()

    x_element = browser.find_element(By.XPATH, '//span[@id="input_value"]')
    answer = calc(x_element.text)

    button = browser.find_element(By.TAG_NAME, "button")
    browser.execute_script("return arguments[0].scrollIntoView({block: 'start', inline: 'nearest', behavior: 'smooth'});", button)
    # browser.execute_script("window.scrollBy(0, 100);")

    answer_field = browser.find_element(By.ID, "answer")
    answer_field.send_keys(answer)

    robot_checkbox = browser.find_element(By.CSS_SELECTOR, "[for='robotCheckbox']")
    robot_checkbox.click()

    robot_radio = browser.find_element(By.CSS_SELECTOR, "[for='robotsRule']")
    robot_radio.click()

    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
