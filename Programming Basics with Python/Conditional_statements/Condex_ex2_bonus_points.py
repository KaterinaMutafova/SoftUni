points = int(input())

bonus = 0

if points <= 100:
    bonus = 5
elif points > 1000:
    bonus = points * 0.10
elif points > 100:
    bonus = points * 0.20

if points % 2 ==0:
    bonus += 1    #the same as bonus = bonus +1
elif points % 5 == 0:
    bonus += 2    #the same as bonus = bonus +5

print(bonus)
print(points+bonus)
