def get_info(**personal_info):

    return f"This is {personal_info.get('name')} from {personal_info.get('town')} and he is {personal_info.get('age')} years old"


print(get_info(**{"name": "George", "town": "Sofia", "age": 20}))
    