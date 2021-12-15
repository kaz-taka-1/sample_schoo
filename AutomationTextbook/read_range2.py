import openpyxl as excel

book = excel.load_workbook("test100.xlsx")
sheet = book.active

for row in sheet["B2":"D4"]:
    r = []
    for cell in row:
        r.append(cell.value)
        print(r)
