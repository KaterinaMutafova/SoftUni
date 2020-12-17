# Shouting in games with repeatable words:

line = input()
index = 0
current_result = ''
result = ''

while index < len(line):
    if not line[index].isdigit():
        current_result += line[index]
        index += 1
    else:
        number = ''
        while index < len(line) and line[index].isdigit():
            number += line[index]
            index += 1
        number = int(number)
        current_result = current_result.upper() * number
        result += current_result
        current_result = ''


print(f"Unique symbols used: {len(set(result))}")
print(result)



