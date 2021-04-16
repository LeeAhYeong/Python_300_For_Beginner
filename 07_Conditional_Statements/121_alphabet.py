character = input('문자 한 개를 입력하세요!: ')

if character.islower() == True:
    character = character.upper()
else:
    character = character.lower()

print(character)


  
'''
문자열을 대문자로 변경 하는 함수 string.upper()
문자열을 소문자로 변겨 하는 함수 string.lower()
문자가 대문자인지 확인하는 함수 string.isupper()
문자가 소문자인지 확인하는 함수 string,islower() '''