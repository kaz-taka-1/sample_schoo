import openpyxl as excel
book = excel.load_workbook("hello.xlsx")
sheet = book.worksheets[0]
cell = sheet["A1"]
print(cell.value)
