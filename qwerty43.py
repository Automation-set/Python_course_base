def modify_list(l):
    ls = []
    for i in l:
        if i % 2 == 0:
            ls.append(i // 2)
    l.clear()
    l.extend(ls)


lst = [1, 2, 3, 4, 5, 6]
modify_list(lst)
print(lst)

# Вариант с курсов:
# def modify_list(l):
#     l[:] = [i // 2 for i in l if i % 2 == 0]