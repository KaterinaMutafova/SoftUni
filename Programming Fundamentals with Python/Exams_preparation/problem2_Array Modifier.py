list_nums = [int(el) for el in input().split()]

command = input()

while not command == "end":
    info = command.split()

    if info[0] == "swap":
        index_1 = int(info[1])
        index_2 = int(info[2])
        list_nums[index_1], list_nums[index_2] = list_nums[index_2], list_nums[index_1]

    elif info[0] == "multiply":
        index_1 = int(info[1])
        index_2 = int(info[2])
        list_nums[index_1] = list_nums[index_1] * list_nums[index_2]

    elif info[0] == "decrease":
        list_nums = list(map(lambda x: x - 1, list_nums))

    command = input()

string_list = [str(el) for el in list_nums]
print(', '.join(string_list))





