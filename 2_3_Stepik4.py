import time
import math
from selenium import webdriver
from selenium.webdriver.common.by import By

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))
try:
    link = "http://suninjuly.github.io/alert_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    button1 = browser.find_element(By.XPATH, "//*[@type='submit']")
    button1.click()
    confirm = browser.switch_to.alert
    confirm.accept()

    x_elements = browser.find_element(By.XPATH, "//*[@id='input_value']")
    y = calc(x_elements.text)
    input1 = browser.find_element(By.XPATH, "//*[@id='answer']")
    input1.send_keys(y)

    button2 = browser.find_element(By.XPATH, '//button')
    button2.click()
finally:
    time.sleep(10)
    browser.quit()




