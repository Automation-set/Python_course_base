genome = input()
genomeUp = genome.upper()
sl = 0
s = 0
for i in genomeUp:
    s += 1
    if i == 'G' or i == 'C':
        sl += 1
print(sl / s * 100)
