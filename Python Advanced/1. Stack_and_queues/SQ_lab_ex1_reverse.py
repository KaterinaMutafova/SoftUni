text = list(input())
reverse_text = []

for ch in range(len(text)):
    reverse_text.append(text.pop())

print(''.join(reverse_text))




