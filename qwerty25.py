# genome = 'ATGG'
# for i in range(4):
#     print(genome[i])

# Вариант перечисления всего генома
genome = 'CACCTGGAC'
s = 0
for c in genome:
    if c == 'C':
        s += 1
print(s)

# genome = input()
# print(genome.count('C'))