def solutions(s):
    idx = 0
    new_str = ''
    for char in s:
        if char == ' ':
            new_str += char
            idx = 0
            continue
        elif idx % 2 == 0:
            new_str += char.upper()

        elif idx % 2 == 1:
            new_str += char.lower()
        idx += 1

    return new_str

print(solutions("try hello WORLD"))