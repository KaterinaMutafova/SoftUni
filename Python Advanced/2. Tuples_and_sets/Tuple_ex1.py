def get_info(n):
    l_n = []
    for iteration in range(number):
        name = input()
        l_n.append(name)
    return l_n


def transform_list(l_n):
    l_n = set(l_n)
    return l_n


def print_name(l_n):
    for n in l_n:
        print(n)


number = int(input())

list_names = get_info(number)

list_names = transform_list(list_names)

print_name(list_names)
