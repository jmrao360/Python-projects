def first_upper(str):
    if not str:
        return None
    
    if (str[0].isupper()):
        return str[0]
    return first_upper(str[1:])

print(first_upper("aXBc"))