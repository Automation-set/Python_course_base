a = int(input())
b = int(input())
c = int(input())

# a = 1 # 1 1 1 1 1 1 1 1 1 2 2 2 2 2 2 2 2 2 3 3 3 3 3 3 3
# b = 2 # 1 1 1 2 2 2 3 3 3 1 1 1 2 2 2 3 3 3 1 1 1 2 2 2 3
# c = 1 # 1 2 3 1 2 3 1 2 3 1 2 3 1 2 3 1 2 3 1 2 3 1 2 3 3

if a >= b >= c:
    print(a)
    print(c)
    print(b)
elif a >= c >= b:
    print(a)
    print(b)
    print(c)
elif b >= a >= c:
    print(b)
    print(c)
    print(a)
elif b >= c >= a:
    print(b)
    print(a)
    print(c)
elif c >= a >= b:
    print(c)
    print(b)
    print(a)
elif c >= b >= a:
    print(c)
    print(a)
    print(b)
