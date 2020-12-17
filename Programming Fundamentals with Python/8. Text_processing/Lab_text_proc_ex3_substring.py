# Remove word from a given string

word_to_remove = input()
text = input()

while word_to_remove in text:
    text = text.replace(word_to_remove, "")

print(text)