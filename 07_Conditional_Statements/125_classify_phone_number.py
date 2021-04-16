#1
phone_number = input("휴대전화 번호 입력: ")

if phone_number[0:3] == "011":
    print("당신은 SKT 사용자 입니다.")
elif phone_number[0:3] == "016":
    print("당신은 KT 사용자 입니다.")
elif phone_number[0:3] == "019":
    print("당신은 LGU 사용자 입니다.")
elif phone_number[0:3] == "010":
    print("통신사 알수없음")
else:
    print("number error!")
    
#2
number = input("휴대전화 번호 입력: ")
num = number.split("-")[0]
if num == "011":
    com = "SKT"
elif num == "016":
    com = "KT"
elif num == "019":
    com = "LGU"
else:
    com = "알수없음"
print(f"당신은 {com} 사용자입니다.")
