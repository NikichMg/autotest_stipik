from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os


try:
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element(By.XPATH, "//*[@name='firstname']")
    input1.send_keys('Ivan')

    input2 = browser.find_element(By.XPATH, "//*[@name='lastname']")
    input2.send_keys('Ivanov')

    input3 = browser.find_element(By.XPATH, "//*[@name='email']")
    input3.send_keys('Ivanov@ivanov.ru')

    # находим путь до текущей папки
    current_dir = os.path.abspath(os.path.dirname(__file__))

    # достраиваем его до пути до нужного файла
    file_path = os.path.join(current_dir, "test.txt")

    # посылаем этот файл
    file_button = browser.find_element(By.XPATH, "//*[@id='file']") 
    file_button.send_keys(file_path)

    button = browser.find_element(By.XPATH, "//button")
    button.click()



finally:
    time.sleep(10)
    browser.quit





