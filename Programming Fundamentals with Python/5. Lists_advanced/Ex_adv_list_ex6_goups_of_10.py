list_of_nums = [int(el) for el in (input().split(", "))]

group_index = 1

while len(list_of_nums) > 0:
    new_group_list = []
    for el in list_of_nums:
        if el <= group_index * 10:
            new_group_list.append(el)
    for new_el in new_group_list:
        if new_el in list_of_nums:
            list_of_nums.remove(new_el)
    print(f"Group of {group_index * 10}'s: {new_group_list}")
    group_index += 1

















# list_10 = []
# list_20 = []
# list_30 = []
# list_40 = []
# list_50 = []
#
# for i in list_of_nums:
#     if int(i) <= 10:
#         list_10.append(int(i))
#     elif int(i) <= 20:
#         list_20.append(int(i))
#     elif int(i) <= 30:
#         list_30.append(int(i))
#     elif int(i) <= 40:
#         list_40.append(int(i))
#     elif int(i) <= 50:
#         list_50.append(int(i))
#
# print(f"Group of 10's: {list_10}")
# print(f"Group of 20's: {list_20}")
# print(f"Group of 30's: {list_30}")
# print(f"Group of 40's: {list_40}")
# print(f"Group of 50's: {list_50}")


