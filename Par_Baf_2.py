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
header_vacancies = browser.find_elements(By.XPATH, '//span[@class="sht-price"][1]')
header_name = header_vacancies[1].text
#print(header_name)


# # Находим кнопку "3л" и нажимаем её
search_button3 = browser.find_elements(By.PARTIAL_LINK_TEXT, 'www.bafus.ru/200100780/'[0])
#print(search_button)
# search_button3 = search_button[1]
search_button3.click()

# # Найдем заголовок
# header_vacancies = browser.find_element(By.CSS_SELECTOR, '[data-qa="vacancies-search-header"]')
# header_name = header_vacancies.text

# Форматируем строку с помощью регулярного выражения
vacancies_count = header_name
# vacancies_count = re.sub(r"\D", "", header_name)
print(f"Цена: {vacancies_count}")
# print(header_vacancies)

# Ждем
time.sleep(2)

# Закрываем браузер
browser.close()