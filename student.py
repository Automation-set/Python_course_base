sl = {'1': [], '2': [], '3': [], '4': [], '5': [], '6': [], '7': [], '8': [], '9': [], '10': [], '11': []}
with open('dataset_3380_5.txt', 'r') as school:
    for i in school:
        x = i.split()
        sl[x[0]].append(int(x[2]))

for i in sl:
    if sl[i] != None:
        out = sum(sl[i]) / len(sl[i])
        print(i, out)
    else:
        print(i, '-')
