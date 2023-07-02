"""
https://stepik.org/lesson/181384/step/8?unit=156009
"""
import math
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


try:
    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser = webdriver.Chrome()
    browser.implicitly_wait(5)
    browser.get(link)
    browser.maximize_window()

    price_label = WebDriverWait(browser, 15).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100")
    )
    book_button = browser.find_element(By.XPATH, "//button[@id='book']")
    book_button.click()

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
