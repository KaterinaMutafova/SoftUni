import math
figure = str(input())

#logic
area = 0

if figure == "square":
    side = float(input())
    area = side * side

if figure == "rectangle":
    side_a = float(input())
    side_b = float(input())
    area = side_a * side_b

if figure == "circle":
    r = float(input())
    area = math.pi * math.pow(r,2)

if figure == "triangle":
    side = float(input())
    h = float(input())
    area = (side * h)/2

print(f"{area:.3f}")

