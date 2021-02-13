def age_assignment(*args, **kwargs):
    names_tuple = args
    age_dict = kwargs
    new_names_dict = {}
    for n in names_tuple:
        for key,value in kwargs.items():
            if key[0] == n[0]:
                new_names_dict[n] = value
    return new_names_dict

print(age_assignment("Peter", "George", G=26, P=19))
print(age_assignment("Amy", "Bill", "Willy", W=36, A=22, B=61))