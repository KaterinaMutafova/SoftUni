import re

data = input()

pattern = r"(^|(?<=\s))-?\d+(\.\d+)?($|(?=\s))"

numbers = re.finditer(pattern, data)
numbers = [d.group() for d in numbers]
print(*numbers)
