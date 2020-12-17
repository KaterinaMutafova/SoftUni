# Find  the emoticon

message = input()

for index in range(len(message)):
    if message[index] == ":":
        result = message[index] + message[index+1]
        print(result)


