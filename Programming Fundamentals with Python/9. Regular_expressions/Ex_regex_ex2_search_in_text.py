import re

pattern = r"(^_{1}|(?<=\s_){1})[A-Za-z0-9]+($|(?=[\s\.]))"

data = input()

match = re.finditer(pattern, data)
match = [m.group() for m in match]

print(','.join(match))