#x – височината на къщата – реално число в интервала [2...100]
#y – дължината на страничната стена – реално число в интервала [2...100]
#h – височината на триъгълната стена на прокрива – реално число в интервала [2...100]

x_side = float(input())
y_side = float(input())
h_roof = float(input())

#logic
S_wind_door = 2 * 1.5 * 1.5 + 1.2 * 2
S_walls_house = (2 * (x_side + y_side) * x_side) - S_wind_door
S_roof_house = 2 * (x_side * y_side) + 2 * (x_side * h_roof) / 2

#Разхода на зелената боя е 1 литър за 3.4 м2, а на червената – 1 литър за 4.3 м2.

l_walls_green = S_walls_house / 3.4
l_roof_red = S_roof_house / 4.3

print(f"{l_walls_green:.2f}")
print(f"{l_roof_red:.2f}")


