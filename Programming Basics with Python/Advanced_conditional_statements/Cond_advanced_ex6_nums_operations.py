#N1 – цяло число;
#N2 – цяло число;
#Оператор – един символ измежду: +, -, *, /, %

N1 = int(input())
N2 = int(input())
operat = input()

result = 0
even_odd = "both"

if operat == "+":
    result = N1 + N2
    if result % 2 == 0:
        even_odd = "even"
    else:
        even_odd = "odd"
elif operat == "-":
    result = N1 - N2
    if result % 2 == 0:
        even_odd = "even"
    else:
        even_odd = "odd"
elif operat == "*":
    result = N1 * N2
    if result % 2 == 0:
        even_odd = "even"
    else:
        even_odd = "odd"
elif operat == "/":
    if N2 == 0:
        print(f"Cannot divide {N1} by zero")
    else:
        result = N1 / N2
elif operat == "%":
    if N2 == 0:
        print(f"Cannot divide {N1} by zero")
    else:
        result = N1 % N2

if operat == "+" or operat == "-" or operat == "*":
    print(f"{N1} {operat} {N2} = {result} - {even_odd}")

elif operat == "/":
    if N2 != 0:
        print(f"{N1} / {N2} = {result:.2f}")

elif operat == "%":
    if N2 != 0:
        print(f"{N1} % {N2} = {result}")


