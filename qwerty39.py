x = []
y = 0
end = ''
while True:
    if end == 'end':
        break
    for j in [input().split()]:
        if j == ['end']:
            end += 'end'
            break
        x += [[int(i) for i in j]]

for i in range(len(x)):
    for j in range(i):
        if i == j:
            y += x[i][i+1] + x[i][i-1] + x[j+1][j] + x[j+1][j-1]





print(x, y)

# x = [int(i) for i in input().split()]
# y = [int(i) for i in input().split()]
# z = [int(i) for i in input().split()]
# end = input()
#
# for i in range(len(x)+1):
#     for j in range(len(y)+1):
#
# 9 5 3
# 0 7 -1
# -5 2 -9
#
#
#
# a = [[9, 5, 3], [0, 7, -1], [-5, 2, 9]]

