from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time

'''Открыть страницу http://suninjuly.github.io/get_attribute.html.
Найти на ней элемент-картинку, который является изображением сундука с сокровищами.
Взять у этого элемента значение атрибута valuex, которое является значением x для задачи.
Посчитать математическую функцию от x (сама функция остаётся неизменной).
Ввести ответ в текстовое поле.
Отметить checkbox "I'm the robot".
Выбрать radiobutton "Robots rule!".
Нажать на кнопку "Submit".'''

link = 'http://suninjuly.github.io/get_attribute.html'
browser = webdriver.Chrome()
browser.get(link)

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


x_element = browser.find_element(By.ID, 'treasure')
x = int(x_element.get_attribute('valuex'))
y = calc(x)

answer = browser.find_element(By.ID, 'answer')
answer.send_keys(y)
time.sleep(1)
checkbox = browser.find_element(By.ID, 'robotCheckbox')
checkbox.click()

radiobutton = browser.find_element(By.ID, 'robotsRule')
radiobutton.click()
#time.is locals()
#time.sleep(10)

browser.find_element(By.CLASS_NAME, 'btn.btn-default').click()

time.sleep(5)
browser.quit()