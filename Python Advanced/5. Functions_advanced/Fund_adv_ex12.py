def palindrome(word, index):
    if index == len(word) // 2:
        return f"{word} is a palindrome"

    if word[index] == word[::-1][index]:
        return palindrome(word,index + 1)
    else:
        return f"{word} is not a palindrome"




print(palindrome("abcba", 0))
# print(palindrome("peter", 0))

# word = "abcd"
# reverced_word = word[::-1]
# print(reverced_word)
#
# first_char = word[0]
# first_rev_char = reverced_word[0]
# print(first_char)
# print(first_rev_char)