import time
import math
from selenium import webdriver
from selenium.webdriver.common.by import By




def calc(num1, num2):
    return str(str(int(num1)+int(num2)))

try:
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    a = browser.find_element(By.XPATH, "//*[@id='num1']")
    b = browser.find_element(By.ID, "num2")
    y = int(a.text)+int(b.text)

    browser.find_element(By.XPATH, "//*[@id='dropdown']").click()
    browser.find_element(By.XPATH, "//*[@value='" + str(y) + "']").click()

    button = browser.find_element(By.XPATH, '//button')
    button.click()

finally:
    time.sleep(10)
    browser.quit() 
