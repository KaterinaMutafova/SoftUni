def factorial_calc(number):
    result = 1
    for num in range(1, number +1):
        result *= num
    return result


first_num = int(input())
second_num = int(input())

first_res = factorial_calc(first_num)
second_res = factorial_calc(second_num)

total_result = first_res / second_res

print(f"{total_result:.2f}")

