"""
https://stepik.org/lesson/236918/step/2?unit=209305
pytest -s -v -m smoke ./chapter_3/lesson_5/test_step_2/test_step_2.py, где -v - это verbose, -s для того, чтобы видеть принты, -m маркер
pytest -s -v -m "not smoke" ./chapter_3/lesson_5/test_step_2/test_step_2.py - инверсия, запустятся все тесты, кроме smoke
pytest -s -v -m "smoke or regression" ./chapter_3/lesson_5/test_step_2/test_step_2.py - запустятся тесты smoke и regression
pytest -s -v -m "smoke and win10" ./chapter_3/lesson_5/test_step_2/test_step_2.py - запустятся тесты, у которых 2 этих маркера

pytest -s -v -rx ./chapter_3/lesson_5/test_step_2/test_step_2.py, где -rx report-on-xfail
-rxXs показывать дополнительную информацию о тестах xfailed, xpassed, и skipped
Ни XFAIL, ни XPASS по умолчанию не приводят к падению всего набора тестов. Но это можно изменить, установив параметру strict значение True:
"""
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

link = "http://selenium1py.pythonanywhere.com/"


@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()


class TestMainPage1:

    @pytest.mark.smoke
    @pytest.mark.win10
    def test_guest_should_see_login_link(self, browser):
        browser.get(link)
        browser.find_element(By.CSS_SELECTOR, "#login_link")

    @pytest.mark.regression
    def test_guest_should_see_basket_link_on_the_main_page(self, browser):
        browser.get(link)
        browser.find_element(By.CSS_SELECTOR, ".basket-mini .btn-group > a")

    @pytest.mark.xfail(reason="fixing this bug right now")  # xfail для тестов, от которых ожидаем падение
    def test_guest_should_see_search_button_on_the_main_page(self, browser):
        browser.get(link)
        browser.find_element(By.CSS_SELECTOR, "button.favorite")
