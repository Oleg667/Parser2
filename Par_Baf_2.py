import re
import time
import chromedriver_binary

from selenium import webdriver
from selenium.webdriver.common.by import By


#  Создаем браузер
browser = webdriver.Chrome()
browser.maximize_window()

# Открываем сайт
browser.get("https://www.bafus.ru/200100782/") #открываем страницу Евролайф 1л база А


# Найдем цену на 1л
price = browser.find_elements(By.XPATH, '//span[@class="sht-price"][1]')
price_n = price[1].text

# Форматируем строку с помощью регулярного выражения
print(f"Цена за 1 л: {price_n}")



# Находим кнопку "3л" и нажимаем её
search_button3 = browser.find_element(By.XPATH, '/html/body/div[4]/div[1]/div[2]/div/div[1]/main/div[1]/div[2]/div[1]/div/div/div/section/div/ul/li[1]/div[2]/div/div/div[2]/div/a')
search_button3.click()

# Найдем цену на 3 л
header_vacancies = browser.find_elements(By.XPATH, '//span[@class="sht-price"][1]')
header_name = header_vacancies[1].text

# Форматируем строку с помощью регулярного выражения
vacancies_count = header_name
print(f"Цена за 3 л: {vacancies_count}")


# # Находим кнопку "10л" и нажимаем её
search_button10 = browser.find_element(By.XPATH, '/html/body/div[4]/div[1]/div[2]/div/div[1]/main/div[1]/div[2]/div[1]/div/div/div/section/div/ul/li[1]/div[2]/div/div/div[3]/div/a')
search_button10.click()

# Найдем цену на 10л
price = browser.find_element(By.XPATH, '/html/body/div[4]/div[1]/div[2]/div/div[1]/main/div[1]/div[2]/div[2]/aside/div/div[1]/table[1]/tbody/tr/td/span[1]')
price_n = price.text

# Печатпем цену
print(f"Цена за 10 л: {price_n}")


# Ждем
time.sleep(2)

# Закрываем браузер
#browser.close()