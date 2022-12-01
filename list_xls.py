#https://metanit.com/python/tkinter/2.9.php

import tkinter
import openpyxl


from tkinter import ttk
from tkinter import *



def list_parser():# Получаем список листов из файла эксель

    wb = openpyxl.reader.excel.load_workbook(filename="PRICE2022.xlsx", data_only=True)  # открываем файл с переменными

    list_par = wb.sheetnames# список листов
    del list_par[0] # Удалеям имя первого (нулевого) листа с контрольным прайсом

    return (list_par)

def selected(event): # Обработка выделенных строк в списке
    selected_indices = languages_listbox.curselection() # получаем индексы выделенных элементов
    selected_langs = ",".join([languages_listbox.get(i) for i in selected_indices])# получаем сами выделенные элементы
    msg = f"вы выбрали: {selected_langs}"
    selection_label["text"] = msg
    global selected_langs1  # переменная хранит список выбранных магазинов (названия листов) для проверки
    selected_langs1 = ([languages_listbox.get(i) for i in selected_indices])



root = Tk() # класс окна

root.title("ПАРСЕР ЛКМ SYMPHONY") #текст в шапке окна
root.geometry("500x500") # размер окна

photo = tkinter.PhotoImage(file='logofkm.png') # лого в шапке окна
root.iconphoto(False,photo)

download_label = Label(root, text = 'Выберите что будем проверять', font=35) # текст в окне
download_label.pack(pady = 20)





# создаем список

list_par=list_parser() #обращаемся к функции для получения списка листов для парсинга
languages_var = Variable(value=list_par)

selection_label = ttk.Label()
selection_label.pack(anchor=NW, fill=X, padx=5, pady=5)

languages_listbox = Listbox(listvariable=languages_var, selectmode=EXTENDED) # Создаем список, selectmode=EXTENDED позволяет выделять несколько строк
languages_listbox.pack(anchor=NW, fill=X, padx=5, pady=5)#размещаем список в окне
languages_listbox.bind("<<ListboxSelect>>", selected) #ля обработки выбора элементов в Listbox необходимо прикрепить функцию обработки к событию <<ListboxSelect>> с помощью метода bind:




# Кнопка
button = Button(root,text=" Запустить Парсер ", font = 40, command= list_parser) # создаем кнопку
button.pack(side = BOTTOM, pady = 40) # расположение кнопки, отступ по оси У




root.mainloop() # запуск визуализации окна

print(selected_langs1)
#

# wb.active = 1 # делаем активной вторую страницу  там где Бафус
# sheet_parser = wb.active # копируем страницу в переменную
# wb.active = 0 # делаем активной первую страницу с прайсом РРЦ
# sheet_active = wb.active
