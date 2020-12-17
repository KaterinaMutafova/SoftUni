float_num = float(input())

if float_num == 0:
    print("zero")

elif float_num > 0:
    if 0 < float_num < 1:
        print("small positive")
    elif 1 < float_num < 1000000:
        print("positive")
    elif float_num > 1000000:
        print("large positive")

elif float_num < 0:
    if -1 < float_num < 0:
        print("small negative")
    elif -1000000 < float_num < -1:
        print("negative")
    elif float_num < -1000000:
        print("large negative")
