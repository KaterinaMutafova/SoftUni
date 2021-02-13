def even_odd(*args):
    command = args[-1]
    nums_list = args[:-1]
    mapper = {"even": list(filter(lambda x: x % 2 == 0, nums_list)), "odd": list(filter(lambda x: x % 2 != 0, nums_list))}

    return mapper[command]



print(even_odd(1, 2, 3, 4, 5, 6, "even"))
print(even_odd(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "odd"))