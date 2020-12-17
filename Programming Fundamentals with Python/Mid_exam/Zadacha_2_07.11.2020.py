def reverse_nums(list_nums, start_index, count_nums):
    second_list = list_nums[start_index:start_index+count_nums]
    second_list.reverse()
    new_list = list_nums[0:start_index] + second_list + list_nums[start_index+count_nums:]
    return new_list


def sort_nums(list_nums, start_index, count_nums):
    second_list = list_nums[start_index:start_index + count_nums]
    second_list.sort()
    new_list = list_nums[0:start_index] + second_list + list_nums[start_index + count_nums:]
    return new_list


def remove_nums(list_nums, count_nums):
    for count in range(count_nums):
        list_nums.remove(list_nums[0])
    new_list = list_nums
    return new_list


numbers = input().split()
command = input()

while not command == "end":
    command = command.split()

    if command[0] == "reverse":
        start_i = int(command[2])
        count_n = int(command[4])
        numbers = reverse_nums(numbers, start_i, count_n)
    elif command[0] == "sort":
        start_i = int(command[2])
        count_n = int(command[4])
        numbers = sort_nums(numbers, start_i, count_n)
    elif command[0] == "remove":
        count_n = int(command[1])
        numbers = remove_nums(numbers, count_n)

    command = input()

if command == "end":
    numbers = ', '.join(numbers)
    print(numbers)




# numbers = input().split()
# new_list = ""
#
# while True:
#     command = input()
#     if command == "end":
#         break
#     command = command.split()
#
#     if command[0] == "reverse":
#         start_i = int(command[2])
#         count_n = int(command[4])
#         second_list = numbers[start_i:start_i + count_n]
#         second_list.reverse()
#         new_list = numbers[0:start_i] + second_list + numbers[start_i+count_n:]
#
#     elif command[0] == "sort":
#         start_i = int(command[2])
#         count_n = int(command[4])
#         second_list = numbers[start_i:start_i + count_n]
#         second_list.sort()
#         new_list = numbers[0:start_i] + second_list + numbers[start_i + count_n:]
#
#     elif command[0] == "remove":
#         count_n = int(command[1])
#         for count in range(count_n):
#             numbers.remove(numbers[0])
#         new_list = numbers
#
# if command == "end":
#     new_list = ', '.join(new_list)
#     print(new_list)








