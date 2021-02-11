# string_info = [word + " " + "->"+ " " + str(len(word)) for word in (input().split(", "))]
# print(', '.join(string_info))


string_info = [f"{word} -> {len(word)}" for word in (input().split(", "))]
print(', '.join(string_info))
