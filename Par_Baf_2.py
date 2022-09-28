import re
import time
import chromedriver_binary

from selenium import webdriver
from selenium.webdriver.common.by import By


#  Создаем браузер
browser = webdriver.Chrome()
browser.maximize_window()




# Парсинг цены. Входные данные:
# - адрес страницы
# - локатор цены
# - локатор наименования лкм
# - локатор тары
# - локатор базы
def open_get(url_1,xpath_prise,xpath_lkm,xpath_tara,xpath_baza): #открываем страницу по адресу и вытаскивает цену

        browser.get(url_1) #jnrhsnbt страницы по переданному адресу

        price = browser.find_element(By.XPATH, xpath_prise) # получение цены
        price_n = price.text # форматирование данных цены

        name = browser.find_element(By.XPATH, xpath_lkm)  # получение наименования
        name_n = name.text  # форматирование данных наименование

        tara = browser.find_element(By.XPATH, xpath_tara)  # получение тары
        tara_n = tara.text  # форматирование данных тары

        baza = browser.find_element(By.XPATH, xpath_baza)  # получение базы
        baza_n = baza.text  # форматирование данных базы
        browser.close() #закрываем браузер


        return(name_n,tara_n,baza_n,price_n)

url_1="https://www.bafus.ru/200100780/"
xpath_prise = '/html/body/div[4]/div[1]/div[2]/div/div[1]/main/div[1]/div[2]/div[2]/aside/div/div[1]/table[1]/tbody/tr/td/span[1]'
xpath_lkm = '/html/body/div[4]/div[1]/div[2]/div/div[1]/main/div[1]/header/div/div/div/h1'
xpath_tara = '/html/body/div[4]/div[1]/div[2]/div/div[1]/main/div[1]/div[2]/div[1]/div/div/div/section/div/ul/li[2]/div[2]/div/div/div[1]/div/span'
xpath_baza = '/html/body/div[4]/div[1]/div[2]/div/div[1]/main/div[1]/div[2]/div[1]/div/div/div/section/div/ul/li[1]/div[2]/div/div/div[2]/div/span'

print(open_get(url_1,xpath_prise,xpath_lkm,xpath_tara,xpath_baza))

#print(yyy)
#print(name_n, tara_n, price_n)

# Найдем цену на 1л
# price = browser.find_elements(By.XPATH, '//span[@class="sht-price"][1]')


# # Форматируем строку с помощью регулярного выражения
# print(f"Цена за 1 л: {price_n}")
#
#
#
# # Находим кнопку "3л" и нажимаем её
# search_button3 = browser.find_element(By.XPATH, '/html/body/div[4]/div[1]/div[2]/div/div[1]/main/div[1]/div[2]/div[1]/div/div/div/section/div/ul/li[1]/div[2]/div/div/div[2]/div/a')
# search_button3.click()
#
# # Найдем цену на 3 л
# header_vacancies = browser.find_elements(By.XPATH, '//span[@class="sht-price"][1]')
# header_name = header_vacancies[1].text
#
# # Форматируем строку с помощью регулярного выражения
# vacancies_count = header_name
# print(f"Цена за 3 л: {vacancies_count}")
#
#
# # # Находим кнопку "10л" и нажимаем её
# search_button10 = browser.find_element(By.XPATH, '/html/body/div[4]/div[1]/div[2]/div/div[1]/main/div[1]/div[2]/div[1]/div/div/div/section/div/ul/li[1]/div[2]/div/div/div[3]/div/a')
# search_button10.click()
#
# # Найдем цену на 10л
# price = browser.find_element(By.XPATH, '/html/body/div[4]/div[1]/div[2]/div/div[1]/main/div[1]/div[2]/div[2]/aside/div/div[1]/table[1]/tbody/tr/td/span[1]')
# price_n = price.text
#
# # Печатпем цену
# print(f"Цена за 10 л: {price_n}")
#
#
# # Ждем
# time.sleep(2)
#
# # Закрываем браузер
# #browser.close()