numbers = tuple(map(float, input().split()))

dict_count = {}

for num in numbers:
    if num not in dict_count:
        dict_count[num] = 1
    else:
        dict_count[num] += 1

for key, value in dict_count.items():
    print(f"{key} - {value} times")



