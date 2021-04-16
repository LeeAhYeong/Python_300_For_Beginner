number = input("주민등록번호: ")
area_code = number[8:10]

if 0 <= int(area_code) <= 8:
    print("서울입니다.")
else:
    print("서울이 아닙니다.")