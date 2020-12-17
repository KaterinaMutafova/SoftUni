import sys
numbers = input()
n_to_remove = int(input())

list_of_numbers = numbers.split(" ")

for k in range(len(list_of_numbers)):
    list_of_numbers[k] = int(list_of_numbers[k])

previous_num = sys.maxsize
current_num = 0
current_minimum = sys.maxsize

for j in range(n_to_remove):
    current_minimum = sys.maxsize
    for i in range(len(list_of_numbers)):
        current_num = list_of_numbers[i]
        if current_num < current_minimum:
            current_minimum = current_num
        else:
            pass
        previous_num = current_num
    list_of_numbers.remove(current_minimum)

print(list_of_numbers)

