# exchange {index} – splits the array after the given index, and exchanges the places of the two resulting sub-arrays.

def exchange(index, array_list):
    if 0 <= index < len(array_list):
        array_list_1 = array_list[:index+1]
        array_list_2 = array_list[index+1:]
        array_list = array_list_2 + array_list_1
        return array_list
    else:
        print("Invalid index")
        return array_list



# a_list = [1, 2, 3, 4, 5]
# print(exchange(2, a_list))

# max even/odd– returns the INDEX of the max even/odd element -> [1, 4, 8, 2, 3] -> max odd -> print 4

def max_even_odd(type_number, array_list):
    if type_number == "even":
        even_list = []
        for num in array_list:
            if num % 2 == 0:
                even_list.append(num)
        if len(even_list) > 0:
            max_num = max(even_list)
            for i in range(len(array_list) - 1, -1, -1):
                if array_list[i] == max_num:
                    max_index = i
                    return max_index
        else:
            print("No matches")
    elif type_number == "odd":
        odd_list = []
        for num in array_list:
            if not num % 2 == 0:
                odd_list.append(num)
        if len(odd_list) > 0:
            max_num = max(odd_list)
            for i in range(len(array_list) - 1, -1, -1):
                if array_list[i] == max_num:
                    max_index = i
                    return max_index
        else:
            return "No matches"


# a_list = [5, 5, 5, 5, 5]
# print(max_even_odd("even", a_list))

# min even/odd – returns the INDEX of the min even/odd element -> [1, 4, 8, 2, 3] -> min even > print 3

def min_even_odd(type_number, array_list):
    if type_number == "even":
        even_list = []
        for num in array_list:
            if num % 2 == 0:
                even_list.append(num)
        if len(even_list) > 0:
            min_num = min(even_list)
            for i in range(len(array_list) - 1, -1, -1):
                if array_list[i] == min_num:
                    min_index = i
                    return min_index
        else:
            return "No matches"
    elif type_number == "odd":
        odd_list = []
        for num in array_list:
            if not num % 2 == 0:
                odd_list.append(num)
        if len(odd_list) > 0:
            min_num = min(odd_list)
            for i in range(len(array_list) - 1, -1, -1):
                if array_list[i] == min_num:
                    min_index = i
                    return min_index
        else:
            return "No matches"


# first {count} even/odd– returns the first {count} elements -> [1, 8, 2, 3] -> first 2 even -> print [8, 2]

def first_several_even_odd(count_num, type_number, array_list):
    if count_num > len(array_list) or count_num <= 0:
        return "Invalid count"
    elif type_number == "even":
        even_list = []
        for i in range(len(array_list)):
            if array_list[i] % 2 == 0:
                if len(even_list) == count_num:
                    break
                else:
                    even_list.append(array_list[i])
        return even_list

    elif type_number == "odd":
        odd_list = []
        for i in range(len(array_list)):
            if not array_list[i] % 2 == 0:
                if len(odd_list) == count_num:
                    break
                else:
                    odd_list.append(array_list[i])
        return odd_list


def last_several_even_odd(count_num, type_number, array_list):
    if count_num > len(array_list) or count_num <= 0:
        return "Invalid count"
    elif type_number == "even":
        even_list = []
        for i in range(len(array_list) - 1, -1, -1):
            if array_list[i] % 2 == 0:
                if len(even_list) == count_num:
                    break
                else:
                    even_list.append(array_list[i])
        return even_list

    elif type_number == "odd":
        odd_list = []
        for i in range(len(array_list) - 1, -1, -1):
            if not array_list[i] % 2 == 0:
                if len(odd_list) == count_num:
                    break
                else:
                    odd_list.append(array_list[i])
        return odd_list


list_nums = [int(elem) for elem in input().split()]


while True:
    command = input()
    info = command.split()
    if info[0] == "end":
        print(list_nums)
        break

    elif info[0] == "exchange":
        list_nums = exchange(int(info[1]), list_nums)

    elif info[0] == "max":
        print(max_even_odd(info[1], list_nums))

    elif info[0] == "min":
        print(min_even_odd(info[1], list_nums))

    elif info[0] == "first":
        print(first_several_even_odd(int(info[1]), info[2], list_nums))

    elif info[0] == "last":
        print(last_several_even_odd(int(info[1]), info[2], list_nums))









