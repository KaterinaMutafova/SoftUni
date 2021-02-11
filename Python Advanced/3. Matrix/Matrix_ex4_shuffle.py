def get_matrix():
    rows, cols = [int(el) for el in input().split(" ")]
    m = []
    for i in range(rows):
        line = input().split(" ")
        m.append(line)
    return m


def print_matrix(matrix):
    for r in range(len(matrix)):
        m=[]
        for c in range(len(matrix[0])):
            m.append(matrix[r][c])
        print(' '.join(m))


matrix = get_matrix()
data = input()

while not data == "END":
    data = data.split(" ")
    command = data[0]
    coordinates = data[1:]

    if (not command == "swap") or len(coordinates) != 4:
        print("Invalid input!")
    else:
        row1, col1, row2, col2 = coordinates
        row1 = int(row1)
        col1 = int(col1)
        row2 = int(row2)
        col2 = int(col2)
        if row1 > len(matrix) or \
        row2 > len(matrix) or col1 > len(matrix[0]) or col2 > len(matrix[0]):
            print("Invalid input!")
        else:
            matrix[row1][col1],  matrix[row2][col2] = matrix[row2][col2], matrix[row1][col1]
            print_matrix(matrix)


    data = input()


