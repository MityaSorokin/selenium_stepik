import  unittest
from selenium import webdriver
from selenium.webdriver.common.by import  By
import time

link1 = 'http://suninjuly.github.io/registration1.html'
link2 = 'http://suninjuly.github.io/registration2.html'
browser = webdriver.Chrome()

class TestUnittest (unittest.TestCase):
    def testRegistration1(self):
        browser.get(link1)
        message = "Congratulations! You have successfully registered!"
        browser.find_element(By.CSS_SELECTOR, 'div .first_block input.form-control.first').send_keys("Vasya")
        browser.find_element(By.CSS_SELECTOR, 'div .first_block input.form-control.second').send_keys("Pupkin")
        browser.find_element(By.CLASS_NAME, "form-control.third").send_keys("VasyaPupkin@mail.ge")

        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

        self.assertEqual(browser.find_element(By.TAG_NAME, "h1").text, message, "reg failed")
        print("passed 1")


    def testRegistration2(self):
        browser.get(link2)
        message = "Congratulations! You have successfully registered!"
        browser.find_element(By.CSS_SELECTOR, 'div .first_block input.form-control.first').send_keys("Vasya")
        browser.find_element(By.CSS_SELECTOR, 'div .first_block input.form-control.second').send_keys("Pupkin")
        browser.find_element(By.CLASS_NAME, "form-control.third").send_keys("VasyaPupkin@mail.ge")

        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

        self.assertEqual(browser.find_element(By.TAG_NAME, "h1").text, message, "registration failed!")
        print("passed 2")


if __name__ == "__main__": unittest.main()