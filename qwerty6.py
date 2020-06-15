x = int(input())
h = int(input())
m = int(input())
y = (x + h * 60 + m)
H = y // 60
M = y - H * 60
print(H)
print(M)
