리스트 = ['intra.h', 'intra.c', 'define.h', 'run.py']

for item in 리스트:
    file_extension = item.split('.')[1]
    if file_extension == 'h' or file_extension == 'c':
        print(item)