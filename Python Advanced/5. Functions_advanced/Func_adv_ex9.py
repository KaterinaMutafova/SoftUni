def func_executor(*args):
    list_results = []
    for tuple_bundle in args:
        current_result = tuple_bundle[0](*tuple_bundle[1])
        list_results.append(current_result)

    return list_results


def sum_numbers(num1, num2):
    return num1 + num2

def multiply_numbers(num1, num2):
    return num1 * num2


print(func_executor((sum_numbers, (1, 2)), (multiply_numbers, (2, 4))))






