#На първия ред - размерът на ръкава - реално число в интервала [1…1000]
#• На втория ред - размерът на предната част - реално число в интервала [1…1000]
#• На третия ред - платът, от който искаме да е ризата - "Linen", "Cotton", "Denim", "Twill" или "Flannel"
#• На четвъртия ред - дали ще желае вратовръзка – текст с възможности: "Yes", "No"

sleeve_length_cm = float(input())
front_length_cm = float(input())
type_fabric = input()
tie = input()

price_meter = 0

shirt_length = 2 * (sleeve_length_cm + front_length_cm) / 100
shirt_length += 0.10 * shirt_length

if type_fabric == "Linen":
    price_meter = 15
elif type_fabric == "Cotton":
    price_meter = 12
elif type_fabric == "Denim":
    price_meter = 20
elif type_fabric == "Twill":
    price_meter = 16
elif type_fabric == "Flannel":
    price_meter = 11

price_shirt = price_meter * shirt_length + 10

if tie == "Yes":
    price_shirt += 0.20 * price_shirt

print(f"The price of the shirt is: {price_shirt:.2f}lv.")
