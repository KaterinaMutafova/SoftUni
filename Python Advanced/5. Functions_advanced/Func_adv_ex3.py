def min_max_sum(nums_list):
    print(f"The minimum number is {min(nums_list)}")
    print(f"The maximum number is {max(nums_list)}")
    print(f"The sum number is: {sum(nums_list)}")



numbers = [int(el) for el in input().split()]
min_max_sum(numbers)