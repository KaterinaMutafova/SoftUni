import re

cool_threshold_sum = 1

line = input()

pattern_digits = r"\d"

digits = re.finditer(pattern_digits, line)

for dig in digits:
    # cool_threshold_sum *= int(dig.group())
    result = dig.group()
    cool_threshold_sum *= int(result)

print(cool_threshold_sum)

