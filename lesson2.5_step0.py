from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time


'''Открыть страницу http://suninjuly.github.io/explicit_wait2.html
Дождаться, когда цена дома уменьшится до $100 (ожидание нужно установить не меньше 12 секунд)
Нажать на кнопку "Book"
Решить уже известную нам математическую задачу (используйте ранее написанный код) и отправить решение'''
link_selenium_lessons = 'https://stepik.org/lesson/236205/step/3?unit=208637'

link = 'https://stepik.org/course/575/promo'


browser = webdriver.Chrome()
# link = 'https://stepik.org/'
browser.get(link)

WebDriverWait(browser, 7).until(EC.element_to_be_clickable((By.ID, "ember54")))
# browser.execute_script("window.scrollTo(0,document.body.scrollHeight);")
time.sleep(2)
browser.find_element(By.ID, 'ember54').click()

# browser.implicitly_wait(5)
time.sleep(6)
# browser.switch_to.alert
# browser.find_element(By.ID, 'id_login_email').send_keys('genrymorli@gmail.com')
# browser.find_element(By.ID, 'id_login_password').send_keys('dima17dima')

browser.find_element(By.CLASS_NAME, 'sign-form__btn.button_with-loader ').click()

browser.get(link_selenium_lessons)

time.sleep(5)
browser.quit()


