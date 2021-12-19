import openpyxl as excel
book = excel .load_workbook(
    "uriage.xlsx",data_only=True)
sheet = book.active
rows = sheet["A3":"F999"]
for row in rows:
    values = [cell.value for cell in row]
    if values[0] is None: break
    print(values)
