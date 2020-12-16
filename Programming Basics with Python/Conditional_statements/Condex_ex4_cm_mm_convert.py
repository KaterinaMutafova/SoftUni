number = float(input())

text_input = input()
text_output = input()

if text_input == "cm":
    number /= 100
elif text_input == "mm":
    number /= 1000

if text_output == "cm":
    number *=100
elif text_output == "mm":
    number *=1000

print(f"{number:.3f}")

