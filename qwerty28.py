genome = input()
j = genome[0]
z = 0
for i in genome:
    if i == j:
        z += 1
    elif i != j:
        print(j, z, sep="", end="")
        j = i
        z = 0+1
print(j, z, sep="")

# Другой вариант
# genome = input()+' '
# s = 0
# j = genome[0]
# for i in genome:
#     if i != j:
#         print(j + str(s), end="")
#         j = i
#         s = 0
#     s += 1