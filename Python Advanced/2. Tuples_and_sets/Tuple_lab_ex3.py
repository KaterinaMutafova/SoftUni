number = int(input())

name_list = []
for n in range(number):
    name = input()
    name_list.append(name)

name_set = set(name_list)

for nam in name_set:
    print(nam)
