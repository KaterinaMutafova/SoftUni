targets = input().split()

targets = list(map(int, targets))

data = input()


def shoot(nums, i, v):
    if 0 <= i <= len(nums):
        nums[i] = nums[i] - v
        if nums[i] <= 0:
            nums.pop(i)
    return nums

def add(nums, i, v):
    if 0 <= i < len(nums):
        nums.insert(i, v)
    else:
        print(f"Invalid placement!")
    return nums


def strike(nums, i, v):
    left_index = i - v
    right_index = i + v

    if left_index >= 0 and right_index < len(nums):
        left_part = nums[:left_index]
        right_part = nums[right_index+1:]
        nums = left_part + right_part
    else:
        print("Strike missed!")
    return nums


while not data == "End":
    command, index, value = data.split()
    index = int(index)
    value = int(value)

    if command == "Shoot":
        targets = shoot(targets, index, value)
    elif command == "Add":
        targets = add(targets, index, value)
    elif command == "Strike":
        targets = strike(targets, index, value)

    data = input()

print("|".join(str(i) for i in targets))



# Another way without functions:

# targets = input().split()
#
# targets = list(map(int, targets))
#
# data = input()
#
# while not data == "End":
#     command, index, value = data.split()
#     index = int(index)
#     value = int(value)
#
#     if command == "Shoot":
#         if index > len(targets) - 1:
#             pass
#         elif 0 <= index <= len(targets):
#             targets[index] = targets[index] - value
#             for i in targets:
#                 if i == 0 or i < 0:
#                     targets.remove(i)
#                 else:
#                     pass
#     elif command == "Add":
#         if 0 <= index < len(targets):
#             targets.insert(index, value)
#         else:
#             print(f"Invalid placement!")
#     elif command == "Strike":
#         left_index = index - value
#         right_index = index + value
#
#         if left_index >= 0 and right_index < len(targets):
#             left_part = targets[:left_index]
#             right_part = targets[right_index+1:]
#             targets = left_part + right_part
#         else:
#             print("Strike missed!")
#         # if index > len(targets) - 1:
#         #     pass
#
#     data = input()
#
# print("|".join(str(i) for i in targets))
