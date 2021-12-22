import openpyxl as xl
book = xl.Workbook()
sheet = book.active

def set_cell(cname, value, fmt):
    c = sheet[cname]
    c.value = value
    c.number_format = fmt

keta3_fmt = '#,##0'
sheet["A1"] = keta3_fmt
set_cell("B1", 12345, keta3_fmt)
set_cell("C1", 123456789, keta3_fmt)

cur_fmt = '"\"#,##0;"\"\\-#,##0'
sheet["A2"] = cur_fmt
set_cell("B2", 12345, cur_fmt)
set_cell("C2", -12345, cur_fmt)

num_fmt = '#,##0;[red]"▲ "#,##0'
sheet["A3"] = num_fmt
set_cell("B3", 12345, num_fmt)
set_cell("C3", -12345, num_fmt)

book.save("number_format2.xlsx")