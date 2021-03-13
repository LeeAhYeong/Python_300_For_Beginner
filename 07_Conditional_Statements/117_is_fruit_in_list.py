fruit = ["사과", "포도", "홍시"]
user = input('좋아하는 과일은? ')

for data in fruit:
    if data == user:
        print('정답입니다.')
        break
    else:
        print('오답입니다.')
        break

if user in fruit:
    print('정답입니다.')
else:
    print('오답입니다.')