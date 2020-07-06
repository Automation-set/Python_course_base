a, b = 0, 0
while True:
    i = int(input())
    a += i
    b += i * i
    if a == 0:
        break
print(b)

# Другой интересный пример
# s = [0, 0, 1]
# while s[2]:
#     i = int(input())
#     s = [s[0] + i, s[1] + i ** 2, s[0] + i]
# print(s[1])


