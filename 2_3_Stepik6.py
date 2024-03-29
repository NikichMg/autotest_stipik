import math
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))
try:
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    button1 = browser.find_element(By.XPATH, "//button")
    button1.click()

    first_window = browser.window_handles[0]
    second_window = browser.window_handles[1]

    browser.switch_to.window(second_window)

    x_elements = browser.find_element(By.XPATH, "//*[@id='input_value']")
    y = calc(x_elements.text) 
    input1 = browser.find_element(By.XPATH, '//*[@id="answer"]')
    input1.send_keys(y)

    button2 = browser.find_element(By.XPATH, '//button')
    button2.click()

finally:
    time.sleep(10)
    browser.quit()
