n = int(input())
l = int(input())


for symbol_1 in range(1, n + 1):
    for symbol_2 in range(1, n + 1):
        for symbol_3 in range(97, 97 + l):
            for symbol_4 in range(97, 97 + l):
                for symbol_5 in range(1, n + 1):
                    if symbol_5 > symbol_1 and symbol_5 > symbol_2:
                        print(f"{symbol_1}{symbol_2}{chr(symbol_3)}{chr(symbol_4)}{symbol_5}", end = " ")

