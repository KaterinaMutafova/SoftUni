def concatenate(*args):
    result = ''.join(["" + el for  el in args])
    return result



print(concatenate("Soft", "Uni", "Is", "Great", "!"))