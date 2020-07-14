sl = {}
n = int(input())

while n != 0:
    n -= 1
    x = int(input())
    if x not in sl:
        sl[x] = f(x)
        print(sl[x])
    elif x in sl:
        print(sl[x])


