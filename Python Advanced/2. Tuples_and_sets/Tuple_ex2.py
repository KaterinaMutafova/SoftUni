def get_list(num1, num2):
    num1_list = []
    num2_list = []
    for iter in range(num1 + num2):
        number = int(input())
        if iter < num1:
            num1_list.append(number)
        else:
            num2_list.append(number)
    return (num1_list, num2_list)


def get_set(list_0):
    list_0 = set(list_0)

    return list_0

def get_result(final):
    for i in final:
        print(i)


lengths = input().split(" ")

n = int(lengths[0])
m = int(lengths[1])

(n_list, m_list) = get_list(n, m)


n_list = get_set(n_list)
m_list = get_set(m_list)

final_set = n_list.intersection(m_list)

get_result(final_set)



