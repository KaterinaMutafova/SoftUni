#Порода на котката – текст – една от възможностите: "British Shorthair", "Siamese",
# "Persian", "Ragdoll", "American Shorthair" или "Siberian"
#Пол на котката – символ – 'm' или 'f'

cat_breed = input()
cat_sex = input()
human_year = 0
invalid_breed = False




if cat_breed == "British Shorthair":
    if cat_sex == "m":
        human_year = 13
    elif cat_sex == "f":
        human_year = 14
elif cat_breed == "Siamese":
    if cat_sex == "m":
        human_year =15
    elif cat_sex == "f":
        human_year = 16
elif cat_breed == "Persian":
    if cat_sex == "m":
        human_year = 14
    elif cat_sex == "f":
        human_year = 15
elif cat_breed == "Ragdoll":
    if cat_sex == "m":
        human_year = 16
    elif cat_sex == "f":
        human_year = 17
elif cat_breed == "American Shorthair":
    if cat_sex == "m":
        human_year = 12
    elif cat_sex == "f":
        human_year = 13
elif cat_breed == "Siberian":
    if cat_sex == "m":
        human_year = 11
    elif cat_sex == "f":
        human_year = 12
else:
    invalid_breed = True

cat_months = (human_year * 12) / 6

if invalid_breed:
    print(f"{cat_breed} is invalid cat!")
else:
    print(f"{round(cat_months)} cat months")