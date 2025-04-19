def uniq_path(rows, columns):
    if rows == 1 or columns == 1:
        return 1
    
    return uniq_path(rows - 1, columns) + uniq_path(rows, columns - 1)


print(uniq_path(3,7))