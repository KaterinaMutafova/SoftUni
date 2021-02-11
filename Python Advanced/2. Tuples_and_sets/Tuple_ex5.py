def get_dict():

    command = input()

    dict_contacts = {}
    while not command.isdigit():
        contact_name, contact_number = command.split("-")
        dict_contacts[contact_name] = contact_number

        command = input()

    is_found(command, dict_contacts)

    return command, dict_contacts, dict_contacts


def is_found(command, dict_contacts):
    if command.isdigit():
        number = int(command)
        for name in range(number):
            searched_name = input()
            if searched_name in dict_contacts:
                print(f"{searched_name} -> {dict_contacts[searched_name]}")
            else:
                print(f"Contact {searched_name} does not exist.")


get_dict()
