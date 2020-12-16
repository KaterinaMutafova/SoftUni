#плод - banana / apple / orange / grapefruit / kiwi / pineapple / grapes;
#ден от седмицата - Monday / Tuesday / Wednesday / Thursday / Friday / Saturday /
#Sunday;
#количество (реално число).

fruit = input()
day = input()
quantity = float(input())

price = 1
is_invalid = False
# banana apple orange grapefruit kiwi pineapple grapes

if day == "Monday" or day == "Tuesday" or day == "Wednesday" or day == "Thursday" or day == "Friday":
    if fruit == "banana":
        price = 2.50
    elif fruit == "apple":
        price = 1.20
    elif fruit == "orange":
        price = 0.85
    elif fruit == "grapefruit":
        price = 1.45
    elif fruit == "kiwi":
        price = 2.70
    elif fruit == "pineapple":
        price = 5.50
    elif fruit == "grapes":
        price = 3.85
    else:
        is_invalid = True

elif day == "Saturday" or day == "Sunday":
    if fruit == "banana":
        price = 2.70
    elif fruit == "apple":
        price = 1.25
    elif fruit == "orange":
        price = 0.90
    elif fruit == "grapefruit":
        price = 1.60
    elif fruit == "kiwi":
        price = 3.00
    elif fruit == "pineapple":
        price = 5.60
    elif fruit == "grapes":
        price = 4.20
    else:
        is_invalid = True
else:
    is_invalid = True

total = price * quantity

if is_invalid:
    print("error")
else:
    print(f"{total:.2f}")



