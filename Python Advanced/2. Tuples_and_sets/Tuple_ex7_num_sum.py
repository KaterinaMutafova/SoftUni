count = int(input())

even_numbers_set = set()
odd_numbers_set = set()

for i in range(1, count+1):
    name = input()
    current_sum =sum([ord(el) for el in name]) // i
    if current_sum % 2 == 0:
        even_numbers_set.add(current_sum)
    else:
        odd_numbers_set.add(current_sum)

sum_evens = sum(even_numbers_set)
sum_odds = sum(odd_numbers_set)

if sum_evens == sum_odds:
    modified_set = [str(el) for el in even_numbers_set.union(odd_numbers_set)]
    print(', '.join(modified_set))
elif sum_odds > sum_evens:
    modified_set = [str(el) for el in odd_numbers_set.difference(even_numbers_set)]
    print(', '.join(modified_set))
else:
    modified_set = [str(el) for el in even_numbers_set.symmetric_difference(odd_numbers_set)]
    print(', '.join(modified_set))


