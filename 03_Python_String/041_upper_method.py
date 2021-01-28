# upper method 사용
ticker = "btc_krw"
ticker = ticker.upper()
print(ticker)

# upper method 직접 구현
# ord() > char > int / chr() : int > char
# a 97 A 65
ticker = "btc_krw"
result = ''
for data in ticker:
    if ord('a') <= ord(data) <= ord('z') : # and (&&)
        result += chr(ord(data)-32)
    else :
        result += data

print(result)

