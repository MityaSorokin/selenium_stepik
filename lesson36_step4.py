import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

import math
import time

#link = 'https://stepik.org/lesson/236895/step/1'



links = [
        'https://stepik.org/lesson/236895/step/1',
        'https://stepik.org/lesson/236896/step/1',
        'https://stepik.org/lesson/236897/step/1',
        'https://stepik.org/lesson/236898/step/1',
        'https://stepik.org/lesson/236899/step/1',
        'https://stepik.org/lesson/236903/step/1',
        'https://stepik.org/lesson/236904/step/1',
        'https://stepik.org/lesson/236905/step/1'
]
'''
@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()
'''
class TestMainPage():

    @pytest.mark.parametrize('links', links)
    def test_answer(browser, links):
        options = webdriver.ChromeOptions()
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        browser = webdriver.Chrome(executable_path='<path-to-chrome>', options=options)
        #browser = webdriver.Chrome()
        browser.get(links)
        browser.implicitly_wait(5)
        browser.find_element(By.CLASS_NAME, 'ember-view.navbar__auth.navbar__auth_login').click()
        browser.implicitly_wait(10)
        browser.find_element(By.NAME, 'login').send_keys('***')
        browser.find_element(By.NAME, 'password').send_keys('***')
        browser.implicitly_wait(10)
        browser.find_element(By.CLASS_NAME, 'sign-form__btn.button_with-loader ').click()
        time.sleep(2)
        #browser.get(links)
        #answer = math.log(int(time.time()))
        browser.implicitly_wait(10)
        #browser.find_element(By.CLASS_NAME,"ember-text-area.ember-view.textarea.string-quiz__textarea").send_keys()
        time.sleep(3)
        browser.find_element(By.CLASS_NAME, "textarea").send_keys(str(math.log(int(time.time()))))
        browser.implicitly_wait(10)
        time.sleep(4)
        browser.find_element(By.CLASS_NAME, 'submit-submission').click()
        time.sleep(4)
        browser.implicitly_wait(10)
        #print(browser.find_element(By.CLASS_NAME, 'smart-hints').text)
        assert "Correct!" in browser.find_element(By.CLASS_NAME, 'smart-hints__hint').text, f"Wrong result, got {browser.find_element(By.CLASS_NAME, 'smart-hints__hint').text} instead of Correct!"
        #print(browser.find_element(By.CLASS_NAME, 'smart-hints__hint'))
        #if browser.find_element(By.CLASS_NAME, 'smart-hints__hint').text == "Correct!": assert True
        #else: assert False