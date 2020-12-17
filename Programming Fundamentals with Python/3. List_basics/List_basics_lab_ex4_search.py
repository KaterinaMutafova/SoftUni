n_times = int(input())
word = input()

my_list = []
my_list_with_maches = []

for i in range(n_times):
    text = input()
    my_list.append(text)
    if word in text:
        my_list_with_maches.append(text)

print(my_list)
print(my_list_with_maches)

