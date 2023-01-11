from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:
    link = "http://suninjuly.github.io/registration2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # код, который осуществляет поиск обязательных полей и заполняет их
    '''elem = browser.find_elements(By.CSS_SELECTOR, 'div .first_block input.form-control')
    for i in elem:
        i.send_keys('stop war')'''

    # Ваш код, который заполняет обязательные три поля из первой ссылки
    element1 = browser.find_element(By.CSS_SELECTOR, 'div .first_block input.form-control.first')
    element1.send_keys('Name')
    # этот элемент не доступен для страницы "http://suninjuly.github.io/registration2.html" - получаем ошибку selenium.common.exceptions.NoSuchElementException
    element2 = browser.find_element(By.CSS_SELECTOR, 'div .first_block input.form-control.second')
    element2.send_keys('Surname')
    element3 = browser.find_element(By.CSS_SELECTOR, 'div .first_block input.form-control.third')
    element3.send_keys('email')

    time.sleep(1)

    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(4)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(2)
    # закрываем браузер после всех манипуляций
    browser.quit()


