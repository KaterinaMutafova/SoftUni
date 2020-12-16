length = input()
sum = 0

for i in range(0,len(length)):
    if length[i] == "a":
        sum += 1
    if length[i] == "e":
        sum += 2
    if length[i] == "i":
        sum += 3
    if length[i] == "o":
        sum += 4
    if length[i] == "u":
        sum += 5

print(sum)

