# Travel vacation - show the  destinations

import re

travel_stops = input()

pattern = r"(?P<separator>[=/])(?P<destination>[A-Z][A-Za-z]{2,})(?P=separator)"
destinations_list = []
travel_points = 0

destinations = [el.group() for el in re.finditer(pattern, travel_stops)]

destinations_string = ' '.join(destinations)
for i in destinations:
    match = re.match(pattern, i)
    obj = match.groupdict()
    destinations_list.append(obj['destination'])
    travel_points += len(obj['destination'])

print(f"Destinations: {', '.join(destinations_list)}")
print(f"Travel Points: {travel_points}")


# Кратък вариант - само 7 РЕДА!!!

# import re
#
# pattern = r"(=|/)([A-Z][A-Za-z]{2,})\1"
# location = [match.group(2) for match in re.finditer(pattern, input())]
# print(f"Destinations: {', '.join(location)}")
# print(f"Travel Points: {len(list(''.join(location)))}")


