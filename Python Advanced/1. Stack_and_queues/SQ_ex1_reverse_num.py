text = list(map(int, input().split()))
reverse_text = []

for num in range(len(text)):
    reverse_text.append(text.pop())

reverse_text = list(map(str, reverse_text))

print(' '.join(reverse_text))