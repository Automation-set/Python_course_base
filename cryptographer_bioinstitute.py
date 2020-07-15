x, y, out1, out2 = input(), input(), input(), input()

sl = {key: value for key, value in zip(x, y)}
for i in out1:
    for key in sl:
        if key == i:
            print(sl[key], end='')
sl2 = {key: value for key, value in zip(y, x)}
print()
for i in out2:
    for key in sl2:
        if key == i:
            print(sl2[key], end='')

