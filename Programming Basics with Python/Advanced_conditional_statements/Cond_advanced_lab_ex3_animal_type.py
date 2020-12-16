animal = input()

type_of_animal = "Any_animal"

if animal == "dog":
    type_of_animal = "mammal"
elif animal == "crocodile":
    type_of_animal = "reptile"
elif animal == "tortoise":
    type_of_animal = "reptile"
elif animal == "snake":
    type_of_animal = "reptile"
else:
    type_of_animal = "unknown"

print(type_of_animal)
