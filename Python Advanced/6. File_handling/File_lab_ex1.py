try:
    with open("test.txt") as file:
        print("File found")
except:
    print("File not found")
