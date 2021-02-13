def numbers_searching(*args):
    biggest_num = max(args)
    smallest_num = min(args)
    missing_list = []
    duplicate_list = []

    numbers = range(smallest_num, biggest_num + 1)
    new_list = []

    for num in args:
        if num in numbers and num not in new_list:
            new_list.append(num)
        else:
            duplicate_list.append(num)

    for n in numbers:
        if n not in args:
            missing_list.append(n)
    duplicate_list = sorted(set(duplicate_list))

    missing_list.append(duplicate_list)

    return missing_list




print(numbers_searching(1, 2, 4, 2, 5, 4))

print(numbers_searching(5, 5, 9, 10, 7, 8, 7, 9))

print(numbers_searching(50, 50, 47, 47, 48, 45, 49, 44, 47, 45, 44, 44, 48, 44, 48))