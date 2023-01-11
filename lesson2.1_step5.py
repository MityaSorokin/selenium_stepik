from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time

link = 'https://suninjuly.github.io/math.html'
browser = webdriver.Chrome()
browser.get(link)

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


x_element = browser.find_element(By.ID, 'input_value')
x = x_element.text
y = calc(x)

answer = browser.find_element(By.ID, 'answer')
answer.send_keys(y)

checkbox = browser.find_element(By.ID, 'robotCheckbox')
checkbox.click()

radiobutton = browser.find_element(By.ID, 'robotsRule')
radiobutton.click()
#time.is locals()
#time.sleep(10)

browser.find_element(By.CSS_SELECTOR, 'btn-default').click()

time.sleep(5)
browser.quit()