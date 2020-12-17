count_words = int(input())

dict_synonyms = {}

for time in range(count_words):
    word = input()
    synonym = input()
    if word not in dict_synonyms:
        dict_synonyms[word] = []
    dict_synonyms[word].append(synonym)


for word in dict_synonyms:
    print(f"{word} - {', '.join(dict_synonyms[word])}")
