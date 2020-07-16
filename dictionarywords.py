sl, sl2 = [], []
for i in range(int(input())):
    sl += [input().lower()]
for j in range(int(input())):
    for i in input().lower().split():
        if i not in sl:
            sl2 += [i]
for p in set(sl2):
    print(p)
