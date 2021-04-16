while True:
    score = int(input('score:'))
    
    if 0 <= score <= 100:
        break 
    else: # 예외처리
        print('Range exceeded!!!')

if 81 <= score <= 100:
    score = 'A'
elif 61 <= score < 81:
    score = 'B'
elif 41 <= score < 61:
    score = 'C'
elif 21 <= score < 41:
    score = 'D'
else:
    score = 'E'

print('grade is',score)
