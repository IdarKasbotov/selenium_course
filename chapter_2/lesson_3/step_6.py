"""
https://stepik.org/lesson/184253/step/6?unit=158843
"""
import math
import time

from selenium import webdriver
from selenium.webdriver.common.by import By


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


try:
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)
    browser.maximize_window()

    submit_button = browser.find_element(By.XPATH, "//button[@type='submit']")
    submit_button.click()

    second_window = browser.window_handles[1]
    browser.switch_to.window(second_window)

    x_element = browser.find_element(By.XPATH, '//span[@id="input_value"]')
    answer = calc(x_element.text)

    answer_field = browser.find_element(By.ID, "answer")
    answer_field.send_keys(answer)

    submit_button = browser.find_element(By.XPATH, "//button[@type='submit']")
    submit_button.click()

    alert = browser.switch_to.alert
    alert_text = alert.text
    print(alert_text.split(": ")[-1])

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
