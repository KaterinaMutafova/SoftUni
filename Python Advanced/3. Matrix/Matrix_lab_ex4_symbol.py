count_rows = int(input())
matrix = []

for i in range(count_rows):
    line = list(input())
    matrix.append(line)

symbol = input()

for big_i in range(count_rows):
    for small_i in range(count_rows):
        current_position = matrix[big_i][small_i]
        if symbol == current_position:
            print(tuple([big_i, small_i]))
            exit(0)

print(f"{symbol} does not occur in the matrix")



