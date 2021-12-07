import shutil
import glob
import openpyxl
import re
import os
try:
    shutil.copytree('./before','./after')
except FileExistsError as e:
    print('すでにafterファイルが存在します')
files = glob.glob('./after/**',recursive=True)



for file in files:
    if '.xlsx' in file:
        return True
    else:
        return False

invoice_sheet_name='請求書'
wb = openpyxl.load_workbook(file)
if invoice_sheet_name in wb.sheetnames:
    return True
else:
    return False

corporate_name_cell='B2'
invoice_corporate_name=wb[invoice_sheet_name][corporate_name_cell].value

invoice_created_date_cell='B5'
value=wb[invoice_sheet_name][invoice_created_date_cell].value

invoice_created_date_regex = re.complie(r'\d\d\d\d/\d\d')
invoice_created_date_match = invoice_created_date_regex.search(value)
invoice_created_date=invoice_created_date_match.group()

formatted_date='{0}年{1}月'.format(invoice_created_date[0:4],invoice_created_date[5:7])
file_name='請求書_{0}様_{1}'.format(invoice_corporate_name,formatted_date)
file_name_with_ext=file_name+'.xlsx'

dir_path='./after/'+invoice_corporate_name
os.makedirs(dir_path,exist_ok=True)
shutil.move(file,new_dir_path+'/'+new_file_name)


