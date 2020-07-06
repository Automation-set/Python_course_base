# a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# print(a[1][1])

# n = 3
# a = [[0] * n] * n
# a[0][0] = 5
# print(a)

n = 3
a = [[0] * n for i in range(n)]
a[0][0] = 5
print(a)

a = [[0 for j in range(n)] for i in range(n)]