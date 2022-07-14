import math
import time
from selenium import webdriver
from selenium.webdriver.common.by import By


try:
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element(By.XPATH, "//*[@id='treasure']")
    x_element_val = x_element.get_attribute("valuex")
    x = x_element_val
    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))
    y = calc(x)

    input1 = browser.find_element(By.XPATH, "//*[@id='answer']")
    input1.send_keys(y)
    option1 = browser.find_element(By.XPATH, "//*[@id='robotCheckbox']")
    option1.click()
    option2 = browser.find_element(By.XPATH, "//*[@id='robotsRule']")
    option2.click()
    button = browser.find_element(By.XPATH, "//button")
    button.click()

finally:
    time.sleep(10)
    browser.quit()
