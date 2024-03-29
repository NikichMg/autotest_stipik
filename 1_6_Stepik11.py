from selenium import webdriver
from selenium.webdriver.common.by import By
import time


link = "http://suninjuly.github.io/registration1.html"
browser = webdriver.Chrome()
browser.get(link)

# Ваш код, который заполняет обязательные поля
input1 = browser.find_element(By.XPATH, '//label[text()="First name*"]/following-sibling::input')
input1.send_keys("Ivan")
input3 = browser.find_element(By.XPATH, '//label[text()="Last name*"]/following-sibling::input')
input3.send_keys("Petrov")
input2 = browser.find_element(By.XPATH, '//*[contains(@placeholder, "Input your email")]')
input2.send_keys("petrob@gmail.com")


# Отправляем заполненную форму
button = browser.find_element(By.CSS_SELECTOR, "button.btn")
button.click()

# Проверяем, что смогли зарегистрироваться
# ждем загрузки страницы
time.sleep(1)

# находим элемент, содержащий текст
welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
# записываем в переменную welcome_text текст из элемента welcome_text_elt
welcome_text = welcome_text_elt.text

# с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
print(welcome_text) 
