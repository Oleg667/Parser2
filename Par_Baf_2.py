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

# # Находим поле ввода текста и вводим текст
# search_input = browser.find_element(By.ID, "a11y-search-input")
# search_input.send_keys("Python Junior")

# Найдем цену на 1л
header_vacancies = browser.find_element(By.CSS_SELECTOR, '[span.data-orig-price.class]')
header_name = header_vacancies.text


# # Находим кнопку "Найти работу"
# search_button = browser.find_element(By.CSS_SELECTOR, 'button[data-qa="search-button"]')
# search_button.click()

# # Найдем заголовок
# header_vacancies = browser.find_element(By.CSS_SELECTOR, '[data-qa="vacancies-search-header"]')
# header_name = header_vacancies.text

# Форматируем строку с помощью регулярного выражения
vacancies_count = header_name
# vacancies_count = re.sub(r"\D", "", header_name)
print(f"Цена: {vacancies_count}")
print(header_vacancies)

# Ждем
time.sleep(2)

# Закрываем браузер
browser.close()