import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math

# функция, которая находит значение выражения при заданном x
def calc(x):
	return str( math.log (abs ( 12 * math.sin( x ) ) ) )

try:
	# переходим на нужную страницу
	browser = webdriver.Chrome()
	link = "http://suninjuly.github.io/explicit_wait2.html"
	browser.get(link)

	# находим цену дома и ждем, пока она не станет 10 000 RUR, бронируем
	button = browser.find_element(By.XPATH,"//*[@id='book']")
	price = WebDriverWait(browser, 12).until(
		EC.text_to_be_present_in_element((By.ID, "price"), "$100")
	)
	button.click()

	# находим значение x для выполнения задания
	x_string = browser.find_element(By.XPATH, '//*[@id="input_value"]')
	x_number = int( x_string.text )

	# высчитываем результат для задания
	answer = calc(x_number)

	# вводим результат в поле ввода
	input_answer = browser.find_element(By.XPATH, '//*[@id="answer"]')
	input_answer.send_keys(answer) 

	# нажимаем на кнопку
	send_button = browser.find_element(By.XPATH, "//*[@id='solve']")
	send_button.click()
finally:
	time.sleep(13)
	browser.quit()
