numbers = input()
num_list_2 = []

num_list = numbers.split(" ")
for i in range(len(num_list)):
    num_list_2.append(-int(num_list[i]))

print(num_list_2)

