#Първи ред – начало на интервала – цяло число в интервала [1...999]
#Втори ред – край на интервала – цяло число в интервала [по-голямо от първото число...1000]
#Трети ред – магическото число – цяло число в интервала [1...10000]

start = int(input())
end = int(input())
magic_number = int(input())
counter = 0
i = 0
j = 0
is_found = False

for i in range(start, end + 1):
    for j in range(start, end + 1):
        counter += 1
        if i + j == magic_number:
            is_found = True
            print(f"Combination N:{counter} ({i} + {j} = {magic_number})")
            break
    if is_found:
        break

if not is_found:
    print(f"{counter} combinations - neither equals {magic_number}")

