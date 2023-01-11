import os
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

'''Открыть страницу http://suninjuly.github.io/file_input.html
Заполнить текстовые поля: имя, фамилия, email
Загрузить файл. Файл должен иметь расширение .txt и может быть пустым
Нажать кнопку "Submit"'''


link = "http://suninjuly.github.io/file_input.html"
browser = webdriver.Chrome()
browser.get(link)

browser.find_element(By.NAME, 'firstname').send_keys('Antony')
browser.find_element(By.NAME, 'lastname').send_keys('Wild')
browser.find_element(By.NAME, 'email').send_keys('anwi@mail.com')

open('newfile.txt', 'a').close() # создаём , если отсутствует
curr_dir = os.path.abspath(os.path.dirname(__file__))
file_name = "newfile.txt"
file_path = os.path.join(curr_dir, file_name)
element = browser.find_element(By.NAME, "file")
element.send_keys(file_path) # сабмит файла
os.remove('newfile.txt')

curr_dir = os.path.abspath(os.path.dirname(__file__))
file_name = "test_text.txt"
file_path = os.path.join(curr_dir, file_name)

'''element = browser.find_element(By.CSS_SELECTOR, "[type='file']")
element.send_keys(file_path)'''

browser.find_element(By.CLASS_NAME, 'btn.btn-primary').click()

time.sleep(4)
