#https://metanit.com/python/tkinter/2.9.php

import tkinter
import openpyxl


from tkinter import ttk
from tkinter import *
from Par_Baf_2 import *



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

def Checkbutton_1(): # Обработка чекбокса о выводе в файл только цен ниже контрольных или всех
    global violation
    if var1.get() == 1:
        violation = 1
    else:
        violation = 0
    print(var1.get())

def Checkbutton_2(): # Обработка чекбокса о допустимой скидке 5% при контроле цены
    global skidka_5 # если скидки нет то рано 1 если скидка есть то 0,95 (множитель для контрольной цены)
    if var2.get() == 1:
        skidka_5 = 0,95
    else:
        skidka_5 = 1

   print(var2.get())

selected_langs1 = list_parser()

root = Tk() # класс окна

root.title("ПАРСЕР ЛКМ SYMPHONY") #текст в шапке окна
root.geometry("500x500") # размер окна

photo = tkinter.PhotoImage(file='logofkm.png') # лого в шапке окна
root.iconphoto(False,photo)

download_label = Label(root, text = 'Выберите сайты для проверки', font=35) # текст в окне
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
button = Button(root,text=" Запустить Парсер ", font = 40, command =lambda: Parser_master(selected_langs1)) # создаем кнопку, через lambda:  иначе сразу запускается Parser_master не дожидаясь нажатия
button.pack(side = BOTTOM, pady = 40) # расположение кнопки, отступ по оси У

# Чекбоксы

var1 = tkinter.StringVar() # Чекбокс о выводе в файл только цен ниже контрольных
var1.set("ON")
checkbutton_active = tkinter.Checkbutton(root, text="Выводить в файл только нарушение цены", variable=var1, command=Checkbutton_1)
checkbutton_active.pack(side = BOTTOM )

var2 = tkinter.StringVar() # Чекбокс о допустимой скидке 5% при контроле цены
var2.set("OFF")
checkbutton_active = tkinter.Checkbutton(root, text="Допустима скидка от контрольной цены 5%", variable=var2, command=Checkbutton_2)
checkbutton_active.pack(side = BOTTOM )


root.mainloop() # запуск визуализации окна

#print(selected_langs1)


