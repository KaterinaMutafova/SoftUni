product = input()

# fruit :  banana, apple, kiwi, cherry, lemon и grapes;
# vegetable : tomato, cucumber, pepper и carrot;
if product == "banana":
    type_prod = "fruit"
elif product == "apple":
    type_prod = "fruit"
elif product == "kiwi":
    type_prod = "fruit"
elif product == "cherry":
    type_prod = "fruit"
elif product == "lemon":
    type_prod = "fruit"
elif product == "grapes":
    type_prod = "fruit"

elif product == "tomato":
    type_prod = "vegetable"
elif product == "cucumber":
    type_prod = "vegetable"
elif product == "pepper":
    type_prod = "vegetable"
elif product == "carrot":
    type_prod = "vegetable"
else:
    type_prod = "unknown"

print(type_prod)

