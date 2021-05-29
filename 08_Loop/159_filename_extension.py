'''
리스트 = ['intra.h', 'intra.c', 'define.h', 'run.py']

for item in 리스트:
    if item.split('.')[1] == 'h':
        print(item)
    
# endweith("")

'''

리스트 = ['intra.h', 'intra.c', 'define.h', 'run.py']

for item in 리스트:
    if item.endswith('h') == True:
        print(item)