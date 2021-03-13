user = int(input('입력값:'))
num = user-20

if num < 0:
    print(0)
elif num > 255:
    print(255)
else:
    print(num)