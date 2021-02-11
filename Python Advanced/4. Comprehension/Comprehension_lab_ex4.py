def flatten_matrix(matrix):
    new_list = []
    for mini_list in matrix:
        for i in mini_list:
            new_list.append(i)
    return new_list



def get_matrix():
    count_rows = int(input())
    matrix = []
    for i in range(count_rows):
        line = list(map(int, input().split(", ")))
        matrix.append(line)

    return matrix


matrix = get_matrix()
print(flatten_matrix(matrix))


