from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math
import time

'''Открыть страницу http://suninjuly.github.io/explicit_wait2.html
Дождаться, когда цена дома уменьшится до $100 (ожидание нужно установить не меньше 12 секунд)
Нажать на кнопку "Book"
Решить уже известную нам математическую задачу (используйте ранее написанный код) и отправить решение'''

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

browser = webdriver.Chrome()
link = 'http://suninjuly.github.io/explicit_wait2.html'
browser.get(link)

WebDriverWait(browser, 13).until(EC.text_to_be_present_in_element((By.ID, "price"), '$100'))
browser.execute_script("window.scrollTo(0,document.body.scrollHeight);")
bookbtn = browser.find_element(By.ID, 'book')
WebDriverWait(browser,2).until(EC.element_to_be_clickable(bookbtn))
bookbtn.click()






x = browser.find_element(By.ID, 'input_value').text
print(x)
answer = math.log(abs(12 * math.sin(int(x))))
browser.find_element(By.ID, 'answer').send_keys(str(answer))
print(answer)

browser.implicitly_wait(5)

butt = browser.find_element(By.ID, 'solve')
WebDriverWait(browser, 5).until(EC.element_to_be_clickable(butt))
butt.click()

time.sleep(1)
browser.switch_to.alert
alert = browser.switch_to.alert.text.split()[-1]
print(alert)


browser.quit()


