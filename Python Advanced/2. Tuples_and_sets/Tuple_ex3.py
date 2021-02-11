def get_list(count_num):
    elements = []
    for i in range(count):
        current_el = input().split(" ")
        elements.extend(current_el)

    return elements


def get_set(list_0):
    list_0 = set(list_0)

    return list_0


def get_result(final_list):
    for i in final_list:
        print(i)


count = int(input())

list_elements = get_list(count)

list_elements = get_set(list_elements)

get_result(list_elements)
