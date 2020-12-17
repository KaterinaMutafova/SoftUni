def contain_function(key_input, sub_input):
    if sub_input in key_input:
        return f"{key_input} contains {sub_input}"
    else:
        return f"Substring not found!"


def flip_function(key_input, up_low_value, start_i, end_i):
    for index in range(start_i, end_i):
        if up_low_value == "Upper":
            key_input[index] = key_input[index].upper()
        elif up_low_value == "Lower":
            key_input[index] = key_input[index].lower()

    key_input = ''.join(key_input)

    return key_input


def slice_function(key_input, start_i, end_i):
    new_list = key_input[0:start_i] + key_input[end_i:]
    key_input = ''.join(new_list)
    return key_input


raw_key = input()

command = input()

while not command == "Generate":
    command_data = command.split(">>>")

    if command_data[0] == "Contains":
        print(contain_function(raw_key, command_data[1]))

    elif command_data[0] == "Flip":
        raw_key = [str(el) for el in raw_key]
        start_index = int(command_data[2])
        end_index = int(command_data[3])
        raw_key = flip_function(raw_key, command_data[1], start_index, end_index)
        print(raw_key)

    elif command_data[0] == "Slice":
        raw_key = [str(el) for el in raw_key]
        start_index = int(command_data[1])
        end_index = int(command_data[2])
        raw_key = slice_function(raw_key, start_index, end_index)
        print(raw_key)

    command = input()

generated_key = ''.join(raw_key)

if command == "Generate":
    print(f"Your activation key is: {generated_key}")



