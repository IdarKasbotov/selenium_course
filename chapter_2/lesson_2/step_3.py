"""
https://stepik.org/lesson/228249/step/3?unit=200781
"""

import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

try:
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)
    browser.maximize_window()

    first_number_label = browser.find_element(By.XPATH, '//span[@id="num1"]')
    second_number_label = browser.find_element(By.ID, 'num2')
    sum_of_numbers = int(first_number_label.text) + int(second_number_label.text)

    select = Select(browser.find_element(By.XPATH, "//select"))
    select.select_by_value(str(sum_of_numbers))

    submit_button = browser.find_element(By.XPATH, '//button[@type="submit"]')
    submit_button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
