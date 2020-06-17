x = input()
if x == 'прямоугольник':
    a = float(input())
    b = float(input())
    print(a * b)
elif x == 'круг':
    r = int(input())
    p = float(3.14)
    S = (p * r) * r
    print(S)
elif x == 'треугольник':
    a = int(input())
    b = int(input())
    c = int(input())
    p = (a + b + c) / 2
    S = (p * (p - a) * (p - b) * (p - c)) ** 0.5
    print(S)