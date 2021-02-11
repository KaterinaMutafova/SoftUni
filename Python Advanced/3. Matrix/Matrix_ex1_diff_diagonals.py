def get_matrix(is_test=True):
    if is_test:
        return [
            [11, 2, 4],
            [4, 5, 6],
            [10, 8, - 12],
        ]
    else:
        count = int(input())
        matrix = []
        for row in range(count):
            row = [int(el) for el in input().split(" ")]
            matrix.append(row)
    return matrix


def get_main_diagonal(matrix):
    sum = 0
    for i in range(len(matrix)):
        sum += matrix[i][i]
    return sum


def get_second_diagonal(matrix):
    sum_second = 0
    col = len(matrix) - 1
    length = len(matrix)
    for i in range(length):
        sum_second += matrix[i][col]
        col -= 1
    return sum_second


def get_difference(sum_first, sum_sec):
    diff = abs(sum_first - sum_sec)
    return diff


matrix = get_matrix(is_test=False)

sum_main_diagonal = get_main_diagonal(matrix)
sum_second_diagonal = get_second_diagonal(matrix)
diff = get_difference(sum_main_diagonal, sum_second_diagonal)

print(diff)



