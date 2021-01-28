# lower method 사용
ticker = "BTC_KRW"
ticker = ticker.lower()
print(ticker)

#2 lower method 직접 구현
ticker = "BTC_KRW"
result =''

for data in ticker:
    if 'A' <= data <= 'Z':
        result += chr(ord(data)+32)
    else:
        result += data
print(result)