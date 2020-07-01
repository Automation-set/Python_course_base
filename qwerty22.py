a, b, c, d = int(input()), int(input()), int(input()), int(input())
for n in range(c, d+1):
    print('\t', n,  end="")
print()
for i in range(a, b+1):
    print(i, end="")
    for j in range(c, d+1):
        print('\t', j * i, end="")
    print()
