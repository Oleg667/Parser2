#https://metanit.com/python/tkinter/2.9.php

import tkinter

import pandas as pd
import json

import openpyxl
import time
import re





from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException
from openpyxl.utils import get_column_letter

from tkinter import *
from tkinter.messagebox import showinfo

def list_parser():# Получаем список листов из файла эксель

    wb = openpyxl.reader.excel.load_workbook(filename="PRICE2022.xlsx", data_only=True)  # открываем файл с переменными

    list_par = wb.sheetnames# список листов
    del list_par[0] # Удалеям имя первого (нулевого) листа с контрольным прайсом

    return (list_par)



root = Tk() # класс окна

root.title("ПАРСЕР ЛКМ SYMPHONY") #текст в шапке окна
root.geometry("500x500") # размер окна

photo = tkinter.PhotoImage(file='logofkm.png') # лого в шапке окна
root.iconphoto(False,photo)

download_label = Label(root, text = 'Выберите что будем проверять', font=35) # текст в окне
download_label.pack(pady = 20)





# создаем список

list_par=list_parser() #обращаемся к функции для получения списка листов для парсинга

#languages = ["Python", "JavaScript", "C#", "Java"]
languages_var = Variable(value=list_par)

languages_listbox = Listbox(listvariable=languages_var)

languages_listbox.pack(anchor=NW, fill=X, padx=5, pady=5)




# Кнопка
button = Button(root,text=" Запустить Парсер ", font = 40, command= list_parser) # создаем кнопку
button.pack(side = BOTTOM, pady = 40) # расположение кнопки, отступ по оси У




root.mainloop() # запуск визуализации окна


#

# wb.active = 1 # делаем активной вторую страницу  там где Бафус
# sheet_parser = wb.active # копируем страницу в переменную
# wb.active = 0 # делаем активной первую страницу с прайсом РРЦ
# sheet_active = wb.active