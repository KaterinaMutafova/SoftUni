num = int(input())
day = "Everyday"
is_invalid = False

if num == 1:
    day = "Monday"
elif num == 2:
    day = "Tuesday"
elif num == 3:
    day = "Wednesday"
elif num == 4:
    day = "Thursday"
elif num == 5:
    day = "Friday"
elif num == 6:
    day = "Saturday"
elif num ==7:
    day = "Sunday"
else:
    is_invalid = True

if is_invalid:
    print("Error")
else:
    print(day)


