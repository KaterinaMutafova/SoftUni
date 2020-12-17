def password_validator(password):

    is_valid = True
    if not (6 <= len(password) <= 10):
        is_valid = False
        print(f"Password must be between 6 and 10 characters")

    for el in password:
        if not el.isdigit() and not el.isalpha():
            is_valid = False
            print(f"Password must consist only of letters and digits")
            break
    counter_digit = 0

    for el in password:
        if el.isdigit():
            counter_digit += 1
    if counter_digit < 2:
        is_valid = False
        print(f"Password must have at least 2 digits")

    return is_valid


passw = input()

is_valid = password_validator(passw)

if is_valid:
    print("Password is valid")


