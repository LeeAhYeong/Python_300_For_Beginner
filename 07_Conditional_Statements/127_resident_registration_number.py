number = input("주민등록번호: ")
number = number[7]

if number in ["1", "3"]:
    print("남자")
elif number in ["2", "4"]:
    print("여자")
else:
    print("잘못된 숫자입니다.")
