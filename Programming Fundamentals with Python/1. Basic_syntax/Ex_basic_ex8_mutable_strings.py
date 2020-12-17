word_1 = input()
word_2 = input()
current_result = ""
previous_result = word_1

for iteration in range(0, len(word_2)):
    for index_2 in range(0, iteration + 1):
        current_result += word_2[index_2]
    for index_1 in range(iteration + 1, len(word_1)):
        current_result += word_1[index_1]
    if not previous_result == current_result:
        print(current_result)
    previous_result = current_result
    current_result = ""