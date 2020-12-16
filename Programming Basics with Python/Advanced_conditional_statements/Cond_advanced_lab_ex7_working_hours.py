hour = int(input())
day = input()

sign = "none"

if day == "Monday":
    if 10 <= hour <= 18:
        sign = "open"
    else:
        sign = "closed"

elif day == "Tuesday":
    if 10 <= hour <= 18:
        sign = "open"
    else:
        sign = "closed"

elif day == "Wednesday":
    if 10 <= hour <= 18:
        sign = "open"
    else:
        sign = "closed"

elif day == "Thursday":
    if 10 <= hour <= 18:
        sign = "open"
    else:
        sign = "closed"

elif day == "Friday":
    if 10 <= hour <= 18:
        sign = "open"
    else:
        sign = "closed"

elif day == "Saturday":
    if 10 <= hour <= 18:
        sign = "open"
    else:
        sign = "closed"

elif day == "Sunday":
    sign = "closed"

print(sign)
