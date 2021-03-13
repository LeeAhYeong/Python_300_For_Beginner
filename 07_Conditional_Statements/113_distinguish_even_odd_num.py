while True:
    num = int(input('숫자를 하나를 입력하세요! '))

    if num > 0:
        break
    else:
        print('1이상의 숫자를 입력하세요')

if num % 2 == 0:
    print('짝수')
else:
    print('홀수')