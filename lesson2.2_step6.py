from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
import math
import time

'''Открыть страницу http://SunInJuly.github.io/execute_script.html.
Считать значение для переменной x.
Посчитать математическую функцию от x ln(abs(12*sin(x))).
Проскроллить страницу вниз.
Ввести ответ в текстовое поле.
Выбрать checkbox "I'm the robot".
Переключить radiobutton "Robots rule!".
Нажать на кнопку "Submit".'''

link = 'http://SunInJuly.github.io/execute_script.html'
browser = webdriver.Chrome()
browser.get(link)
browser.maximize_window()

x = browser.find_element(By.ID, 'input_value').text
result = math.log(abs(12 * math.sin(int(x))))
print(f'result - {result}')

browser.execute_script("window.scrollBy(0, 230);")
browser.find_element(By.ID, 'answer').send_keys(result)

'''
expected_el = expected_conditions.presence_of_element_located(By.TAG_NAME, 'button'
el = WebDriverWait(browser, timeout).until((expected_el)))
'''

browser.find_element(By.ID, 'robotCheckbox').click()
browser.find_element(By.ID, 'robotsRule').click()


browser.find_element(By.CLASS_NAME, 'btn.btn-primary').click()
time.sleep(4)
