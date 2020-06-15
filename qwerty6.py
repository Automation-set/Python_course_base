x = int(input())
h = int(input())
m = int(input())
H = (x + h * 60 + m) // 60
aM = x + h * 60 + m
bM = aM // 60
M = aM - bM * 60
print(H)
print(M)
