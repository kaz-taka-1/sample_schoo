import openpyxl as excel

book = excel.Workbook()
sheet = book.active

sheet["A1"] = "2023/01/01"
sheet["B1"] = '=TEXT(A1,"ggge年m月d日")'

book.save("susiki.xlsx")
