n = [int(i) for i in input().split()]
n.sort()
x = []
for i in range(len(n)):
    if i > 0:
        if n[i] == n[i-1]:
            if n[i] not in x:
                x += [n[i]]
print(*x)

# Другие варианты:
# str = [int(i) for i in input().split()]
# ans = []
# [ans.append(x) for x in str if x not in ans and str.count(x) > 1]
# print(*ans)
#
# Другое варианты:
# a = [int(i) for i in input().split()]
# s = []
# for i in a:
#     if a.count(i) >= 2 and i not in s:
#         s.append(i)
#         print(i, end=" ")