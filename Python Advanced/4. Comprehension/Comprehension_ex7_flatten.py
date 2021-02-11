numbers = input().split("|")

new_list =[]
for el in numbers:
    stripped_nums = (el.strip()).split()
    new_list.append(stripped_nums)


n = []

for j in new_list[::-1]:
    n.extend(j)

print(' '.join(n))




