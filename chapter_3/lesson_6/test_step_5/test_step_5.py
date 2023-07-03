"""
https://stepik.org/lesson/237240/step/5?unit=209628
"""

import math
import time

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

LINKS = [
	"https://stepik.org/lesson/236895/step/1",
	"https://stepik.org/lesson/236896/step/1",
	"https://stepik.org/lesson/236897/step/1",
	"https://stepik.org/lesson/236898/step/1",
	"https://stepik.org/lesson/236899/step/1",
	"https://stepik.org/lesson/236903/step/1",
	"https://stepik.org/lesson/236904/step/1",
	"https://stepik.org/lesson/236905/step/1"
]


class TestStep4:

	@pytest.mark.parametrize("link", LINKS)
	def test_sign_in(self, browser, link):
		browser.get(link)
		log_in_button = browser.find_element(By.ID, "ember33")
		log_in_button.click()

		log_in_window = browser.find_element(By.ID, "login_form")
		email_input = log_in_window.find_element(By.XPATH, ".//input[@name='login']")
		email_input.send_keys("geohots@mail.ru")
		password_input = log_in_window.find_element(By.XPATH, ".//input[@name='password']")
		password_input.send_keys("MasterGuide6621")
		log_in_submit_button = log_in_window.find_element(By.XPATH, ".//button[@type='submit']")
		log_in_submit_button.click()

		WebDriverWait(browser, 10).until_not(expected_conditions.presence_of_element_located((By.ID, "login_form")))

		WebDriverWait(browser, 10).until(expected_conditions.presence_of_element_located((By.ID, "ember93")))
		answer_edit = browser.find_element(By.ID, "ember93")
		answer_edit.send_keys(math.log(int(time.time())))

		WebDriverWait(browser, 10).until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, ".submit-submission")))
		submit_solution_button = browser.find_element(By.CSS_SELECTOR, ".submit-submission")
		submit_solution_button.click()

		WebDriverWait(browser, 10).until(expected_conditions.text_to_be_present_in_element((By.XPATH, "//div[@id='ember108']/p"), "Correct!"))
