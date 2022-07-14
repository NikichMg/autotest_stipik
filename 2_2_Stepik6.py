import math
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

try:
    link = "http://suninjuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element(By.XPATH, "//*[@id='input_value']")
    x = x_element.text
    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))
    y = calc(x)

    input1 = browser.find_element(By.XPATH, "//*[@id='answer']")
    input1.send_keys(y)

    checkbox = browser.find_element(By.XPATH,"//*[@id='robotCheckbox']")
    #СКРИПТ ПОМОГАЮЩИЙ ЗА СКРОЛИТЬ до ОБЪЕКТА
    browser.execute_script("return arguments[0].scrollIntoView(true);", checkbox)
    checkbox.click()
    radiobutton = browser.find_element(By.XPATH, "//*[@id='robotsRule']")
    radiobutton.click()
    button = browser.find_element(By.XPATH, "//button")
    button.click()
finally:
    time.sleep(10)
    browser.quit()
