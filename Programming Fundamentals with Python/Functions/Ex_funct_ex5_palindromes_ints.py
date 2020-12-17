string_of_numbers = input().split(", ")


def palindrome_function(number):
    is_palindrome = False
    list_numbers = []

    for num in str(number):
        list_numbers.append(int(num))

    length_number = len(list_numbers)
    if length_number == 1:
        is_palindrome = True
        return "True"
    else:
        for k in range(0, len(list_numbers) - 1):
            for j in range(len(list_numbers) -1, 0, -1):
                if list_numbers[k] == list_numbers[j]:
                    is_palindrome = True
                    return "True"
                else:
                    palindrome = False
                    return "False"


for p_num in string_of_numbers:
    print(palindrome_function(p_num))





