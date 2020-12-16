# - При 100 лв. или по-малко – някъде в България:
# Лято – 30% от бюджета;
# Зима – 70% от бюджета.
# = При 1000 лв. или по малко – някъде на Балканите:
# Лято – 40% от бюджета;
# Зима – 80% от бюджета.
# = При повече от 1000 лв. – някъде из Европа:
# При пътуване из Европа, независимо от сезона, ще похарчи 90% от бюджета.

budget = float(input())
season = input()

destination = "somewhere"
accommod = "anywhere"

price = 0
if budget <= 100:
    destination = "Bulgaria"
    if season == "summer":
        accommod = "Camp"
        price = 0.3 * budget
    elif season == "winter":
        accommod = "Hotel"
        price = 0.7 * budget

elif 100 < budget <= 1000:
    destination = "Balkans"
    if season == "summer":
        accommod = "Camp"
        price = 0.4 * budget
    elif season == "winter":
        accommod = "Hotel"
        price = 0.8 * budget

elif budget > 1000:
    destination = "Europe"
    accommod = "Hotel"
    price = 0.9 * budget

print(f"Somewhere in {destination}")
print(f"{accommod} - {price:.2f}")




