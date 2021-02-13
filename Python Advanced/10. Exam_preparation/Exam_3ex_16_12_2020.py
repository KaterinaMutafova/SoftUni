def get_magic_triangle (count):
    matrix = []
    for r in range(count):
        line_length = r + 1
        line = [1] * line_length
        matrix.append(line)

    for row in range(count):
        for col in range(0, len(matrix[row]) -1):
            if row >= 1 and row < len(matrix) - 1:
                matrix[row + 1][col + 1] = matrix[row][col] + matrix[row][col + 1]


    return matrix


print(magic_triangle(7))