sm = 0
linex = 0
x, y, z = 0, 0, 0

with open('dataset_3363_4(2).txt', 'w') as text2:
    with open('dataset_3363_4.txt', 'r') as text:
        for line in text:
            linex += 1
            s = line.strip().split(';')
            sm = (int(s[-1]) + int(s[-2]) + int(s[-3])) / 3
            print(s[0], sm, file=text2)
            x += int(s[-3])
            y += int(s[-2])
            z += int(s[-1])
    print(x / linex, y / linex, z / linex, file=text2)





