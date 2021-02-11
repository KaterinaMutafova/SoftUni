start = int(input())
end = int(input())


nums_list = []
for num in range(2, 10 + 1):
    for el in range(start, end + 1):
        if el % num == 0:
            nums_list.append(el)

print(list(set(nums_list)))
