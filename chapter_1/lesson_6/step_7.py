"""
https://stepik.org/lesson/138920/step/7?unit=196194
"""
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/huge_form.html")
    browser.maximize_window()
    elements = browser.find_elements(By.TAG_NAME, "input")
    for i, element in enumerate(elements):
        element.send_keys(f"kek{i}")

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()
