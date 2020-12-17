# import re
#
# data = input()
#
# pattern = r"\d{2}([\./-])[A-Z][a-z]{2}\1\d{4}"
#
# dates = re.finditer(pattern, data)
# for d in dates:
#     m_obj = d.group(0)
#     day = m_obj[0:2]
#     month = m_obj[3:6]
#     year = m_obj[7:11]
#     print(f"Day: {day}, Month: {month}, Year: {year}")

# НОВ ВАРИАНТ!!!


import re

data  = input()

pattern = r"(?P<day>\d{2})(?P<separator>[\./-])(?P<month>[A-Z][a-z]{2})(?P=separator)(?P<year>\d{4})"
dates = re.finditer(pattern, data)

for date in dates:
    dict = date.groupdict()
    print(f"Day: {dict['day']}, Month: {dict['month']}, Year: {dict['year']}")


# Упражнение   --- Да се опрости регекса с извикване  отново  на  повтарящия се код от регекса но
# не и същата  стойнст



