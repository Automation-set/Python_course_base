# a, b = (int(i) for i in input().split())
a = int(input())
b = int(input())
r = 0
o = 0
for j in range(a, b+1):
    if j % 3 == 0:
        r += j
        o += 1
print(r / o)