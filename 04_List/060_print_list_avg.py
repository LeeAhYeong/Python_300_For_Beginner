nums = [1, 2, 3, 4, 5]
total = 0

for data in nums:
    total += data

avg = total / len(nums) # sum(nums) / len(nums)

print(avg)

'''
여러개를 기준대로 보겠다.
[0] > 0index
[1:3] > 1~3미만
[::-1] > 역순
'''