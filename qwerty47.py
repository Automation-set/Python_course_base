with open('w.txt') as inf:
    x = inf.readline().strip()
    y = ''
    z = x[0]
    out = ''
    for i in x[1:]:
        if i.isalpha():
            out += (z * int(y))
            y, z = '', i
        elif i.isdigit():
            y += i
    out += (z * int(y))
with open('w.txt', 'w') as out2:
    out2.write(out)

