# Astronaut - calculate how much food  you have and for how  many days.

# (#|\|)(?P<item>[a-zA-Z\s]+)\1(?P<date>\d{2}/\d{2}/\d{2})\1(?P<calories>([0-9][0-9]{0,3}|10000))\1

import re

info = input()

pattern = r"(#|\|)(?P<product>[A-Za-z\s]+)\1(?P<date>\d{2}/\d{2}/\d{2})\1(?P<calories>1?([0-9][0-9]{0,3}|10000))\1"

data = re.finditer(pattern, info)

count = re.findall(pattern, info)
total_calories = 0
list_items = []

for el in data:
    product_data = el.groupdict()
    total_calories += int(product_data['calories'])
    list_items.append(el)

days_to_last = total_calories//2000
print(f"You have food to last you for: {days_to_last} days!")

for item in list_items:

    print(f"Item: {item['product']}, Best before: {item['date']}, Nutrition: {item['calories']}")

