# a = int(input())
# b = int(input())
# c = int(input())
# p = (a + b + c) / 2
# S = (p * (p - a) * (p - b) * (p - c)) ** 0.5
# print(S)

# x = int(input())
# y = -15 < x <= 12 or 14 < x < 17 or 19 <= x
# print(y)

a = float(input())
b = float(input())
z = input()
if z == 'mod':
    if b != 0:
        print(a % b)
    else:
        print('Деление на 0!')
elif z == '*':
    print(a * b)
elif z == '/':
    if b != 0:
        print(a / b)
    else:
        print('Деление на 0!')
elif z == '+':
    print(a + b)
elif z == '-':
    print(a - b)
elif z == 'pow':
    print(a ** b)
elif z == 'div':
    if b != 0:
        print(a // b)
    else:
        print('Деление на 0!')
