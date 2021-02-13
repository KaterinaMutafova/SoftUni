def list_manipulator(*args):
    list_nums = args[0]
    command = args[1]
    position = args[2]
    if command == "add":
        addition_nums = list(args[3:])
        if position == "beginning":
            addition_nums.extend(list_nums)
            list_nums = addition_nums
        elif position == "end":
            list_nums.extend(addition_nums)
    elif command == "remove":
        if position == "beginning":
            if len(args) > 3:
                number_to_remove = (args[3:])
                for _ in range(number_to_remove[0]):
                    list_nums.remove(list_nums[0])
            else:
                list_nums.remove(list_nums[0])
        elif position == "end":
            if len(args) > 3:
                number_to_remove = (args[3:])
                for _ in range(number_to_remove[0]):
                    list_nums.pop()
            else:
                list_nums.pop()


    return list_nums





# print(list_manipulator([1,2,3], "remove", "end"))
# print(list_manipulator([1,2,3], "remove", "beginning"))
print(list_manipulator([1,2,3], "add", "beginning", 20))
print(list_manipulator([1,2,3], "add", "end", 30))
print(list_manipulator([1,2,3], "remove", "end", 2))
print(list_manipulator([1,2,3], "remove", "beginning", 2))
print(list_manipulator([1,2,3], "add", "beginning", 20, 30, 40))
print(list_manipulator([1,2,3], "add", "end", 30, 40, 50))

