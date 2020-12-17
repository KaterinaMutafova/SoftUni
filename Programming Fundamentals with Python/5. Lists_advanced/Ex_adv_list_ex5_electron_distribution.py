count_electrons = int(input())

n = 1
shells = []

while 2 * pow(n, 2) < count_electrons:
    count_electrons -= 2 * pow(n, 2)
    shells.append(2 * pow(n, 2))
    n += 1

shells.append(count_electrons)

print(shells)
