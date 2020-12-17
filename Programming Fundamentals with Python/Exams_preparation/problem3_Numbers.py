numbers = list(map(int, input().split()))

average_sum = sum(numbers) / len(numbers)

top_numbers_above_average = []
counter = 0

numbers.sort(reverse = True)

for num in numbers:
    if counter == 5:
        break
    if num > average_sum:
        top_numbers_above_average.append(num)
        counter += 1

if len(top_numbers_above_average) == 0:
    print("No")
else:
    print(' '.join(str(el) for el in top_numbers_above_average))






