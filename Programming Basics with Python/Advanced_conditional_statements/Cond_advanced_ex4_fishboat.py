#Бюджет на групата – цяло число;
#Сезон – текст: Spring, Summer, Autumn; или Winter;
#Брой рибари – цяло число.

budget = int(input())
season = input()
fishermen_count = int(input())

rent = 0

if season == "Spring":
    rent = 3000
    if fishermen_count <= 6:
        rent = 0.9 * rent
    elif 7 <= fishermen_count <= 11:
        rent = 0.85 * rent
    elif fishermen_count >= 12:
        rent = 0.75 * rent
    if fishermen_count % 2 == 0:
        rent = 0.95 * rent

elif season == "Summer":
    rent = 4200
    if fishermen_count <= 6:
        rent = 0.9 * rent
    elif 7 <= fishermen_count <= 11:
        rent = 0.85 * rent
    elif fishermen_count >= 12:
        rent = 0.75 * rent
    if fishermen_count % 2 == 0:
        rent = 0.95 * rent

elif season == "Autumn":
    rent = 4200
    if fishermen_count <= 6:
        rent = 0.9 * rent
    elif 7 <= fishermen_count <= 11:
        rent = 0.85 * rent
    elif fishermen_count >= 12:
        rent = 0.75 * rent

if season == "Winter":
    rent = 2600
    if fishermen_count <= 6:
        rent = 0.9 * rent
    elif 7 <= fishermen_count <= 11:
        rent = 0.85 * rent
    elif fishermen_count >= 12:
        rent = 0.75 * rent
    if fishermen_count % 2 == 0:
        rent = 0.95 * rent

diff = abs(budget - rent)

if budget >= rent:
    print(f"Yes! You have {diff:.2f} leva left.")
elif rent >= budget:
    print(f"Not enough money! You need {diff:.2f} leva.")




