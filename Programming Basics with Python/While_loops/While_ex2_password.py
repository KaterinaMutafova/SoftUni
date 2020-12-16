username = input()
password = input()

confirm_pass = input()

while confirm_pass != password:
    confirm_pass = input()

print(f"Welcome {username}!")