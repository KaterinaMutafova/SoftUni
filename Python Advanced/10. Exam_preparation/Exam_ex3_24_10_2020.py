from collections import deque


def best_list_pureness(*args):
    list_nums = args[0]
    k = args[1]
    list_nums = deque(list_nums)


    best_pureness = 0
    for i in range(k + 1):
        pureness = 0
        for index in range(len(list_nums)):
            pureness += index * list_nums[index]
        if pureness > best_pureness:
            best_pureness = pureness
            count_rootation_of_the_best = i

        list_nums.appendleft(list_nums.pop())
    return f"Best pureness {best_pureness} after {count_rootation_of_the_best} rotations"








# test = ([4, 3, 2, 6], 4)
# result = best_list_pureness(*test)
# print(result)

# test = ([7, 9, 2, 5, 3, 4], 3)
# result = best_list_pureness(*test)
# print(result)

test = ([1, 2, 3, 4, 5], 10)
result = best_list_pureness(*test)
print(result)

