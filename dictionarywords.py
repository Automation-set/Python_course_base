sl, sl2 = [], []
for i in range(int(input())):
    sl += [input()]
for j in range(int(input())):
    for i in input().lower().split():
        if i not in sl:
            sl2 += [i]
print(set(sl2))
