from selenium import webdriver
from selenium.webdriver.common.by import By
import time


browser = webdriver.Chrome()
link = 'http://suninjuly.github.io/alert_accept.html'
browser.get(link)
time.sleep(5)

browser.find_element(By.ID, "ember1040").click()
time.sleep(2)

