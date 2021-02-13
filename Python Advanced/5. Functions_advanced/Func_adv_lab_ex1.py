def convert_absolute_value(nums_list):
    result = [abs(el) for el in nums_list]
    print(result)


nums = [float(el) for el in input().split()]
convert_absolute_value(nums)

