def command_odd_even(nums_list, command):
    even_list = list(filter(lambda x: x % 2 == 0, nums_list))
    odd_list = list(filter(lambda x: x % 2 != 0, nums_list))
    mapper = {"Even": sum(even_list) * len(nums_list), "Odd": sum(odd_list) * len(nums_list)}
    return mapper[command]


command = input()
numbers = list(map(int, input().split()))
print(command_odd_even(numbers, command))