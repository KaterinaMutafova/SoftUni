# Filter digits, letters and other symbols from a  text
digits = []
letters = []
others = []


line = input()
a = 6
for char in line:
    if char.isdigit():
        digits.append(char)
    elif char.isalpha():
        letters.append(char)
    else:
        others.append(char)

print(''.join(digits))
print(''.join(letters))
print(''.join(others))

