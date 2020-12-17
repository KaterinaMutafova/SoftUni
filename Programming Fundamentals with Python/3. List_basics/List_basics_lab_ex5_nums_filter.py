n_times = int(input())

even_list = []
odd_list = []
negative_list = []
positive_list = []


for i in range(n_times):
    num = int(input())
    if num % 2 == 0:
        even_list.append(num)
    else:
        odd_list.append(num)
    if num >= 0:
        positive_list.append(num)
    else:
        negative_list.append(num)

command = input()

if command == "even":
    print(even_list)
elif command == "odd":
    print(odd_list)
elif command == "positive":
    print(positive_list)
elif command == "negative":
    print(negative_list)

