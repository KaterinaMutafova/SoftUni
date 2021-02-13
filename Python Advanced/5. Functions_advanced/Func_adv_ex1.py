def filter_even(nums_list):
    nums_list = list(filter(lambda x: (x % 2 == 0), nums_list))
    print(nums_list)


numbers = [int(el) for el in input().split()]
filter_even(numbers)
