from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math


'''Открыть страницу http://suninjuly.github.io/alert_accept.html
Нажать на кнопку
Принять confirm
На новой странице решить капчу для роботов, чтобы получить число с ответом'''

browser = webdriver.Chrome()

link = 'http://suninjuly.github.io/alert_accept.html'

browser.get(link)


browser.find_element(By.TAG_NAME, "button").click()
time.sleep(1)
alert = browser.switch_to.alert
alert.accept()
time.sleep(1)
x = browser.find_element(By.ID, 'input_value').text
#print(x)

result = math.log(abs((12 * math.sin(int(x)))))

#print(result)

b = browser.find_element(By.ID, 'answer')
b.send_keys(result)


# alert = browser.switch_to.alert
time.sleep(1)

browser.find_element(By.CLASS_NAME, "btn.btn-primary").click()

browser.switch_to.alert

y = browser.switch_to.alert.text.split()[-1]

print(y)

browser.quit()

'''browser.get('https://stepik.org/lesson/184253/step/4?unit=158843')
time.sleep(3)
browser.find_element(By.CLASS_NAME, 'ember-text-area.ember-view.textarea.string-quiz__textarea').send_keys(y)
time.sleep(3)

browser.quit()'''