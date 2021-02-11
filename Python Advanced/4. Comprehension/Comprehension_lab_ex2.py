string_text = input()

vowels = ["a", "o", "u", "e", "i", "A", "O", "U", "E", "I"]

new_string_text = []

for char in string_text:
    if char not in vowels:
        new_string_text.append(char)

print(''.join(new_string_text))