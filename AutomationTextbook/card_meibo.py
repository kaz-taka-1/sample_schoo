import csv, openpyxl as excel
in_file = 'meibo.csv'
template_file = 'card-template.xlsx'
save_file = 'card-meibo.xlsx'

def read_csv(fname):
    with open(fname, encoding='sjis') as f:
        reader = csv.reader(f)
        next(reader)
        return[v for v in reader]

book = excel.load_workbook(template_file)
sheet_tpl = book['Sheet']
for i, person in enumerate(read_csv(in_file)):
    name, zipno, addr = person
    idx = i % 10
    if idx == 0:
        sheet = book.copy_worksheet(sheet_tpl)
        sheet.title = 'Page'+str(idx)

    row = 4 * (idx % 5) + 2
    col = 2 * (idx // 5) + 2
    sheet.cell(row=row + 0, column=col, value=name)
    sheet.cell(row=row + 1, column=col, value=zipno)
    sheet.cell(row=row + 2, column=col, value=addr)

book.remove(sheet_tpl)
book.save(save_file)
