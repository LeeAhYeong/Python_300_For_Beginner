'''file_name = "보고서.xlsx"
file_name = file_name.endswith(('xlsx', 'xls'))
print(file_name)'''

file_name = "보고서.xlsx"
if file_name.endswith(('xlsx', 'xls')):
    print('맞습니다')
else:
    print('아닙니다')