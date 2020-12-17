import re

line = input()
names = []
total_price = 0

pattern = r"(^>>)(?P<name>\w+)<<(?P<price>\d+(\.\d+)?)\!(?P<quantity>\d+)($|(?=\s))"

while not line == "Purchase":
    match = re.match(pattern, line)
    if match:
        obj = match.groupdict()
        names.append(obj['name'])
        total_price += float(obj['price']) * int(obj['quantity'])

    line = input()

print("Bought furniture:")
for name in names:
    print(name)
print(f"Total money spend: {total_price:.2f}")





