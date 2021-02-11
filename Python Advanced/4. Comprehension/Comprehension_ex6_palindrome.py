matrix = []
count_row, count_column = list(map(int, input().split(" ")))

dict_alphabet = {}
for i in range(1, 27):
    dict_alphabet[i] = chr(96 + i)

for row in range(1, count_row + 1):
    line = [f"{dict_alphabet[row]}{dict_alphabet[row + el]}{dict_alphabet[row]}" for el in range(count_column)]
    print(' '.join(line))

    matrix.append(line)



