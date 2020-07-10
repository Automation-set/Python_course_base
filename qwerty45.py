def update_dictionary(d, key, value):
    if key in d:
        d[key] += [value]
    elif key not in d:
        keyx = key * 2
        if keyx not in d:
            d[keyx] = [value]
        elif keyx in d:
            d[keyx] += [value]

print(update_dictionary(d, 1, -1))  # None
print(d)                            # {2: [-1]}
update_dictionary(d, 2, -2)
print(d)                            # {2: [-1, -2]}
update_dictionary(d, 1, -3)
print(d)


# Вариант из курса:
# def update_dictionary(d, key, value):
#     if key in d:
#         d[key] += [value]
#     elif 2 * key in d:
#         d[2 * key] += [value]
#     else:
#         d[2 * key] = [value]