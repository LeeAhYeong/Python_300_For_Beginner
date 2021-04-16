zip_code = input("우편 번호: ")
zip_code = zip_code[:3]

if zip_code in ["010","011","012"]:
    print("강북구")
elif zip_code in ["014", "015", "016"]:
    print("도봉구")
else:
    print("노원구")

# 1번 : c, 변환명세(%c %s %d %f)
print("%d %d", num1, num2)

# 2번 : print(, +) 연결기호
print(num1, num2, num3) # num1 num2 num3 자료형 무관, 띄어쓰기(변수)
print(num1 + num2 + num3) # num1 num2 num3 같은 자료형, str()

# 3번 : F-String, 출력, string 만들때
print(F" {}asdfdf {} {}")