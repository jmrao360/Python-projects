def generate_number(idx):
    if idx == 0:
        return 0
    
    return idx + generate_number(idx -1)


print(generate_number(6))


