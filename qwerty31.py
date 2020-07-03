n = [int(i) for i in input().split()]
s2 = []
if len(n) > 1:
    for j in range(len(n)):
        if j == 0:
            s2.append(n[1] + n[-1])
        elif j == len(n) - 1:
            s2.append(n[0] + n[-2])
        else:
            s2.append(n[j+1] + n[j-1])
    print(*s2)
else:
    print(*n)
