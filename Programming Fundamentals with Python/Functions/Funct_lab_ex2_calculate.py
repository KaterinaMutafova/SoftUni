operation = input()
num_1 = int(input())
num_2 = int(input())


# &#39;multiply&#39;, &#39;divide&#39;, &#39;add&#39;, &#39;subtract&#39;

def math_action(a, b, operate):
    if operate == "multiply":
        result = a * b
        return round(result)
    elif operate == "add":
        result = a + b
        return round(result)
    elif operate == "divide":
        result = a / b
        return round(result)
    elif operate == "subtract":
        result = a - b
        return round(result)


print(math_action(num_1, num_2, operation))


