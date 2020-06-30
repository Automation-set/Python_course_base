a = int(input())
b = int(input())
r = 1

while (r % a != 0) or (r % b != 0):
    r += 1

print(r)