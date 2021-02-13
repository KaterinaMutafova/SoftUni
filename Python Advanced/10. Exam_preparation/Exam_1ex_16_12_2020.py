from collections import deque


males = list(map(int, input().split(" ")))
females = deque(list(map(int, input().split(" "))))

counter_matches = 0


while True:
    if len(males) <= 0 or len(females) <= 0:
        break
    else:
        current_male = males[-1]
        current_female = females[0]
        if current_male <= 0:
            males.pop()
            continue
        if current_female <= 0:
            females.popleft()
            continue

        if current_male % 25 == 0 and len(males) > 0:
            males.pop()
            if len(males) > 0:
                males.pop()
                continue

        if current_female % 25 == 0 and len(females) > 0:
            females.popleft()
            if len(females) > 0:
                females.popleft()
                continue


        if current_male == current_female:
            counter_matches += 1
            males.pop()
            females.popleft()
        elif current_male != current_female:
            females.popleft()
            males[-1] -= 2


print(f"Matches: {counter_matches}")
if len(males) <= 0:
    print("Males left: none")
else:
    males = [str(el) for el in list(males)[::-1]]
    print(f"Males left: {', '.join(males)} ")
if len(females) <= 0:
    print("Females left: none")
else:
    females = [str(i) for i in females]
    print(f"Females left: {', '.join(females)}")


