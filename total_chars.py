def count_chars(s):
    if len(s) == 0:
        return 0
    return len(s[0]) + count_chars(s[1:])


print(count_chars(["ab", "c", "def", "ghij"]))
