"""
https://stepik.org/lesson/228249/step/8?unit=200781
"""

import time
from pathlib import Path

from selenium import webdriver
from selenium.webdriver.common.by import By

try:
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)
    browser.maximize_window()

    name_edit = browser.find_element(By.NAME, "firstname")
    name_edit.send_keys("John")

    last_name_edit = browser.find_element(By.NAME, "lastname")
    last_name_edit.send_keys("Wick")

    email_edit = browser.find_element(By.NAME, "email")
    email_edit.send_keys("john.wick@dog.com")

    choose_file_button = browser.find_element(By.ID, "file")
    file_path = Path(__file__).parent / "file_for_step_8.txt"
    choose_file_button.send_keys(str(file_path))

    submit_button = browser.find_element(By.XPATH, "//button[@type='submit']")
    submit_button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
