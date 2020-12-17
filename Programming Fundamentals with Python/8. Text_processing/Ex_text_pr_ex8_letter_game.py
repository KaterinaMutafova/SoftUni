# Number-letter game with string input

alphabet_dict = {chr(96 + digit): digit for digit in range(1, 27)}

line_strings = input().split()
result_sum = 0

for el in line_strings:
    first_letter = el[0]
    last_letter = el[-1]
    main_num = float(el[1:-1])
    if first_letter.isupper():
        sum_1 = main_num / float(alphabet_dict[first_letter.lower()])

    elif first_letter.islower():
        sum_1 = main_num * float(alphabet_dict[first_letter.lower()])

    if last_letter.isupper():
        sum_2 = sum_1 - float(alphabet_dict[last_letter.lower()])

    elif last_letter.islower():
        sum_2 = sum_1 + float(alphabet_dict[last_letter.lower()])

    result_sum += sum_2

print(f"{result_sum:.2f}")




