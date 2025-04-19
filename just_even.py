def just_even(myArray):
    if not myArray:
        return []
    
    if myArray[0] % 2 == 0:
        return [myArray[0]] + just_even(myArray[1:])
    else:
        return just_even(myArray[1:])

result = just_even([1, 2, 3, 5])
print(result)