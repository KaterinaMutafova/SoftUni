first_num = int(input())
second_num = int(input())
third_num = int(input())

def smallest_of_three(a,b,c):
    result = min(a,b,c)
    return result


print(smallest_of_three(first_num, second_num, third_num))
