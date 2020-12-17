# pattern = (U\$)(?P<username>[A-Z][a-z]{2,})\1(P\@\$)(?P<password>[a-z]{5,}[0-9]{1,})\3

import re
pattern = r"(U\$)(?P<username>[A-Z][a-z]{2,})\1(P\@\$)(?P<password>[a-z]{5,}[0-9]{1,})\3"

list_valid_usernames = []
count_inputs = int(input())
a = 6
for input_iter in range(count_inputs):
    username_data = input()
    valid_username = re.match(pattern, username_data)
    if valid_username:
        obj = valid_username.groupdict()
        list_valid_usernames.append(valid_username)
        print("Registration was successful")
        print(f"Username: {obj['username']}, Password: {obj['password']}")
    else:
        print("Invalid username or password")

print(f"Successful registrations: {len(list_valid_usernames)}")












# 3
# U$MichaelU$P@$asdqwe123P@$
# U$NameU$P@$PasswordP@$
# U$UserU$P@$ad2P@$


# 2
# U$TommyU$P@$asdqwe123P@$
# Sara 1232412