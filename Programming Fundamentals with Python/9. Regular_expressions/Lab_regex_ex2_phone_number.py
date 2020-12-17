import re
data = input()

reg_pattern = r"(\+359\s2\s\d{3}\s\d{4}\b)|(\+359-2-\d{3}-\d{4}\b)"

phones = re.finditer(reg_pattern, data)
phones = [p.group(0) for p in phones]
print(', '.join(phones))

