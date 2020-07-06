a = int(input())
b = a
for i in range(a+1):
    if b == 0:
        break
    for j in range(i):
        print(i, end=' ')
        b -= 1
        if b == 0:
            break
