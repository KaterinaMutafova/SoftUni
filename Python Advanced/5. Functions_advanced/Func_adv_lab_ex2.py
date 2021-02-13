def round_nums(nums_list):
    result = [round(el) for el in nums_list]
    print(result)



nums = [float(el) for el in input().split()]
round_nums(nums)