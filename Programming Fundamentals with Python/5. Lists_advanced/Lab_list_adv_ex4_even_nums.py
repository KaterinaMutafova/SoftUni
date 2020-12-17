string_nums = input()
list_nums = string_nums.split(", ")


int_nums = list(map(lambda num: int(num), list_nums))

even_nums = [index for index in range(len(int_nums)) if int_nums[index] % 2 == 0]

print(even_nums)
