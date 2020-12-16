start_num = int(input())
end_num = int(input())


for i in range(start_num, end_num + 1):
    num_as_str = str(i)
    odd_sum = 0
    even_sum = 0
    for index, digit in enumerate(num_as_str):
        if index % 2 == 0:
            even_sum += int(digit)
        else:
            odd_sum += int(digit)

    if even_sum == odd_sum:
        print(f"{num_as_str}", end = " ")



