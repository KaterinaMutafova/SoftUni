count = int(input())

matrix = [list(map(int, input().split(", ")))for _ in range(count)]

first_d_list = []
second_d_list = []
for i in range(count):
    current_num_f = matrix[i][i]
    current_num_s = matrix[i][count - i - 1]
    first_d_list.append(current_num_f)
    second_d_list.append(current_num_s)

print(f"First diagonal: {', '.join(str(el) for el in first_d_list)}. Sum: {sum(first_d_list)}")
print(f"Second diagonal: {', '.join(str(el2) for el2 in second_d_list)}. Sum: {sum(second_d_list)}")



