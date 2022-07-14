from unittest import TestCase, main
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class TestSite(TestCase):
    def test_1_6_Stepik11(self):
        link = "http://suninjuly.github.io/registration1.html"
        browser = webdriver.Chrome()
        browser.get(link)
        input1 = browser.find_element(By.XPATH, "//*[@placeholder='Input your first name']")
        input1.send_keys("Ivan")
        input3 = browser.find_element(By.XPATH, "//*[@placeholder='Input your last name']")
        input3.send_keys("Petrov")
        input2 = browser.find_element(By.XPATH, "//*[@placeholder='Input your email']")
        input2.send_keys("petrob@gmail.com")
        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()
        time.sleep(1)
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        welcome_text = welcome_text_elt.text
        self.assertEqual(welcome_text, "Congratulations! You have successfully registered!")

    def test_1_6_Stepik11_2(self):
        link = "http://suninjuly.github.io/registration2.html"
        browser = webdriver.Chrome()
        browser.get(link)
        input1 = browser.find_element(By.XPATH, "//*[@placeholder='Input your first name']")
        input1.send_keys("Ivan")
        input3 = browser.find_element(By.XPATH, "//*[@placeholder='Input your last name']")
        input3.send_keys("Petrov")
        input2 = browser.find_element(By.XPATH, "//*[@placeholder='Input your email']")
        input2.send_keys("petrob@gmail.com")
        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()
        time.sleep(1)
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        welcome_text = welcome_text_elt.text
        self.assertEqual(welcome_text, "Congratulations! You have successfully registered!")



if __name__ == "__main__":
    main()
