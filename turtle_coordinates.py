sl = {'север': 0, 'запад': 0, 'восток': 0, 'юг': 0}
for i in range(int(input())):
    x = input().split()
    if x[0] in sl:
        sl[x[0]] += int(x[1])
print(sl['восток'] - sl['запад'], sl['север'] - sl['юг'])