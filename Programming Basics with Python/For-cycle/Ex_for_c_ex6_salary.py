#Брой отворени табове в браузъра n - цяло число в интервала [1...10]
#Заплата - число в интервала [700...1500]

tabs = int(input())
salary = float(input())
flag = False


for i in range(1, tabs + 1):
    website = input()
    if website == "Facebook":
        salary -= 150

    elif website == "Instagram":
        salary -= 100

    elif website == "Reddit":
        salary -= 50

    if salary <= 0:
        flag = True
        break

if flag:
    print(f"You have lost your salary.")
else:
    print(int(salary))




