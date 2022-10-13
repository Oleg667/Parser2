import openpyxl

wb = openpyxl.reader.excel.load_workbook(filename="PRICE2022.xlsx", data_only=True)

print(wb.sheetnames)

wb.active = 0

sheet = wb.active
print(sheet['A1'])

#for i in range(1,12):
#    print(sheet['A'+str(i)].value,sheet['B'+str(i)].value,sheet['C'+str(i)].value)