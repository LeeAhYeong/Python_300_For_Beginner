nums = [1, 2, 3, 4, 5, 6, 7]
min_num = min(nums)
max_num = max(nums)
print('max:',max_num)
print('min:',min_num)

def max_cus(data_list):
    max_value = data_list[0]

    for data in data_list:
        if data > max_value:
            max_value = data

    return max_value

nums = [-1,-2,-3,-4,-5,-6]
print(max_cus(nums))