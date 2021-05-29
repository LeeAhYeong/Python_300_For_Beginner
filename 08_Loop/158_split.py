리스트 = ['hello.py', 'ex01.py', 'intro.hwp']

for item in 리스트:
    split_word = item.split('.')
    print(split_word[0])