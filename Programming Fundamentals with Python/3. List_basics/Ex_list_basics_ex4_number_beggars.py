turns = input()
beg_num = int(input())

beggars = []
list_turns = turns.split(", ")

for i in range(beg_num):
    beggars.append(0)

index = 0
for num in list_turns:
    if index == beg_num:
        index = 0
    beggars[index] += int(num)
    index += 1

print(beggars)
print(list_turns)





#print(list_turns)

# sum_turns.insert(0, list_turns[0])
# sum_turns.insert(1, list_turns[1])
#
# sum_turns.insert(0, list_turns[2])
# sum_turns.insert(1, list_turns[3])