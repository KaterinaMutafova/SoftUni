def sort_numbers(nums_list):
    return sorted(nums_list)


numbers = [int(el) for el in input().split()]
print(sort_numbers(numbers))