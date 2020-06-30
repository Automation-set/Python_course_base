# Вариант 1
n = int(input())

x = n // 1000
x1 = x // 100
x2 = x // 10 % 10
x3 = x % 10

y = n % 1000
y1 = y // 100
y2 = y // 10 % 10
y3 = y % 10

if (x1 + x2 + x3) == (y1 + y2 + y3):
    print('Счастливый')
else:
    print('Обычный')

# Вариант 2
a, b, c, d, f, e = input()
print('Счастливый' if int(a) + int(b) + int(c) == int(d) + int(f) + int(e) else 'Обычный')
