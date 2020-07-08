a = [int(i) for i in input().split()]
b = int(input())
x = 0
for i in range(len(a)):
    if b == a[i]:
        x += 1
        print(i, end=' ')
if x == 0:
    print('Отсутствует')