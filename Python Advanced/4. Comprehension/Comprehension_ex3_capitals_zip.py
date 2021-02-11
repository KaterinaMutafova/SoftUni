countries = input().split(", ")
capitals = input().split(", ")

result = list(zip(countries, capitals))
result = [f"{key} -> {value}"for key, value in result]

for el in result:
     print(el)