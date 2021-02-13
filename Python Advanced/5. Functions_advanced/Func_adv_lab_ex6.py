def comb(text, range_first_index = 0):
    if range_first_index == len(text):
        print(''.join(text))
        return

    for i in range(range_first_index, len(text)):
        text[range_first_index], text[i] = text[i], text[range_first_index]
        comb(text, range_first_index + 1)
        text[range_first_index], text[i] = text[i], text[range_first_index]

text = list(input())
comb(text)