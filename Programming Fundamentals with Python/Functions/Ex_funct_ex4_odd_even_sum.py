number_from_input = int(input())


def odd_even_sum_numbers(single_number):
    list_numbers = []
    for i in str(number_from_input):
        list_numbers.append(int(i))

    even_list = []
    odd_list = []

    for num in list_numbers:
        if num % 2 == 0:
            even_list.append(num)
        else:
            odd_list.append(num)

    odd_sum = sum(odd_list)
    even_sum = sum(even_list)

    print(f"Odd sum = {odd_sum}, Even sum = {even_sum}")


odd_even_sum_numbers(number_from_input)






