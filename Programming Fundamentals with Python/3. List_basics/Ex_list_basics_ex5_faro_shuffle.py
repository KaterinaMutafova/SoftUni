cards = input().split(" ")
n_shuffles = int(input())

current_shuffle = cards
new_shuffle = []
counter = 0

for j in range(n_shuffles):
    for i in range(len(current_shuffle)//2):
        second_deck_start_diff = len(current_shuffle)//2
        new_shuffle.append(current_shuffle[i])
        new_shuffle.append(current_shuffle[i + second_deck_start_diff])
    current_shuffle = new_shuffle
    counter += 1
    if counter == n_shuffles:
        pass
    else:
        new_shuffle = []

print(new_shuffle)






