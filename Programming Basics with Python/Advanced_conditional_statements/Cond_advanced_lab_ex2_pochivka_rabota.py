day = input()
work_or_hols = "working weekend"

is_invalid = False

if day == "Monday" or day == "monday":
    work_or_hols = "Working day"
elif day == "Tuesday" or day == "tuesday":
    work_or_hols = "Working day"
elif day == "Wednesday" or day == "wednesday":
    work_or_hols = "Working day"
elif day == "Thursday" or day == "thursday":
    work_or_hols = "Working day"
elif day == "Friday" or day == "friday":
    work_or_hols = "Working day"
elif day == "Saturday" or day == "saturday":
    work_or_hols = "Weekend"
elif day == "Sunday" or day == "sunday":
    work_or_hols = "Weekend"
else:
    is_invalid = True

if is_invalid:
    print("Error")
else:
    print(work_or_hols)
