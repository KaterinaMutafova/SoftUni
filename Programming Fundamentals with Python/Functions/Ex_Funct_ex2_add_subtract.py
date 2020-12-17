num_1 = int(input())
num_2 = int(input())
num_3 = int(input())


def sum_numbers(a, b):
    result_sum = a + b
    return result_sum

k = 1 # for break points
print(sum_numbers(num_1, num_2))


def subtract(result_sum, c):
    final_result = result_sum - c
    return final_result

m = 2 # for break points

print(subtract(sum_numbers(num_1, num_2), num_3))


def add_and_subtract(a, b, c):
    end_result = subtract(sum_numbers(a,b), c)
    return end_result

n = 3  # for break points

print(add_and_subtract(num_1, num_2, num_3))

