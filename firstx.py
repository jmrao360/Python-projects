def find_idx_of_x(s):
    if (s[0] == 'x'):
        return 0
    return find_idx_of_x(s[1:]) + 1
    
  
print(find_idx_of_x("aaaaaaaaaaax"))