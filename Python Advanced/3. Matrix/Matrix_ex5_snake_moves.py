count_rows, count_columns = [int(el) for  el in input().split()]

word = input()

matrix = []

for row in range(count_rows):
    line = [0] * count_columns
    matrix.append(line)

index_word = 0
for r_index in range(count_rows):
    for c_index in range(count_columns):
        matrix[r_index][c_index] = word[index_word]
        index_word += 1
        if index_word >= len(word):
            index_word = 0

for r_index in range(count_rows):
    if r_index % 2 == 0:
        print(''.join(matrix[r_index]))
    else:
        reversed_row = matrix[r_index][::-1]
        print(''.join(reversed_row))




