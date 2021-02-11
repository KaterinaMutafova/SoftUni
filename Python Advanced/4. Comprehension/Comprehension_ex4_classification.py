num_string = list(map(int, input().split(", ")))

positive_num = [str(num) for num in num_string if num >= 0]
negative_num = [str(num) for num in num_string if num < 0]
even_num = [str(num) for num in num_string if num % 2 == 0]
odd_num = [str(num) for num in num_string if not num %2 == 0]

print(f"Positive: {', '.join(positive_num)}")
print(f"Negative: {', '.join(negative_num)}")
print(f"Even: {', '.join(even_num)}")
print(f"Odd: {', '.join(odd_num)}")








