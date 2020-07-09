x = []
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
    for j in range(len(x[i])):
        print(x[i][j-1] + x[i][-len(x[i])+j+1] + x[i-1][j] + x[i-len(x)+1][j], end=' ')
    print()

# Решение других:
# a = input()
# b = []
# while a != 'end':
#     b += [[int(i) for i in a.split()]]
#     a = input()
# for i in range(len(b)):
#     for j in range(len(b[0])):
#         print(b[(i-1)%len(b)][j] + b[(i+1)%len(b)][j] + b[i][(j-1)%len(b[0])] + b[i][(j+1)%len(b[0])], end=' ');
#     print()
