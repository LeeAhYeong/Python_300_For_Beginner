money = input('입력: ')
money = money.split()

if money[1] == '달러':
    money[0] = int(money[0]) * 1167
elif money[1] == '엔':
    money[0] = int(money[0]) * 1.096
elif money[1] == '유로':
    money[0] = int(money[0]) * 1268
elif money[1] == '위안':
    money[0] = int(money[0]) * 171
else:
    print('잘못된 통화명을 입력하셨습니다.')

print(money[0], '원', sep = '')


