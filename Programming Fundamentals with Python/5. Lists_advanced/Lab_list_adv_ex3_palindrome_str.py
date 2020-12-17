string_of_words = input()
searched_word = input()

list_of_words = string_of_words.split()
palindromes = []
count_word = []

is_palindrome = [palindromes.append(word) for word in list_of_words if word == word[::-1]]

count_searched_word = [count_word.append(el) for el in palindromes if el == searched_word]


print(palindromes)
print(f"Found palindrome {len(count_word)} times")