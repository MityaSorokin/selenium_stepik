from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time



'''Открыть страницу https://suninjuly.github.io/selects1.html
Посчитать сумму заданных чисел
Выбрать в выпадающем списке значение равное расчитанной сумме
Нажать кнопку "Submit"'''

link = 'https://suninjuly.github.io/selects1.html'
browser = webdriver.Chrome()
browser.get(link)
#browser.execute_script("document.title='Script executing';alert('Robots at work');")

# def calc(a, b):
#  return a + b

a = int(browser.find_element(By.ID, 'num1').text)
b = int(browser.find_element(By.ID, 'num2').text)
x = str(a + b)



for num, option in enumerate(browser.find_elements(By.TAG_NAME, 'option')):
  if option.get_attribute('value') == x:
    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_value(x)


#f"[value='{c}']"    "[value='1']"
"['value='1]"


time.sleep(2)

browser.find_element(By.XPATH, '//button').click()

time.sleep(2)
browser.quit()