import os
import pandas as pd
folder_path = './excel/'
excel_files = os.listdir(folder_path)
list_sales_data = []
for excel_file in excel_files:
    if '売上' in excel_file:
        sales_data = pd.read_excel(folder_path + excel_file)
        list_sales_data.append(sales_data)

sales_channel = pd.read_excel(folder_path+'取引先流入元.xlsx')
sales_summary = pd.concat(list_sales_data, ignore_index=True)
sales_summary = pd.merge(sales_channel, sales_summary, on='取引先名')
sales_by_channel = sales_summary.groupby('流入元').sum()
print(sales_by_channel)

with pd.ExcelWriter('summary.xlsx')as writer:
    sales_summary.to_excel(writer, sheet_name='売上サマリー')
    sales_by_channel.to_excel(writer, sheet_name='流入ごとの売上')





