from math import pi
from math import pow
r = float(input())

calculated_area = pi * pow(r,2)
calculated_parameter = 2 * pi * r

print(f"{calculated_area:.2f}")
print(f"{calculated_parameter:.2f}")
