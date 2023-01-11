"""
pytest -s -v test_parameters.py
The owls are not what they seem! OvO
"""

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

import time
import math



@pytest.fixture(scope="function")
def browser():
#    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
#    print("\nquit browser..")
    browser.quit()

@pytest.mark.parametrize('url', ["236895", "236896", "236897", "236898", "236899", "236903", "236904", "236905"])
def test_guest_should_see_login_link(browser, url):
    link = "https://stepik.org/lesson/{}/step/1".format(url)
    browser.get(link)
    browser.implicitly_wait(5)
    browser.find_element(By.CLASS_NAME, 'ember-view.navbar__auth.navbar__auth_login').click()
    browser.implicitly_wait(10)
    browser.find_element(By.NAME, 'login').send_keys('genrymorli@gmail.com')
    browser.find_element(By.NAME, 'password').send_keys('dima17dima')
    browser.implicitly_wait(10)
    browser.find_element(By.CLASS_NAME, 'sign-form__btn.button_with-loader ').click()
    answer = math.log(int(time.time()))
    time.sleep(5)
    browser.find_element(By.CLASS_NAME, "textarea").send_keys(str(answer))  # ember-auto-resize ember-view")
    time.sleep(2)
    browser.find_element(By.CLASS_NAME,"submit-submission").click()
    time.sleep(3)
    message = browser.find_element(By.CLASS_NAME, "smart-hints__feedback").text # hints__component hints__component_showed ember-view")
    time.sleep(2)
    assert message == "Correct!", "Attention, aliens!"  # - {}".format(message)