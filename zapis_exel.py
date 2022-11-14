import pandas as pd
import json


# Создаем заголовок таблицы
data={ 'Cod': ['1'],
       'NAME SKU': ['2'],
       'Prise in website': ['3'],
       'recommended retail price list': ['4'],
       'comparison': ['5'],
       'URL': ['6']  }

df = pd.DataFrame(data) #Создаем двумерную таблицу отчета
#
# print(df)

#Гененрируем  новую строку

row = '{"Cod":["111"], "NAME SKU": ["222"], "Prise in website": ["333"], "recommended retail price list": ["444"], "comparison": ["555"], "URL": ["666"]}'



new_row = json.loads(row) # Преобразуем строку в словарь

#print(new_row)

new_row_fr = pd.DataFrame(new_row) # создаем из строки двумерную таблицу

#print(new_row_fr)

df = pd.concat([df, new_row_fr], ignore_index=True) # добавляем строку в таблицу отчета

print(df)

#df.to_excel('./bafus.xlsx', index=False) # Записываем файл с созданными значениями


